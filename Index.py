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
nfaStates = nfaDesc[0].split(' ')
nfaAlpha = nfaDesc[1].split(' ')
nfaStart = nfaDesc[3].split(' ')
nfaEnd = nfaDesc[4].split(' ')

# Printing elements into list
print(nfaDesc) 
file.close() 

# Test case Demo
if nfaDesc[0] == 'q0 q1 q2':
    print('Its in proper form')
# ---------------Printing elements of DFA formal description---------------
# Print a newline to make output look nice and label what is being printed
print('\n')
print('The formal description of your DFA is: ')

# Dummied up for demo
dfaDesc = nfaDesc
print(dfaDesc) 

# Print a newline to make output look nice
print('\n')
