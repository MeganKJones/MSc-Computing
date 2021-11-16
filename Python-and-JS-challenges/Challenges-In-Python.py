# Exercise 1
def reduceFraction(num, den):
    '''
    importing math library to use 
    gcd method on num + den
    before dividing each number by the
    gcd and returning the answer.
    '''
    import math
    gcd = math.gcd(num, den)
    num = math.floor(num/gcd)
    den = math.floor(den/gcd)
    return num, den


# Exercise 2
def isMagicDate(dd, mm, yyyy):
  '''
  twoDigit is the inputted year % 100
  in order to get the last two digits.
  ddmm is the result of the day and 
  month multiplied. The two results 
  are checked to see if they're the same
  if they are- it's a magic number.
  '''
  twoDigit= yyyy % 100
  ddmm = dd * mm
  if ddmm == twoDigit:
    return True
  else:
    return False


# Exercise 3
def sublist(list):
  '''
  sublists is a list with an empty set
  of square brackets that will later hold
  all of the sublists. i loops through 
  each element to the end, j loops from i
  to the end. i and j are sliced from list
  and appended to sublists.
  '''
  sublists= [[]]
  for i in range(0, len(list) +1):
    for j in range(i+1,len(list) +1):
      sli = list[i:j]
      sublists.append(sli)
  return sublists


# Exercise 4
def pigLatin(word):
  #inputs that each character in the string will be checked against
  vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
  special = ["!", ".", ",", ":", "?", ";"]
  punct = None
  capital = False
  if word[-1] in special:
        punct= word[-1]
        word = word[:-1]
  #checks to see if last element is punctuation, if so word 
  #currently has no punctuation
  if word[0].upper() == word[0]:
        capital = True
        word = word.lower()
  #checks for a capital letter, is so it is lowered
  if word[0] in vowel:
        output = word + "way"
  #checks for first word being vowel, if so
  #"way" is added
  else:
      for i in range(len(word)):
          if word[i] in vowel:
              break
  #loop breaks when a vowel is found
      var1 = word[:i]
      var2 = word[i:]
      output = var2 + var1 + "ay"
  #word is split into two, before the vowel and after
  #and concatinated in concordance with pig latin
  if punct != None:
    output = output + punct
  #adds the punctuation back if there before
  if capital == True:
    output = output.capitalize()
  #capitalizes if it was before
  return output


# Exercise 5
def morseCode(text):
  #dictionary of letters/numbers and their morse equivalent
  dictionary ={"a":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".", "f":"..-.", "g":"--.", "h":"....", "i":"..", "j":".---", "k":"-.-", "l":".-..", "m":"--", "n":"-.", "o":"---", "p":".--.", "q":"--.-", "r":".-.", "s":"...", "t":"-", "u":"..-", "v":"...-", "w":".--", "x":"-..-", "y":"-.--", "z":"--..", "1":".----", "2":"..---", "3":"...--", "4":"....-", "5":".....", "6":"-....", "7":"--...", "8":"---..", "9":"--.", "0":"-----"}
  text = text.lower()
  string = ""
  #removes any capital letters to eliminate having to include the capital
  #versions of all letters in dictionary
  #empty string for morse translation
  for i in text:
    if i in dictionary:
      string += dictionary[i] + ' '
  #loop through each letter in text, checks if each letter is in dictionary
  #if so, the value is added to string, with a space in between
  #then stripped to avoid trailing whitespace
  return string.strip()


