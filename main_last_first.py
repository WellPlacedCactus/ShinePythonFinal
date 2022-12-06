
import helper
import user_interface

def getMenuDict():
  return {
    "A": "Number of coasters", 
    "B": "Number of operating coasters", 
    "C": "Fastest coaster", 
    "D": "Amusement parks", 
    "E": "Coasters in a park", 
    "F": "Find coasters", 
    "Q": "Quit"
  }

def main():
  print('Rollar Coasters')
  coasters = helper.createCoastersFromFile()
  menuDict = getMenuDict()
  user_interface.displayMenu(menuDict)
  choice = user_interface.getUserChoice(menuDict)

  if choice.strip().lower() == 'a':
    user_interface.displayNumCoasters(coasters)
  elif choice.strip().lower() == 'b':
    user_interface.displayNumOperatingCoasters(coasters)
  elif choice.strip().lower() == 'c':
    user_interface.displayFastestCoaster(coasters)
  elif choice.strip().lower() == 'd':
    user_interface.displayAllParks(coasters)
  elif choice.strip().lower() == 'e':
    user_interface.displayCoastersInPark(coasters)
  elif choice.strip().lower() == 'f':
    user_interface.findCoasters(coasters)
  elif choice.strip().lower() == 'q':
    return

main()