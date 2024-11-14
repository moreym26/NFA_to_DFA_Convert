# NFA -> DFA Converter
# Main file with code
# By Malory Morey

# opening the file in read mode 
file = open("Test.txt", "r") 
# reading the file 
data = file.read() 

# Print a newline to make output look nice and label what is being printed
print('\n')
print('The formal description of your NFA is: ')

# When theres a newline ('\n'), make new element. 
nfaDesc = data.split("\n") 

# Printing elements into list
print(nfaDesc) 
file.close() 

# Test case Demo
if nfaDesc[0] == 'q0 q1 q2':
    print('Its in proper form')

# Print a newline to make output look nice
print('\n')

# Label what is being printed
print('The formal description of your DFA is: ')
# Dummied up for demo
dfaDesc = nfaDesc
print(dfaDesc) 

# Print a newline to make output look nice
print('\n')
