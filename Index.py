#Imports
import numpy

# NFA -> DFA Converter
# Main file with code
# By Malory Morey

# Openingthe file in read mode 
file = open("Test.txt", "r") 
data = file.read() 

# Print a newline to make output look nice and label what is being printed
print('\n')
print('The formal description of your NFA is: ')


#  ---------------Creating elements of NFA formal description---------------
# When theres a newline ('\n'), make new element. 
nfaDesc = data.split("\n")

# Split formal description into their own arrays
nfaStates = numpy.array(i, nfaDesc[0].split(' '))
nfaAlpha = numpy.array(1, nfaDesc[1].split(' '))
nfaStart = numpy.array(nfaDesc[3].split(' '))
nfaEnd = numpy.array(nfaDesc[4].split(' '))

# Printing elements into list
print(nfaDesc) 
file.close() 

# Test case Demo
if nfaDesc[0] == 'q0 q1 q2':
    print('Its in proper form')
# ---------------Converting elements of DFA formal description---------------
#Loop through states to make nfa states
for i in nfaStates:
    #dfaStates[i] = nfaStates[i]
    #if i == nfaStates.length():
    dfaStates[i] = nfaStates[i] + nfaStates[i+1]
        



# ---------------Printing elements of DFA formal description---------------
# Print a newline to make output look nice and label what is being printed
print('\n')
print('The formal description of your DFA is: ')

# Copy over changed elements
print(dfaStates)
print(dfaDesc) 

# Print a newline to make output look nice
print('\n')
