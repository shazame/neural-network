#!/usr/bin/env python

class Neuron:
    def __init__(self, name):
        self.name = name
        self.inputNeurones = []
        self.inputFactor = []
        self.outputNeurones = []
        self.state = 0.0

    def __str__(self):
        return "(%s) state: %f\toutput: %s \tinput: %s" % (self.name, self.state,
        ', '.join(n.name for n in self.outputNeurones),
        ', '.join(n.name for n in self.inputNeurones))

    def connect(self, neuron, factor = 0.5):
        """ Connects the neuron's output to another neuron. """
        if not neuron in self.outputNeurones:
            self.outputNeurones += [neuron]
            neuron.connectFrom(self, factor)

    def connectFrom(self, neuron, factor = 0.5):
        """ Connects the neuron's input to another neuron. """
        if not neuron in self.inputNeurones:
            self.inputNeurones += [neuron]
            self.inputFactor += [factor]
            neuron.connect(self, factor)

    def activationFunction(self):
        """ Function of activation for this neurone """
            
    def charge(self, stimulus):
        """ Charge the neuron """
        self.state += stimulus
        #self.activationFunction()

    def send(self, neuron, stimulus):
        """ Send a stimuli to the neuron. """
        index = self.inputNeurones.index(neuron)
        self.state += stimulus * self.inputFactor[index]
        print(self.state)
        if self.state < 0 :
            self.state = 0
        #self.activationFunction()

    def discharge(self):
        """ Discharge the neuron, sending stimuli on its outputs. """
        for o in self.outputNeurones:
            o.send(self, self.state)
        self.state = 0

class ThresholdNeuron(Neuron):
    def __init__(self, name, threshold):
        Neuron.__init__(self, name)
        self.threshold = threshold

    def activationFunction(self):
        """ Function of activation for this neurone """
        if self.state > self.threshold :
            self.discharge()


if __name__ == "__main__":
    n1 = Neuron("n1")
    n2 = ThresholdNeuron("n2",1)
    n3 = ThresholdNeuron("n3",2)
    n4 = Neuron("n4")
    n1.connect(n2)
    n1.connect(n3)
    n2.connect(n3,-1)
    n2.connect(n4)
    n3.connect(n4)

    print("Set the initial state of n1 to 2:")
    n1.charge(2.3)
    print(n1)
    print(n2)
    print(n3)
    print(n4)

    print("")
    print("Discharge n1:")
    n1.discharge()
    print(n1)
    print(n2)
    print(n3)
    print(n4)

    print("")
    print("Discharge n2:")
    n2.discharge()
    print(n1)
    print(n2)
    print(n3)
    print(n4)
