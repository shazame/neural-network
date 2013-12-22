#!/usr/bin/env python
import readline

cmdlist = "help quit create connect activate list"

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
        print("List availables neurons.")
    else:
        other_cmd(cmd, True)


def command_process():
    cmd = raw_input('$ ')
    if not cmd:
        pass
    elif cmd == "help" or cmd.startswith("help "):
        help(cmd[4:].strip())
    elif cmd == "quit":
        return 0
    else:
        other_cmd(cmd)
    return 1

readline.parse_and_bind("tab: complete")
readline.set_completer(complete)

if __name__ == "__main__":
    while command_process():
        pass
