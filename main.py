import urlParser
import counter

def userScreen():
  userChoice = int(input("Please Choose :\n1 -> KW count from File\n2 -> KW count from website\n\t\t\t:"))
  try:
    if userChoice == 1:
      counter.letsCount("testFile.txt")
    elif userChoice == 2:
      urlParser.theParser()
      
  except:
    print("Please enter a valid choice!")
    userScreen()

# Driver 
userScreen()