import json
from collections import OrderedDict
import numpy as np
# NFA -> DFA Converter
# Main file with code
# By Malory Morey

# Opening and loading the json input file
with open('input.json') as file:
    input = json.load(file)

#  ---------------Creating elements of DFA formal description---------------
dfaStates = 2 ** input["states"]
dfaAlpha = input["alpha"]
dfaStart = input["start"]
dfaTransFunc = []
dfaEnd = []

# make empty transitions for each to manipulate
nfaTrans = {}
dfaTrans = {}

#  ------------------Set up NFA & DFA transitions------------------
for transition in input["transFunc"]:
    nfaTrans[(transition[0], transition[1])] = transition[2]

# Making Q'
Q = []
Q.append((dfaStart,))

# ---------------Converting NFA transitions to DFA transitions---------------
for inState in Q:
    for symbol in dfaAlpha:
        if len(inState) == 1 and (inState[0], symbol) in nfaTrans:
            dfaTrans[(inState, symbol)] = nfaTrans[(inState[0], symbol)]
            if tuple(dfaTrans[(inState, symbol)]) not in Q:
                Q.append(tuple(dfaTrans[(inState, symbol)]))
        
        else:
            end = []
            lastEnd = []
            
            for state in inState:
                if (state, symbol) in nfaTrans and nfaTrans[(state, symbol)]:
                    end.append(nfaTrans[(state, symbol)])
            
            if end:
                for x in end:
                    for val in x:
                        if val not in lastEnd:
                            lastEnd.append(val)
                
                dfaTrans[(inState, symbol)] = lastEnd
                
                if tuple(lastEnd) not in Q:
                    Q.append(tuple(lastEnd))


#Remake transition function
for key, val in dfaTrans.items():
    list = [[key[0], key[1], val]]
    dfaTransFunc.extend(list)

#Get final accepting states of DFA
for state in Q:
    for last in state:
        dfaEnd.append(state)


# ---------Putting elements of DFA formal description in a dictionary---------
dfa = OrderedDict()
dfa["states"] = dfaStates
dfa["alpha"] = dfaAlpha
dfa["transFunc"] = dfaTransFunc
dfa["start"] = dfaStart
dfa["end"] = dfaEnd

# ---------Putting elements of DFA formal description in a new json file---------

output = open('output.json', 'w')
json.dump(dfa, output, separators = (',\t', ':'))


# Print a newline to make output look nice
# Print a success message with directions for user
print('\n')
print('NFA => DFA conversion succesful. Please see the output.json file with your new DFA.')