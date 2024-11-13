# NFA -> DFA Converter
# Main file with code
# By Malory Morey

# opening the file in read mode 
file = open("Test.txt", "r") 
# reading the file 
data = file.read() 

# Label what is being printed
print('The formal description your input is: ')

# When theres a newline ('\n'), make new element. 
formalDesc = data.split("\n") 

# Printing elements into list
print(formalDesc) 
file.close() 

# Test case Demo
if formalDesc[0] == 'q0 q1 q2':
    print('Its in proper form')

