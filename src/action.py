class Action:
  def __init__(self,name):
    self.name = name
    self.state = False

  def activate(self):
    print("")
    print(self.name + " has been activated")

  def send(self, senderName, value):
    if value > 0:
      self.state = True

  def addInput(sefl, newInputName, weight):
    """ Nothing to be done here. """
    pass

  def getState(self):
    """ Return the action's state and reset it. """
    resultState = self.state
    self.state = False
    return resultState
