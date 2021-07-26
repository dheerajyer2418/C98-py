f = open("test.txt")
fileLines = f.readlines()
for line in fileLines: 
    print(line)
introString = "My name is Dheeraj. I am 15 yrs old."
words = introString.split('.')
print(words)

def Greet(name): 
    print("Hello " + name + ". How are You?")

Greet("Dheeraj")