#Askisi 3. Rot13

def rot13(x):
    x1 = ""
    x= input ('Write something to encrypt with rot13 \n')
    
    for i in x:
        y = ord(i)
        if y >= ord('a') and y <= ord('z'):
            if y > ord('m'):
                y -= 13
            else:
                y += 13
        elif y >= ord('A') and y <= ord('Z'):
            if y > ord('M'):
                y -= 13
            else:
                y += 13
        x1 += chr(y)
    return x1
print(rot13("x"))
