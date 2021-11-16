// Exercise 1
function reduceFraction(num, den) {
//variables to store answers
let numFact = [];
let denFact = [];
let factors = [];

for (let n = 0; n <= num; n++) {
  if (num % n === 0){
    numFact.push(n);
  }
//creating an array of "num's" factors
}
for (let m = 0; m <= den; m++) {
  if (den % m === 0){
    denFact.push(m);
  }
//creating an array of "den's" factors
}
for (let i = 0; i < numFact.length; i++) {
  for (let j = 0; j < denFact.length; j++) {
    if (numFact[i] === denFact[j]) {
      factors.push(numFact[i])
    }
//comparing the two arrays, factors that are the same
//are added to "factors"
  }
}
let gcd = Number(factors.slice(-1));
let reduceNum = Math.floor(num / gcd);
let reduceDen = Math.floor(den / gcd);
//find the gcd by accessing last in array
//divide both numbers by gcd and return result
return [reduceNum, reduceDen];
}

// Exercise 2
function isMagicDate(dd, mm, yyyy) {
/* 
  twoDigit is the inputted year % 100
  in order to get the last two digits.
  ddmm is the result of the day and 
  month multiplied. The two results 
  are checked to see if they're the same
  if they are- it's a magic number.
*/
let twoDigit = yyyy % 100;
let ddmm = dd * mm;

if (ddmm === twoDigit) {
  return true;
}
else {
    return false;
}
}


// Exercise 3
const sublist = array => {
/*
  sublists is an array with an empty set
  of square brackets that will later hold
  all of the sublists. i loops through 
  each element to the end, j loops from i
  to the end. i and j are sliced from array
  and pushed to sublists.
*/
    let sublists = [[]];

  for (let i = 0; i < array.length +1; i++) {
    for (let j = i+1; j < array.length +1; j++) {
      let sli = array.slice(i,j)
      sublists.push(sli);
    }
  }
return sublists;
}


// Exercise 4
const pigLatin = word => {
//inputs that each character in the string will be checked against
    let vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"];
    let special = ["!", ".", ",", ":", "?", ";"];
    let punct = null;
    let capital = false;
    
    if (special.includes(word.slice(-1))) {
          punct= word.slice(-1)
          word = word.slice(0,-1);
//checks to see if last element is punctuation, if so word 
//currently has no punctuation
    }
    if (word[0].toUpperCase() === word[0]) {
          capital = true
          word = word.toLowerCase();
//checks for a capital letter, is so it is lowered
    }
    if (vowel.includes(word[0])) {
          output = word + "way";
//checks for first word being vowel, if so
//"way" is added
    }
    else{
        for (i = 0; i < word.length; i++) {
          if (vowel.includes(word[i])) {
            break;
//loop breaks when a vowel is found
          }
        }
    
        var1 = word.slice(0,i);
        var2 = word.slice(i);
        output = var2 + var1 + "ay";
//word is split into two, before the vowel and after
//and concatinated in concordance with pig latin
    }
    if (punct !== null) {
      output = output + punct;
//adds the punctuation back if there before
    }
    if (capital === true) {
      output = output[0].toUpperCase() + output.slice(1);
//capitalizes if it was before
    }
    return output;
}

// Exercise 5
const morseCode = text => {
//object of letters/numbers and their morse equivalent
  object ={"a":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".", "f":"..-.", "g":"--.", "h":"....", "i":"..", "j":".---", "k":"-.-", "l":".-..", "m":"--", "n":"-.", "o":"---", "p":".--.", "q":"--.-", "r":".-.", "s":"...", "t":"-", "u":"..-", "v":"...-", "w":".--", "x":"-..-", "y":"-.--", "z":"--..", "1":".----", "2":"..---", "3":"...--", "4":"....-", "5":".....", "6":"-....", "7":"--...", "8":"---..", "9":"--.", "0":"-----"}
  
  text = text.toLowerCase();
  let string = "";
//removes any capital letters to eliminate having to include the capital
//versions of all letters in object
//empty string for morse translation
  for (let i = 0; i<= text.length; i++) {
    if (text[i] in object){
    string+=object[text[i]] + " "
    }
//loop through each letter in text, checks if each letter is in object
//if so, the value is added to string, with a space in between
//then stripped to avoid trailing whitespace
  }
  return string.trim();
  }

