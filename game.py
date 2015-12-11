import random
import sys


def welcome():
  
  printNow("Welcome to:")
  printNow("*** Stuck in the Catacombs ***")
  printNow("When presented with choices you can always use the following commands:")
  printNow("'help', to print this message again")
  printNow("'exit', to leave the game")
  return
  
""" Rooms """

def room1(player=None):

  #first room in the game needs this
  if player is None:
    player = Player()
    
  # setup your valid directional choices for this room
  validChoices = ['south']

  printNow("You have entered a dark musty chamber about the size of a childs bedroom.")
  
  printNow("The air is heavy and smells of rotten flesh.")
  printNow("You hear small creatures rustling around and the sound of water dripping.")
  
  # if player has torch
  printNow("As you move your torch around you notice a pile of bones in center of the room as tall as you are.")
  
  printNow("As you make your way further into the room you notice, in the faint light, that the walls are lined with skulls.")
  printNow("A deep chill enters your body and shakes you to your core.")
  
  printNow("You you see a doorway to your south. It is the only direction you can travel.")
  direction = requestString("Which direction would you like to go: ")
  
  goDirection(player, 'room1', validChoices, direction)
 

  
def room2(player):

  # setup your valid directional choices for this room
  validChoices = ['north']
  
  # setup an "Item", 
  sword = Item('sword', 'weapon', 80)


  printNow("As you enter the chamber, you stumble on a hole in the foor.")
  
  printNow("You fall and land in a puddle of putrid water.")
  printNow("Your torch is extinguished and you are now wet, cold and smell like a corps.")
  
  printNow("Though you feel you now fit in with the other inhabitants, you are horrified as the darkness envelopes you.")
  printNow("You try to re-light your candle, but it is to wet. You cast it asside in hope you will find another one.")
  printNow("You decide it is wise to save your matches in case of a more serous emergency.")
  printNow("You begin to feel around on the ground looking for the walls.")
  printNow("When you find the wall you trace them around the room feeling along the skulls as you go.")
  printNow("Luckily you find what feels like a torch.")
  printNow("You light a match and the torch illuminates the room.")
  
  printNow("Immediately you notice a suit of armor in the corner.")
  printNow("As you approach you see that dead eyes of the Knights skull inside his helmit.")
  
  if not player.hasItem('sword'):
    printNow("You also notice a bright shinny sword at his side.")
  
    response = requestString("Do you want to pick up the sword. (yes or no)")
    response = response.lower()
    if response == 'yes' or response == 'y':
      player.pickUp(sword)
    
  if not player.inHistory('killed_mummy'):
    printNow("Suddenly a Mummy breaks through the wall of skulls. It's threads a hang about it's body in tatters.")
    printNow("You realize that it will kill you if you don't do something quickly.")
    
    response = requestString("Do you want to fight or run? (fight or run)")
    response = response.lower()
    if response == 'fight' or response == 'f':
      printNow("You have:")
      player.listItems()
      response = requestString("Pick an item by name to use as a weapon.")
      if not player.hasItem(response.lower()):
        printNow("You don't have that item. It's now to late to find another, you will have to fight bare handed")
        
        # call fight control
        fightControl(player, 0, 'Mummy', 25)
        
      else:
        item = player.useItem(response.lower())
        
        # call fight control
        fightControl(player, item.getStrength(), 'Mummy', 25)
          
      if player.getHealth() < 1:
        sys.exit("You lose!")
      else: 
        player.addHistory("killed_mummy")
        printNow("You have killed the mummy! Good job!") 
    else:
      sys.exit("The Mummy is fast, he runs you down and kills you.")
      
  printNow("You you see a doorway to your north. It is the only direction you can travel.")
  direction = requestString("Which direction would you like to go: ")
    
  goDirection(player, 'room2', validChoices, direction)
    
    
"""function goDirection keeps track of the player allowed directions and checks their validity 
it also keeps track of doors and contains the win and lose conditions"""
def goDirection(player, roomName, validChoices, playerChoice):

  choices = ['help', 'exit']
  choices.extend(validChoices)

  while playerChoice.lower() not in choices:
    playerChoice = requestString("Please enter a valid direction: ")
  
  if playerChoice.lower() == "help":
    welcome()
    
  if playerChoice.lower() == "exit":  
    sys.exit("Goodbye. Thank you for playing.")
      
  # room1 choices here 
  if roomName == 'room1':
    if playerChoice.lower() == "south":
      room2(player)
      
  # room2 choices here
  elif roomName == 'room2':
    if playerChoice.lower() == "north":
      room1(player)
      
      
def fightControl(player, strength, monster, penalty):
  while not fight(strength):
    printNow("You strick the "+monster+", but the "+monster+" strikes back")
    player.decrementHealth(penalty)
    printNow("You have lost "+str(penalty)+" health points")
    if player.getHealth() < 1:
      return
    printNow("You have "+ str(player.getHealth()) +" health points left.")
  return

def fight(weaponStrength):
  
  fightScore = random.randint(weaponStrength, 100)
  
  if fightScore > 90:
    return True
    
  return False
  
            
  
"""Class Item represents items in the game"""
class Item:
  name = None
  action = None
  strength = 0
  
  def __init__(self, name, action, strength=0):
    self.name = name
    self.action = action
    self.strength = strength
  
  """Method getName returns string name of an item"""
  def getName(self):
    return self.name
  
  """Method getAction returns string action of an item"""
  def getAction(self):
    return self.action
    
  """Method getStrength returns numeric strength of an item"""
  def getStrength(self):
    return self.strength

"""Class Player represents players in the game"""
class Player:
  
  def __init__(self):
    self.trackHistory = []
    self.knapsack = [];
    self.health = 100
  
  """Method pickUp adds item to player knapsack"""
  def pickUp(self, item):
    self.knapsack.append(item)

  """Method hasItem return bolean if player has item with name"""
  def hasItem(self, name):
    for item in self.knapsack:
      if item.getName() == name:
        return True
    return False

  """Method discardItem remove an item from player knapsack"""
  def discardItem(self, item):
    count = 0
    for item in self.knapsack:
      if item.getName() == name:
        self.knapsack.pop(count) 
      count = count + 1

  """Method useItem use an item from player knapsack"""
  def useItem(self, name):
    for item in self.knapsack:
      if item.getName() == name:  
        return item

  """Method listItems list items in player knapsack"""
  def listItems(self):
    for item in self.knapsack:
      if item is not None:
        printNow(item.getName() + ", cabability: " + item.getAction())
    return

  """Method decrementHealth lose heath points"""
  def decrementHealth(self, loss):
    self.health = self.health - loss
    return  

  """Method getHealth return heath points"""
  def getHealth(self):
    return self.health
    
  """Method addHistory adds a note to a players history"""  
  def addHistory(self, note):
    self.trackHistory.append(note)
    
  """Method inHistory check if a note is in a players history"""    
  def inHistory(self, note):
    return (note in self.trackHistory)
      
  

welcome()
room1()
