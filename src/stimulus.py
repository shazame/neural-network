class Stimulus:
  def __init__(self, name):
    self.name = name
    self.outputNeurones = []

  def connect(self, neuron, weight):
    """ Connects the neuron to the stimulus. """
    self.outputNeurones += [neuron]
    neuron.addInput(self.name, weight)

  def update(self, activated=True):
    """ Sets the stimulus state and updates its ouput neurons. """
    value = (1.0 if activated else 0.0)
    for n in self.outputNeurones:
      n.send(self.name, value)
