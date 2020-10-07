##Leira Salene 1785752

password1 = input()
password2 = ''

for x in password1:
    if (x=='i'):
        password2+="!"
    elif (x=='a'):
        password2 += "@"
    elif (x == 'm'):
        password2 += "M"
    elif (x == 'B'):
        password2 += "8"
    elif (x == 'o'):
        password2 += "."
    else:
        password2 += x
password2 += "q*s"
print (password2)