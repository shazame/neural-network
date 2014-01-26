class Stimulus:
    def __init__(self, name):
        self.name = name
        self.outputNeurones = []

    def addNeuron(self, neuron, factor = 1):
        """ Connects the neuron to the stimulus """
        if factor > 0:
          if not neuron in self.outputNeurones:
            self.outputNeurones += [neuron]
            neuron.addInputStimulus(self,factor)
        else:
          print "Factor have to be positive"

    def charge(self, factor):
        """ Charge all neuron which are connected to the stimulus"""
        for n in self.outputNeurones:
            n.charge(factor,self)
