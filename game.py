import random
import sys


""" Rooms """

def room1():

  printNow("You have entered a dark musty chamber about the size of a childs bedroom.")
  
  printNow("The air is heavy and smells of rotten flesh.")
  printNow("You hear small creatures rustling around and the sound of water dripping.")
  
  # if player has torch
  printNow("As you move your torch around you notice a pile of bones in center of the room as tall as you are.")
  
  printNow("As you make your way further into the room you notice, in the faint light, that the walls are lined with skulls.")
  printNow("A deep chill enters your body and shakes you to your core.")
 

  
def room2():

  sword = Item('sword', 'weapon', 80)

  player = Player()

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
  printNow("You also notice a bright shinny sword at his side.")
  
  response = requestString("Do you want to pick up the sword. (yes or no)")
  response = response.lower()
  if response == 'yes' or response == 'y':
    player.pickUp(sword)
    
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
    else:
      item = player.useItem(response.lower())
      while not fight(item.getStrength()):
        printNow("You strike, but the Mummy strikes back")
        player.decrementHealth(25)
        printNow("You have lost 25 health points")
        printNow("You have "+ str(player.getHealth()) +" health pointsleft.")
    if player.getHealth <= 0:
      sys.exit("You lose!")
    else: 
      printNow("You have killed the mummy! Good job!")
  else:
    sys.exit("The Mummy is fast, he runs you down and kills you.")
        
  
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
       


def fight(weaponStrength):
  
  fightScore = random.randint(weaponStrength, 100)
  
  if fightScore > 90:
    return True
    
  return False
  
  
room2()
