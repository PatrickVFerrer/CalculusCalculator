'''
function to remove whitespace
string to variable method? [eval("") function]
function to find derivative

variable = x  

rules for derivatives:

constant rule = 0
power rule [dy/dx = 7x*3x = 21x^2 = 42x]
chain rule
product rule [21xy -> 21(xy) -> 21(y + (dy/dx * x))]
quotient rule

* if we have time we can print step by step

Bonus:  inverse, tangent line, 
        implicit, table of values, 
        integrals
'''
# def removeSpacing(string):
  
#   string1 = ""
#   string2 = ""
  
#   while string.count(" ") > 0:
#     loc = string.index(" ")
#     string1 = string[0:loc]
#     string2 = string[loc+1:len(string)]
#     string = string1 + string2
#     # print(f"""{string1}, {string2}, {string}""")
#   return string

def isInt(var): # Check if value can be stored as integer
  try:
    var = int(var)
  except ValueError:
    return False    
  else:
    return True

def arePresent(string):
  isPlus = string.count("+") > 0
  isMinus = string.count("-") > 0
  isAster = string.count("*") > 0
  isSlash = string.count("/") > 0
  return isPlus or isMinus or isAster or isSlash

def findLoc(string):
  locs = []
  for char in string:    
    if (
      char == "+" or
      char == "-" or
      char == "/" or
      char == "*"
    ):
      locs.append(string.index(char))
  
  if locs.copy() == [].copy():
    return -1

  return locs[0]

def derivative(string):
  terms = []
  operators = []
  loc = -1

  string = string.replace(" ", "")
  while(arePresent(string)):
    loc = findLoc(string)
    terms.append(string[0:loc])
    operators.append(string[loc])
    string = string[loc+1:len(string)]
  terms.append(string)
  # print(terms)
  # print(operators)
  
  result = ""
  for term in terms:
    
    i = terms.index(term)
    if i == len(operators):
      op = ""
    else:
      op = operators[i]
    
    if term.count("^") > 0:
      result += power_rule(term)
    if term.isdigit():
      result += derv_num(term)

    result += f' {op} '
 
  print(result)

def derv_num(string):
  # returns 0 if input is a constant
  if string.isdigit():
    return 0
  else:
    raise ValueError

def power_rule(inp): # inp = term passed to method
  # Only called if carat present; no inp.count("^") needed
  loc = inp.index("^")        # Gets index of caret in term
  power = int(inp[loc + 1:])  # Gets exponent (all numbers after the caret)
  answer = ""
  coef = 0
  
  # Gets coefficient of x from term
  # If no coeffcient, set to 1
  if inp[:loc-1] == "":
    coef = 1
  else:
    coef = int(inp[:loc-1])

  # Concatenates exponent * coefficient
  answer += str(power * coef) + "x"

  if power - 1 == 1:
    return answer

  if (power - 1 != 1) or (power - 1 != 0):
      answer += "^" + str(power-1)
  if power - 1 == 0:
      return str(coef)
  # if (result_expo[0] - 1) > 1:
  #   answer.append(result_expo[0] - 1)
  
  # print(answer)  
  return answer
  # return ("".join(answer_string))
    
# def derv_coefficient(string):
#   pass
# def chain_rule(string):
#   pass
# def product_rule(string):
#   pass

derivative(input("Input: "))