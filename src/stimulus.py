class Stimulus:
    def __init__(self, name):
        self.name = name
        self.outputNeurones = []

    def addNeuron(self, neuron):
        """ Connects the neuron to the stimulus """
        self.outputNeurones += [neuron]

    def charge(self, factor):
        """ Charge all neuron which are connected to the stimulus"""
        for n in self.outputNeurones:
            n.charge(factor)
