#import the necessary modules
import string
import random
#input the length of password
length = int (input('Enter the length of password:'))
#Define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
#combine the data
all = lower + upper + num + symbols
#use random
temp = random. sample(all, length)
#create the password
password = "".join(temp)
#print the password
print("Password: "+password)