// Exercise 6
const int2Text = num => {
//two objects including numbers with non-repeated names
  const ones = { "0": "zero", "1": "one", "2": "two", "3": "three", "4":"four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine", "10": "ten", "11": "eleven", "12": "twelve", "13": "thirteen", "14": "fourteen", "15": "fifteen", "16": "sixteen", "17": "seventeen", "18": "eighteen", "19": "nineteen"
  }
  const decades = { "2": "twenty", "3": "thirty", "4": "forty", "5": "fifty", "6": "sixty", "7": "seventy", "8": "eighty", "9": "ninety"
  }
  
  let string = String(num);
  const first = string[0];
  const middle = string[1];
  const end = string[2];
  let output = "";
//turns inputted integer into string
//accesses first, last and middle indicies
  if (num < 20) {
    output = ones[num];
  }
//checks for numbers under 20
  else if (num <= 99) {
//checks for 2 digit numbers over 20
    if (middle === "0") {
    output = decades[first];
//checks if ends in zero e.g. 30, 40, 50
    }
    else if (middle !== "0") {
    output = decades[first] + " " + ones[middle];
//all other numbers
    }
  }
  
  else if (num > 99) {
//checks three digit numbers
//middle checks the second number of input
    if (middle === "0" && end === "0") {
      output = ones[first] + " hundred";
//checks for numbers like 100, 200, 300
    }
    else if (middle === "0") {
      output = ones[first] + " hundred " + ones[end];
//checks for numbers with middle 0. e.g. 103, 502
    }
    else if (end === "0" && middle !== "1") {
      output = ones[first] + " hundred " + decades[middle];
//checks for numbers with no ones, but not ending in 10. e.g. 150, 330, 650
    }
    else if (middle === "1") {
      output = ones[first] +" hundred " + ones[string.slice(1,3)];
//checks for numbers ending in "teens"
    }
    else if (middle !== "1") {
      output = ones[first] + " hundred " + decades[middle] + " " + ones[end];
//rest of three digit numbers
    }
  }
  return output;
  }

// Exercise 7
const missingComment = file =>{
//variables to access fs, read and split the
//content of the file into lines
  const fs = require("fs");
  const readFile = fs.readFileSync(file, "utf8");
  let lines = readFile.split("\n");
  
  let linenumber = 0;
  let names = [];
//variables for a counter and an array to store
//the function names
  while (linenumber < lines.length) {
      if (lines[linenumber].startsWith("//")) {
        linenumber += 1;
      }
//checking for a comment, if so you skip past the next line
      else if (lines[linenumber].startsWith("function")) {
          let noFunc = lines[linenumber].slice(9);
          let noVar = noFunc.split("(");
          let name = noVar[0];
          names.push(name);
      }
//noDef slices from index 4 to get rid of "function"
//then its split at the "(" with [0] being the
//function name, so its pushed to the array
  linenumber += 1;
  }
  return names;
//continuing the loop
  }

// Exercise 8
function consistentLineLength(file, maxLen){
//variables to require fs, read, replace any new lines with spaces
//then spliting at spaces so we have the separate words
  const fs = require("fs");
  const data = fs.readFileSync(file, "utf8");
  let fileLine = data.replace(/\n/g, " ");
  let word = fileLine.split(" ");

  let maxLines = [];
  let line = "";
//maxLines is an array to store the output
//each line will be pushed to maxLines
  for (let i = 0; i < word.length; i++) {
//looping through each word in "word"
    if (word[i].length + line.length +1 <= maxLen) {
      line = line + " " + word[i]
    }
    else {
      maxLines.push(line.trim())
      line = word[i]
    }
//the length of the word and length of "line" + 1 to simulate
//the space that will be added. if not over maxLen
//will add more words to line until maxLen reached.
  }
  maxLines.push(line.trim());
//push last line since its not hit maxLen
  return maxLines;
}

// Exercise 9
function knight(start, end, moves) {
    return undefined
}

// Exercise 10
function warOfSpecies(environment) {
    return undefined
}

module.exports = {
    reduceFraction: reduceFraction,
    isMagicDate: isMagicDate,
    sublist: sublist,
    pigLatin: pigLatin,
    morseCode: morseCode,
    int2Text: int2Text,
    missingComment: missingComment,
    consistentLineLength: consistentLineLength,
    knight: knight,
    warOfSpecies: warOfSpecies
}