import json
from collections import OrderedDict
# NFA -> DFA Converter
# Main file Aith code
# By Malory Morey

# Opening and loading the json input file
with open('input.json') as file:
    input = json.load(file)

#  ---------------Creating elements of DFA formal description---------------
dfaStates = 2 ** input["states"] # Number of states is 2^(number of NFA states)
dfaAlpha = input["alpha"]        # Alphabet
dfaStart = input["start"]        # Start state
dfaTransFunc = []                # Transition function
dfaEnd = []                      # End/accept state

# make empty transitions for both NFA and DFA to manipulate beloA
nfaTrans = {}
dfaTrans = {}

#  ------------------Set up NFA & DFA transitions in proper form-----------
for transition in input["transFunc"]:
    nfaTrans[(transition[0], transition[1])] = transition[2]

# Making Q'
Q = []
Q.append((dfaStart,))

# ---------------Converting NFA transitions to DFA transitions---------------
# Go through states in q'
for currState in Q:
    # Go through alphabet for each alphabet symbol in NFA alphabet
    for alphaTrans in dfaAlpha:
        # If the list is only 1 long, then just use NFA transition from the table
        if len(currState) == 1 and (currState[0], alphaTrans) in nfaTrans:
            dfaTrans[(currState, alphaTrans)] = nfaTrans[(currState[0], alphaTrans)]
            #If the transition isn't in q' add it
            if tuple(dfaTrans[(currState, alphaTrans)]) not in Q:
                Q.append(tuple(dfaTrans[(currState, alphaTrans)]))
        # Else if the list is not of length 1 then make new transitions
        else:
            # Make more empty vars to fill with new states
            acceptStates = []
            finalState = []
            
            #Loop through your iteration of q', if add it to state
            for state in currState:
                if (state, alphaTrans) in nfaTrans and nfaTrans[(state, alphaTrans)]:
                    acceptStates.append(nfaTrans[(state, alphaTrans)])
            
            # loop through states and add it if not there
            if acceptStates:
                for x in acceptStates:
                    for val in x:
                        if val not in finalState:
                            finalState.append(val)
                # Add new transitions to final
                dfaTrans[(currState, alphaTrans)] = finalState
                
                # if the accepting states is not in q' then add it
                if tuple(finalState) not in Q:
                    Q.append(tuple(finalState))


#Remake DFA transition function
for key, val in dfaTrans.items():
    list = [[key[0], key[1], val]]
    dfaTransFunc.extend(list)

#Get final accepting states of DFA
for state in Q:
    for last in state:
        dfaEnd.append(state)


# ---------Putting elements of DFA formal description in a list---------
dfa = OrderedDict()
dfa["states"] = dfaStates
dfa["alpha"] = dfaAlpha
dfa["transFunc"] = dfaTransFunc
dfa["start"] = dfaStart
dfa["acceptStates"] = dfaEnd

# ---------Putting elements of DFA formal description in a n json file---------
output = open('output.json', 'w')
json.dump(dfa, output, separators = (',\t', ':'))


# Print a neAline to make output look nice
# Print a success message Aith directions for user
print('\n')
print('NFA => DFA conversion succesful. Please see the output.json file with your new DFA.')