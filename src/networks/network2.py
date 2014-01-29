import sys
sys.path.insert(0,"../")
import neuralNetwork
import neuron
import stimulus
import action
import time

#Stimulus
s1 = stimulus.Stimulus("s1")
s2 = stimulus.Stimulus("s2")

#Neurones
n1 = neuron.ThresholdNeuron("n1",2)
n2 = neuron.ThresholdNeuron("n2",2)
n3 = neuron.ThresholdNeuron("n3",1,True)
n4 = neuron.ThresholdNeuron("n4",1,True)
n5 = neuron.ThresholdNeuron("n5",1)
n6 = neuron.ThresholdNeuron("n6",1)

#Actions
a1 = action.Action("a1")
a2 = action.Action("a2")

#Connections
n1.connect(n3)
n1.connect(n5)
n2.connect(n4)
n2.connect(n6)
n3.connect(n6,1)
n4.connect(n5,1)

s1.addNeuron(n1,2)
s1.addNeuron(n2,0.5)
s2.addNeuron(n1,2)
s2.addNeuron(n2,0.5)

n5.addAction(a1)
n6.addAction(a2)
 
#Neural Network
network = neuralNetwork.NeuralNetwork()
network.addNeuron(n1)
network.addNeuron(n2)
network.addNeuron(n3)
network.addNeuron(n4)
network.addNeuron(n5)
network.addNeuron(n6)


for i in range(10):
  if (i % 2) == 0:
    s1.charge(1.5)
  if (i % 4) == 1:
    s2.charge(1.5)
  network.tick(True)
  time.sleep(1) 



