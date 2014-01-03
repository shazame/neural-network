neural-network
==============

This project aims at building a minimal autonomous neural network system to simulate decision making. 

How to use it?
--------------

The application can be tested through our CLI (command-line interface).
To use it, open a shell and type: `./neural-cli.py`
You are then prompted for a command. You can type `help` to have more
information about available commands.

As an example we will create 3 neurons, connect them to each other, charge
them and activate some of them:

Create 3 neurons called n1, n2 and n3:

`$ create n1 n2 n3`

Connect n1 to n2, n1 to n3 and n2 to n3:

`$ connect n1 n2`

`$ connect n2 n3`

`$ connect n2 n3`

Charge n1, n2 and n3 to 2.3, 4.1 and 0.23 respectively:

`$ charge n1 2.3`

`$ charge n2 4.1`

`$ charge n3 0.23`

Dump neurons information to see their initial state:

`dump`

Discharge n2:

`$ activate n2`

Check neurons state update:

`dump`

Discharge n1:

`$ activate n1`

Then dump their state again:

`dump`

n1, n2 and n3 should now be to 0, 2.3 and 6.63 respectively.
