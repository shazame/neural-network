#!/usr/bin/env python
import neuron

class NeuralNetwork:
    def __init__(self):
        self.neurones = []

    def addNeuron(self, neuron):
        """ Add the neuron given in parameter to the neural network"""
        self.neurones += [neuron]

    def tick(self,display=False):
        """ Execute one tick of the neural network"""
        for n in self.neurones:
            n.activationFunction()
        for n in self.neurones:
            n.updateState()
        if display:
            self.display()

    def display(self):
        """ Display the neural network"""
        print()
        for n in self.neurones:
            print(n)

    def run(self, nbTick, display=False):
        """ Execute nbTick if the neural network"""
        for i in nbTick:
            self.tick(display)


if __name__ == "__main__":
    n1 = neuron.ThresholdNeuron("n1",1)
    n2 = neuron.ThresholdNeuron("n2",1)
    n3 = neuron.ThresholdNeuron("n3",2)
    n4 = neuron.Neuron("n4")
    n1.connect(n2)
    n1.connect(n3)
    n2.connect(n3,-1)
    n2.connect(n4)
    n3.connect(n4)

    network = NeuralNetwork()
    network.addNeuron(n1)
    network.addNeuron(n2)
    network.addNeuron(n3)
    network.addNeuron(n4)

    n1.charge(2.3)
    network.tick(True)
    network.tick(True)
    network.tick(True)

