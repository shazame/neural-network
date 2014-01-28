#!/usr/bin/env python2
import readline
import signal
import sys

import neuron

cmdlist = "help quit create connect activate charge show list dump"

# Neurons are stored in a dictionary to find them from their name
neural_network = {}

def complete(text, state):
    for cmd in cmdlist.split():
        if cmd.startswith(text):
            if not state:
                return cmd
            else:
                state -= 1

def other_cmd(cmd, in_help = False):
    if cmd not in cmdlist.split():
        print(cmd + ": is not a valid command.")
    elif in_help:
        print(cmd + ": is not documented yet.")
    else:
        print(cmd + ": is not implemented yet.")

def help(cmd):
    if cmd.startswith("help"):
        print("Display this help.")
        cmd = None
    if not cmd:
        print("Available commands are:")
        print("    " + cmdlist)
        print("Type \"help COMMAND\" to have more information about a specific command.")
    elif cmd == "quit":
        print("Quit this command interpreter.")
    elif cmd == "create":
        print("Usage: create NEURON1 [NEURON2 ... [NEURONn]]")
        print("Creates a new neurons with their name.")
    elif cmd == "connect":
        print("Usage: connect NEURON1 NEURON2")
        print("Creates a connection from  NEURON1 TO NEURON2.")
    elif cmd == "activate":
        print("Usage: activate NEURON")
        print("Activates a neuron, charging stimuli on its outputs.")
    elif cmd == "charge":
        print("Usage: charge NEURON VAL")
        print("charge a neuron with value VAL.")
    elif cmd == "show":
        print("Usage: show NEURON1 [NEURON2 ... [NEURONn]]")
        print("Display information about neurons.")
    elif cmd == "list":
        print("Usage: list")
        print("List available neurons.")
    elif cmd == "dump":
        print("Usage: dump")
        print("Dump every neurons information.")
    else:
        other_cmd(cmd, True)

def nb_args(args):
    return len(args.split())

def cmd_equals(cmd, cmd_name):
    return cmd == cmd_name or cmd.startswith(cmd_name + " ")

def neuron_create(arg):
    if nb_args(arg) < 1:
        help("create")
    else:
        for n in arg.split():
            if n in neural_network:
                print(n + " already exists.")
            else:
                neural_network[n] = neuron.Neuron(n)
                print("Neuron " + n + " created.")

def neuron_connect(arg):
    if nb_args(arg) != 2:
        help("connect")
    else:
        n1, n2 = arg.split()
        if not n1 in neural_network:
            print(n1 + " does not exist.")
            return
        if not n2 in neural_network:
            print(n2 + " does not exist.")
            return
        neural_network[n1].connect(neural_network[n2])

def neuron_activate(arg):
    if nb_args(arg) != 1:
        help("activate")
    else:
        if arg in neural_network:
            neural_network[arg].discharge()
            print("Neuron " + arg + " discharged.")
        else:
            print(arg + " does not exist.")

def neuron_charge(arg):
    if nb_args(arg) != 2:
        help("charge")
    else:
        n, v = arg.split()
        if not n in neural_network:
            print(n + " does not exist.")
        else:
            try:
                val = float(v)
            except:
                print(v + " should be a decimal number.")
                return
            neural_network[n].charge(val)

def neuron_show(arg):
    if nb_args(arg) < 1:
        help("show")
    else:
        for n in set(arg.split()):
            if n in neural_network:
                print(neural_network[n])
            else:
                print(n + " does not exist.")

def neuron_list(arg):
    if nb_args(arg) != 0:
        help("list")
    else:
        if neural_network:
            print('Neurons: ' + ', '.join(k for k,v in neural_network.items()))
        else:
            print('There are no neurons.')

def neuron_dump(arg):
    if nb_args(arg) != 0:
        help("dump")
    else:
        neuron_show(' '.join(k for k,v in neural_network.items()))

def command_process():
    try:
        cmd = raw_input('$ ')
    except:
        # And EOF may have been sent, we exit cleanly
        print("")
        return 0
    if not cmd:
        pass
    elif cmd_equals(cmd, "help"):
        help(cmd[4:].strip())
    elif cmd == "quit":
        return 0
    elif cmd_equals(cmd, "create"):
        neuron_create(cmd[6:].strip())
    elif cmd_equals(cmd, "connect"):
        neuron_connect(cmd[7:].strip())
    elif cmd_equals(cmd, "activate"):
        neuron_activate(cmd[8:].strip())
    elif cmd_equals(cmd, "charge"):
        neuron_charge(cmd[6:].strip())
    elif cmd_equals(cmd, "show"):
        neuron_show(cmd[4:].strip())
    elif cmd_equals(cmd, "list"):
        neuron_list(cmd[4:].strip())
    elif cmd_equals(cmd, "dump"):
        neuron_dump(cmd[4:].strip())
    else:
        other_cmd(cmd)
    return 1

readline.parse_and_bind("tab: complete")
readline.set_completer(complete)

# Handle interrupt signals (Ctrl+C) to avoid input errors
def signal_handler(signal, frame):
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    while command_process():
        pass