# Exercise 6
def int2Text(integer):
  #two dictionaries including numbers with non-repeated names
  ones = {"0": "zero", "1": "one", "2": "two", "3": "three", "4":"four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine", "10": "ten", "11": "eleven", "12": "twelve", "13": "thirteen", "14": "fourteen", "15": "fifteen", "16": "sixteen", "17": "seventeen", "18": "eighteen", "19": "nineteen"}
  decades = {"2": "twenty", "3": "thirty", "4": "forty", "5": "fifty", "6": "sixty", "7": "seventy", "8": "eighty", "9": "ninety"}

  string = str(integer)
  first = string[0]
  end = string[-1]
  #turns inputted integer into string
  #accesses first and last indicies

  if integer == "0":
    output = ones[string]
  #checks for zero
  elif integer < 20:
    output = ones[string]
  #checks for numbers under 20

  elif integer <= 99:
  #checks for 2 digit numbers over 20
    if end == "0":
      output = decades[first]
  #checks if ends in zero e.g. 30, 40, 50
    else:
      output = decades[first] + " " + ones[end]
  #all other numbers
      
  elif integer > 99:
  #checks three digit numbers
  #middle checks the second number of input
    middle = string[1]
    if middle == "0" and end == "0":
      output = ones[first] + " hundred"
  #checks for numbers like 100, 200, 300
    elif middle == "0":
      output = ones[first] + " hundred " + ones[end]
  #checks for numbers with middle 0. e.g. 103, 502
    elif end == "0" and middle != "1":
      output = ones[first] + " hundred " + decades[middle]
  #checks for numbers with no ones, but not ending in 10. e.g. 150, 330, 650
    elif middle == "1":
      output = ones[first] +" hundred " + ones[string[1:3]]
  #checks for numbers ending in "teens"
    elif middle != "1":
      output = ones[first] + " hundred " + decades[middle] + " " + ones[end]
  #rest of three digit numbers
  return output


# Exercise 7
def missingComment(file):
  #variables to open, read and split the
  #content of the file into lines
  fileOpen = open(file, "r")
  fileRead = fileOpen.read()
  lines = fileRead.split("\n")

  linenumber = 0
  names = []
  #variables for a counter and a list to store
  #the function names
  while linenumber < len(lines):
    if lines[linenumber].startswith("#"):
      linenumber += 1
    #checking for a comment, if so you skip past the next line
    elif lines[linenumber].startswith("def"):
        noDef = lines[linenumber][4:]
        noVar = noDef.split("(")
        name = noVar[0]
        names.append(name)
    #noDef slices from index 4 to get rid of "def"
    #then its split at the "(" with [0] being the
    #function name, so its appended to the list
    linenumber += 1
    #continuing the loop
  return names


# Exercise 8
def consistentLineLength(file, maxLen):
#variables to open, read, replace any new lines with spaces
#then spliting at spaces so we have the separate words
  fileOpen = open(file, "r")
  fileRead = fileOpen.read()
  fileLine = fileRead.replace("\n", " ")
  word = fileLine.split(" ")
  
  maxLines = []
  line = ""
#maxLines is a list to store the output
#each line will be appended to maxLines
  for i in word:
#looping through each word in variable
    if len(i) + len(line) +1 <= maxLen:
      line = line + " " + i
      line = line.strip()
#the length of the word and length of "line" + 1 to simulate
#the space that will be added. if not over maxLen
#will add more words to line until maxLen reached.
    else:
      maxLines.append(line.strip())
      line = i
#once line has hit the maxLen, it will append to maxLines
#reset i
  maxLines.append(line.strip())
#append last line since its not hit maxLen
  return maxLines

# Exercise 9
def knight(initialPos, finalPos, moves):
#making initialPos into coordinates
  initX = "abcdefgh".index(initialPos[0])
  initY = int(initialPos[1]) - 1
#making finalPos into coordinates
  finalX = "abcdefgh".index(finalPos[0])
  finalY = int(finalPos[1]) - 1
  finalTuple = (finalX, finalY)
#variables needed for looping
  knightMoves = [(2,1), (1,2), (-1,2), (-2,1), (-2,-1), (-1,-2), (1,-2), (2,-1)]
  counter = 0
  XX= initX
  YY= initY
  thisMove = []
  nextMoves = [(XX,YY)]
  lastMoves = []
  '''
  i and j loop through the tuples in knightMoves, add them to the coordinates of
  initialPos, and the resulting coordinate is appended if it is a position on the
  board. XX and YY from that loop are used to make the next round of coordinates,
  this is done as many times as there are moves in the given variable "moves"
  if the coordinates of the finalPos is in that long list of possible moves-
  true is returned.
  '''
  while counter < moves:
    for XX, YY in nextMoves:
      for i,j in knightMoves:
        x = i + XX
        y = j + YY
        if x > 0 and x < 7 and y > 0 and y < 7:
          thisMove.append((x, y))
      nextMoves=thisMove.copy()
      lastMoves+=thisMove
      thisMove = []
    counter += 1  
  if finalTuple in lastMoves:
    return True
  else:
    return False


# Exercise 10
def warOfSpecies(environment):
    return None
