#!/usr/bin/env python

class Neuron:
  def __init__(self, name, isInhibitor = False):
    self.name = name
    self.inputWeight = {}
    self.output = []
    self.state = 0
    self.outputValue = (-1 if isInhibitor else 1)
    self.remainingEntries = 0

  def __str__(self):
    return "(%s): %f\toutput: %s \tinput: %s" % (self.name,
    ', '.join(n.name for n in self.output),
    str(self.inputWeight))

  def initialize(self):
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
    to all its ouput when every input has been taken into account ."""
    self.state += value * self.inputWeight[senderName]
    self.remainingEntries -= 1
    if self.remainingEntries == 0:
      returnValue = self.computeActivation()
      for o in self.output:
        o.send(self.name, returnValue)
      self.remainingEntries = len(self.inputWeight)
      # Reset neuron's state
      self.state = 0

  def computeActivation(self):
    """ Function of activation for this neurone.
    Should be implemented by child classes. """
    return 0
      

class ThresholdNeuron(Neuron):
  def __init__(self, name, threshold, isInhibitor = False):
    Neuron.__init__(self, name, isInhibitor)
    self.threshold = threshold

  def computeActivation(self):
    """ Function of activation for this neurone """
    if self.state >= self.threshold :
      return self.outputValue
    else:
      return 0
