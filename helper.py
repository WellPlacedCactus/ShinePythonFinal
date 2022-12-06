
def createCoastersFromFile(filenameStr='roller_coasters.csv'):

  # create a list of coasters
  coasterList = []

  # get contents of file
  fileCoaster = open(filenameStr, 'r', encoding='utf8')

  # get first line of file
  header = fileCoaster.readline().strip()

  # parse first line into array to get individual headers
  headerList = header.split(",")

  # loop through each line in file
  for line in fileCoaster:

    # create a new coaster dict
    coasterDict = {}

    # strip out white space from the current line
    line = line.strip()

    # convert line into lineList for parsing
    lineList = line.split(',')

    # loop through the values
    for i in range(len(headerList)):

      # get key
      key = headerList[i]

      # get value
      value = lineList[i]

      # set key value pair in current dict
      coasterDict[key] = value

    # add current coaster dict to list of all coaster dicts
    coasterList.append(coasterDict)

  # close the file
  fileCoaster.close()

  # return the coaster dicts
  return coasterList

def getParksList(coastersList):

  # create list of park names
  parkNames = []

  # loop through coaster lists given in parameter
  for coaster in coastersList:

    # check if coaster name is not in park names already
    if coaster['name'] not in parkNames:

      # add coaster name to park names if the above condition holds true
      parkNames.append(coaster['name'])

  # return park names
  return parkNames

def getFastestCoaster(coastersList):

  # create a fake coaster with no speed to compare to initially
  fastestCoaster = { 'speed': 0 }

  # loop through all coasters given in the parameter
  for coaster in coastersList:

    # check if the speed is numeric, if it is nothing then continue on
    if (coaster['speed'].isnumeric()):

      # check if the speed is faster than the current coaster
      if int(coaster['speed']) > int(fastestCoaster['speed']):

        # if it is, set the fastest coaster equal to the new coaster
        fastestCoaster = coaster

  # return the coaster
  return fastestCoaster