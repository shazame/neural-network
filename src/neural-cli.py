#!/usr/bin/env python
import readline
import signal
import sys

import neuron

cmdlist = "help quit create connect activate list"

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
        print("Usage: create NEURON")
        print("Creates a new neuron named NEURON.")
    elif cmd == "connect":
        print("Usage: connect NEURON1 NEURON2")
        print("Creates a connection from  NEURON1 TO NEURON2.")
    elif cmd == "list":
        print("List available neurons.")
    else:
        other_cmd(cmd, True)

def nb_args(args):
    return len(args.split())

def cmd_equals(cmd, cmd_name):
    return cmd == cmd_name or cmd.startswith(cmd_name + " ")

def neuron_create(arg):
    if nb_args(arg) != 1:
        help("create")
    else:
        neural_network[arg] = neuron.Neuron(arg)
        print("Neuron " + arg + " created.")

def neuron_list(arg):
    if nb_args(arg) != 0:
        help("list")
    else:
        print('Neurons: ' + ', '.join(k for k,v in neural_network.items()))

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
    elif cmd_equals(cmd, "list"):
        neuron_list(cmd[4:].strip())
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
