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
n1 = neuron.ThresholdNeuron("n1", 1  , 0.0      )
n2 = neuron.ThresholdNeuron("n2", 1  , 0.0      )
n3 = neuron.ThresholdNeuron("n3", 1  , 0.0, True)
n4 = neuron.ThresholdNeuron("n4", 1  , 0.0, True)
n5 = neuron.ThresholdNeuron("n5", 0.5, 0.0      )
n6 = neuron.ThresholdNeuron("n6", 0.5, 0.0      )

#Actions
a1 = action.Action("a1")
a2 = action.Action("a2")

#Connections
n1.connect(n3, 1)
n1.connect(n5, 1)
n2.connect(n4, 1)
n2.connect(n6, 1)
n3.connect(n6, 1)
n4.connect(n5, 1)

s1.connect(n1, 1)
s2.connect(n2, 1)

n5.connect(a1, 1)
n6.connect(a2, 1)
 
#Neural Network
network = neuralNetwork.NeuralNetwork()
network.addStimulus(s1)
network.addStimulus(s2)
network.addNeuron(n1)
network.addNeuron(n2)
network.addNeuron(n3)
network.addNeuron(n4)
network.addNeuron(n5)
network.addNeuron(n6)
network.addAction(a1)
network.addAction(a2)

network.initialize()

network.run([], True)
print("")
network.run(["s1"], True)
print("")
network.run(["s2"], True)
print("")
network.run(["s1", "s2"], True)
