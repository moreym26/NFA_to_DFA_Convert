# NFA -> DFA Converter
# Main file with code
# By Malory Morey

# opening the file in read mode 
file = open("Test.txt", "r") 
  
# reading the file 
data = file.read() 
  
# replacing end splitting the text  
# when newline ('\n') is seen. 
formalDesc = data.split("\n") 
#Printing elements into list
print(formalDesc) 
file.close() 

if formalDesc[0] == 'q0 q1 q2':
    print('Its in proper form')

