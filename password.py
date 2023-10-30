#PASSWORD GENERATOR

import random

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digits=['0','1','2','3','4','5','6','7','8','9']
splchar=['!','@','#','$','%','^','&','*','(',')']

n=int(input("Enter the length of the password required : "))
l=n//3
d=n//3
s=n-d-l
password=[]
s1=""

for i in range(l):
    password.append(random.choice(letters))
for i in range(d):
    password.append(random.choice(digits))
for i in range(s):
    password.append(random.choice(splchar))
random.shuffle(password)
for i in range(len(password)):
    s1+=password[i]

print("Password generated : "+s1)

