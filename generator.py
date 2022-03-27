import random 

#import the "random" library/api

accounttype = "@gmail.com"

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

lower = "abcdefghiklmnopqrstuvwxyz"

string = lower + upper 

length = 16
passwordlength = 12

account = "".join(random.sample(string, length))
password = "".join(random.sample(string, passwordlength))

print("account: " + account + accounttype)
print("password" + password)

#EVERYTHING ABOVE IS AN ACCOUNT GENERATOR
#ACCOUNTS MIGHT ALREADY EXIST (lmao)


