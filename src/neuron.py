#!/usr/bin/env python

class Neuron:
    def __init__(self, name):
        self.name = name
        self.output = []
        self.state = 0

    def __str__(self):
        return "(%s) state: %d\toutput: %s" % (self.name, self.state,
        ', '.join(n.name for n in self.output))

    def connect(self, neuron):
        """ Connects the neuron's output to another neuron. """
        self.output += [neuron]

    def send(self, stimulus):
        """ Send a stimuli to the neuron. """
        self.state += stimulus

    def discharge(self):
        """ Discharge the neuron, sending stimuli on its outputs. """
        for o in self.output:
            o.send(self.state)
        self.state = 0

if __name__ == "__main__":
    n1 = Neuron("n1")
    n2 = Neuron("n2")
    n3 = Neuron("n3")
    n1.connect(n2)
    n1.connect(n3)
    n2.connect(n3)

    print("Set the initial state of n1 to 2:")
    n1.send(2)
    print(n1)
    print(n2)
    print(n3)

    print("")
    print("Discharge n1:")
    n1.discharge()
    print(n1)
    print(n2)
    print(n3)

    print("")
    print("Discharge n2:")
    n2.discharge()
    print(n1)
    print(n2)
    print(n3)
