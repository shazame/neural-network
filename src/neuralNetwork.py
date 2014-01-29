#!/usr/bin/env python
import neuron
import stimulus
import action
import time

class NeuralNetwork:
  def __init__(self):
    self.stimuli = []
    self.actions = []
    self.neurons = []

  def initialize(self):
    for n in self.neurons:
      n.reinitialize()

  def addStimulus(self, newStimulus):
    """ Add the stimulus given in parameter to the neural network. """
    self.stimuli += [newStimulus]

  def addNeuron(self, newNeuron):
    """ Add the neuron given in parameter to the neural network. """
    self.neurons += [newNeuron]

  def addAction(self, newAction):
    """ Add the action given in parameter to the neural network. """
    self.actions += [newAction]

  def display(self):
    """ Display the neural network"""
    print("Stimuli: ")
    for s in self.stimuli:
      print(s)

    print("Neurons: ")
    for s in self.neurons:
      print(s)

    print("Actions: ")
    for a in self.actions:
      print(a)

  def run(self, activatedStimuliNames, display=False):
    """ Compute the decision taken by the network,
    based on activated simuli. """
    for s in self.stimuli:
      s.update(s.name in activatedStimuliNames)

    choices = []
    for a in self.actions:
      if a.getState() == True:
        choices += [a.name]

    if display:
      print("Activated stimuli: %s" % (str(activatedStimuliNames)))
      print("Neural network's choice: %s" % (str(choices)))

    return choices


if __name__ == "__main__":
  #Stimulus
  s1 = stimulus.Stimulus("s1")

  #Neurones
  n1 = neuron.ThresholdNeuron("n1", 1)

  #Actions
  a1 = action.Action("a1")

  #Connections
  s1.connect(n1, 1)
  n1.connect(a1, 1)
   
  #Neural Network
  network = NeuralNetwork()
  network.addNeuron(n1)
  network.addStimulus(s1)
  network.addAction(a1)
  network.initialize()

  network.run([], True)
  network.run(["s1"], True)
