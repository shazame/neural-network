#!/usr/bin/env python

class Neuron:
  def __init__(self, name, isInhibitor = False):
    self.name = name
    self.inputNeurones = []
    self.inputFactor = []
    self.outputNeurones = []
    self.outputActions = []
    self.state = 0.0
    self.nextState = 0.0
    self.inhibitorFactor = (-1.0 if isInhibitor else 1.0)

  def __str__(self):
    return "(%s) state: %f\toutput: %s \tinput: %s" % (self.name, self.state,
    ', '.join(n.name for n in self.outputNeurones),
    ', '.join(n.name for n in self.inputNeurones))

  def addAction(self, action):
    self.outputActions += [action]

  def connect(self, neuron, factor = 0.5):
    """ Connects the neuron's output to another neuron. """
    if factor > 0 :
      if not neuron in self.outputNeurones:
        self.outputNeurones += [neuron]
        neuron.connectFrom(self, factor)
    else :
      print "Factor have to be positive"

  def connectFrom(self, neuron, factor = 0.5):
    """ Connects the neuron's input to another neuron. """
    if factor > 0 :
      if not neuron in self.inputNeurones:
        self.inputNeurones += [neuron]
        self.inputFactor += [factor]
        neuron.connect(self, factor)
    else:
      print "Factor have to be positive"

  def updateState(self):
    """ Put the neuron into the next state"""
    self.state = self.nextState

  def activationFunction(self):
    """ Function of activation for this neurone """
      
  def charge(self, stimulus):
    """ Charge the neuron """
    self.nextState += stimulus

  def send(self, neuron, stimulus):
    """ Send a stimuli to the neuron. """
    index = self.inputNeurones.index(neuron)
    self.nextState += stimulus * self.inputFactor[index]
    if self.nextState < 0 :
      self.nextState = 0

  def discharge(self):
    """ Discharge the neuron, sending stimuli on its outputs. """
    for a in self.outputActions:
      a.activate()
    for o in self.outputNeurones:
      o.send(self, self.state * self.inhibitorFactor)
    self.nextState -= self.state
    if self.nextState < 0 :
      self.nextState = 0

class ThresholdNeuron(Neuron):
  def __init__(self, name, threshold, isInhibitor = False):
    Neuron.__init__(self, name, isInhibitor)
    self.threshold = threshold

  def activationFunction(self):
    """ Function of activation for this neurone """
    if self.state > self.threshold :
      self.discharge()


if __name__ == "__main__":
  n1 = Neuron("n1")
  n2 = ThresholdNeuron("n2",1,True)
  n3 = ThresholdNeuron("n3",2)
  n1.connect(n2)
  n1.connect(n3,2)
  n2.connect(n3,1)

  print("Set the initial state of n1 to 2:")
  n1.charge(2.3)
  n1.updateState()
  n2.updateState()
  n3.updateState()
  print(n1)
  print(n2)
  print(n3)

  print("")
  print("Discharge n1:")
  n1.discharge()
  n1.updateState()
  n2.updateState()
  n3.updateState()
  print(n1)
  print(n2)
  print(n3)

  print("")
  print("Discharge n2:")
  n2.discharge()
  n1.updateState()
  n2.updateState()
  n3.updateState()  
  print(n1)
  print(n2)
  print(n3)
