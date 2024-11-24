import json
from collections import OrderedDict
import numpy as np
# NFA -> DFA Converter
# Main file with code
# By Malory Morey

# Opening and loading the json input file
with open('input.json') as file:
    input = json.load(file)

# Print a newline to make output look nice and label what is being printed
print('\n')
print('The formal description of your NFA is: ')
#  ---------------Creating elements of DFA formal description---------------
dfaStates = 2 ** input["states"]
dfaAlpha = input["alpha"]
dfaStart = input["start"]
dfaTransFunc = []
dfaEnd = []

nfaTrans = {}
dfaTrans = {}

#  ---------------Set up NFA & DFA transitions---------------
for transition in input["transFunc"]:
    nfaTrans[(transition[0], transition[1])] = transition[2]

Q = []
Q.append((dfaStart,))
# Printing elements into list
print() 


# Test case Demo


# ---------------Converting elements of DFA formal description---------------
#Loop through states to make nfa states



# ---------------Printing elements of DFA formal description in a new json file---------------
dfa = OrderedDict()
dfa["states"] = dfaStates
dfa["alpha"] = dfaAlpha
dfa["transFunc"] = dfaTransFunc
dfa["start"] = dfaStart
dfa["end"] = dfaEnd

output = open('output.json', 'w')
json.dump(dfa, output, separators = (',\t', ':'))
# Print a newline to make output look nice
print('\n')
