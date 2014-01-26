#!/usr/bin/env python
import neuron
import stimulus
import action
import time

class NeuralNetwork:
  def __init__(self):
    self.neurones = []
    self.stimulus = []

  def addStimulus(self, stimulus):
    """ Add the stimulus given in parameter to the neural network"""
    self.stimulus += [stimulus]

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
  #Stimulus
  s1 = stimulus.Stimulus("s1")
  s2 = stimulus.Stimulus("s2")

  #Neurones
  n1 = neuron.ThresholdNeuron("n1",2)
  n2 = neuron.ThresholdNeuron("n2",2,True)
  n3 = neuron.ThresholdNeuron("n3",1)
  n4 = neuron.ThresholdNeuron("n4",1)

  #Actions
  a1 = action.Action("a1")
  a2 = action.Action("a2")

  #Connections
  n1.connect(n3)
  n3.connect(n2,1)
  n2.connect(n4)
  n4.connect(n1,1)

  s1.addNeuron(n1)
  s2.addNeuron(n2)

  n1.addAction(a1)
  n2.addAction(a2)
   
  #Neural Network
  network = NeuralNetwork()
  network.addNeuron(n1)
  network.addNeuron(n2)
  network.addNeuron(n3)
  network.addNeuron(n4)
  network.addStimulus(s1)
  network.addStimulus(s2)


  for i in range(10):
    if (i % 2) == 0:
      s1.charge(1.5)
    if (i % 4) == 1:
      s2.charge(1.5)
    network.tick(True)
    time.sleep(1) 

