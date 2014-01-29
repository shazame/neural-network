#!/usr/bin/env python

class Neuron:
  def __init__(self, name, learningRate = 0, isInhibitor = False):
    self.name = name
    self.inputWeight = {}
    self.output = []
    self.state = 0
    self.outputValue = (-1 if isInhibitor else 1)
    self.remainingEntries = 0
    self.inputValues = {}
    self.learningRate = learningRate

  def __str__(self):
    return "(%s): %f\toutput: %s \tinput: %s" % (self.name,
    ', '.join(n.name for n in self.output),
    str(self.inputWeight))

  def reinitialize(self):
    self.state = 0
    self.inputValues = {}
    self.normalizeWeights()
    # Init number of entries
    self.remainingEntries = len(self.inputWeight)

  def normalizeWeights(self):
    weightSum = 0
    for _, v in self.inputWeight.items():
      weightSum += v
    for k, _ in self.inputWeight.items():
      self.inputWeight[k] /= weightSum

  def connect(self, newOutput, weight):
    """ Connects a neuron to a new output. """
    self.output += [newOutput]
    newOutput.addInput(self.name, weight)

  def addInput(self, newInputName, weight):
    """ Add an input to a neuron with a weight.
    The weight must be positive. """
    if weight < 0:
      print("Weight must a positive number.")
      print("Input is not added.")
      return
    self.inputWeight[newInputName] = weight

  def send(self, senderName, value):
    """ Update current neuron state and sends neurons's ouputValue 
    to all its ouput when every input has been taken into account."""
    inputValue = value * self.inputWeight[senderName]
    self.state += inputValue
    # Save value sent by each input
    self.inputValues[senderName] = inputValue
    self.remainingEntries -= 1
    if self.remainingEntries == 0:
      returnValue = self.computeActivation()
      for o in self.output:
        o.send(self.name, returnValue)

      self.updateWeights(returnValue)
      # Reset neuron's state (and normalise weights)
      self.reinitialize()

  def updateWeights(self, returnValue):
    """ Changes weights to reinforce valuable links."""
    for inputName, w in self.inputWeight.items():
      # Inibibor neurons are strengthen when return value is null
      if returnValue == 0 and self.inputValues[inputName] == -1:
        self.inputWeight[inputName] += self.learningRate * (1 - w)
      # Non inibibor neurons are strengthen when return value is not null
      if returnValue == 1 and self.inputValues[inputName] == 1:
        self.inputWeight[inputName] += self.learningRate * (1 - w)


  def computeActivation(self):
    """ Function of activation for this neurone.
    Should be implemented by child classes. """
    return 0
      

class ThresholdNeuron(Neuron):
  def __init__(self, name, threshold, learningRate = 0, isInhibitor = False):
    Neuron.__init__(self, name, learningRate, isInhibitor)
    self.threshold = threshold

  def computeActivation(self):
    """ Function of activation for this neurone """
    if self.state >= self.threshold :
      return self.outputValue
    else:
      return 0
