
import helper

################################################## UNTESTED

def displayMenu(menuDict):

  # loop through the menuDict
  for key in menuDict:

    # print everything
    print(key + ' -> ' + menuDict[key])

def getUserChoice(menuDict):

  # create list of chocies
  choices = []

  # loop through menuDict and put choices into choices list
  for key in menuDict:

    # add choice to choices
    choices.append(key)

  # prompt stupid user until they enter a correct choice
  while True:

    # prompt stupid user
    userInput = input('Choice:')
    
    # check if userInput is in choices
    for choice in choices:

      # case check
      if userInput.strip().lower() == choice.strip().lower():
      
        # return the users input
        return userInput

def displayNumCoasters(coastersList):

  # get number of coasters
  numberOfCoasters = len(coastersList)

  # convert to string and display it
  print("The total number of coasters is " + str(numberOfCoasters))

def displayNumOperatingCoasters(coastersList):

  # set initial number of coasters to 0
  number = 0

  # loop through coasters list
  for coaster in coastersList:

    # check if current coaster is operating
    if coaster['status'] == 'status.operating':
      
      # increase number if so
      number += 1

  # convert string and print
  print("The total number of operating coasters is " + str(number))

def displayCoaster(coasterDict):
  name = coasterDict['name']
  park = coasterDict['park']
  speed = coasterDict['speed']
  height = coasterDict['height']
  length = coasterDict['length']
  status = coasterDict['status']
  print(name + ' [' + park + ']')
  print('\tSpeed = ' + speed + ' mph')
  print('\tHeight = ' + height + ' ft')
  print('\tLength = ' + length + ' ft')
  print('\tStatus is ' + status)

def displayFastestCoaster(coastersList):
  fastestCoaster = helper.getFastestCoaster(coastersList)
  displayCoaster(fastestCoaster)

def displayAllParks(coastersList):
  names = helper.getParksList(coastersList)
  names.sort()
  print('Amusement parks in alphabetical order:')
  for name in names:
    print(name)
  print('There are ' + str(len(names)) + ' unique parks.')

def displayCoastersInPark(coastersList):
  parkName = input('Enter a park:')
  coasters = []
  for coaster in coastersList:
    if coaster['park'].strip().lower() == parkName.strip().lower():
      coasters.append(coaster)
  for coaster in coasters:
    displayCoaster(coaster)

def findCoasters(coastersList):
  searchPhrase = input('Enter a search phrase:')
  coasters = []
  for coaster in coastersList:
    if searchPhrase.strip().lower() in coaster['name'].strip().lower():
      coasters.append(coaster)
  for coaster in coasters:
    displayCoaster(coaster)
  number = len(coasters)
  if number > 0:
    print('Found ' + str(number) + ' coasters that contain "' + searchPhrase + '"')
  else:
    print('No coasters contain the phrase "' + searchPhrase + '"')

