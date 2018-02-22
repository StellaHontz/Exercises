import random
x = input("Please type the name of the file: \n")
f = open ( x , "r")
read = f.read()
spl= read.split ()
read = read.replace(',' ,'')
read = read.replace('.' ,'')
read = read.replace('!' ,'')
read = read.replace('?' ,'')
length = int(len(spl))
sentence = ""
flist = [[]]
k=0
counter = 0
metr = 3

#Split uppercase from lowercase
for i in range (0, length, length) :
	a = [words for words in spl if not words.islower() and not words.isupper()]
	b= [words2 for words2 in spl if words2.isupper()]
	spl2 = [ n for n in spl if n  not in a ]
	newli = [ d for d in spl2 if d  not in b ]
	
	
#split in lists of trios
flist= [ [newli[j] , newli[j+1] , newli[j +2]] for j in range (0 , length -30, 3)]	
#select random trio
trio = random.randint(0 ,len(flist)-1)

#make a text of almost 200 words
if len(flist[len(flist)-1])< 3:
    del flist[len(flist)-1]

for i in flist[trio]:
        sentence = sentence + i + " "

#make a text with 200 words
while metr <= 200:
    for i in range(len(flist)-1):    
        if flist[trio][1] == flist[i][0] and flist[trio][2] == flist[i][1]:
            sentence = sentence + flist[i][2] + " " 
            metr = metr + 1
        else:
            trio = random.randint(0,len(flist)-1)
            for i in flist[trio]:
                sentence = sentence + i + " "
                metr = metr + 3

print(sentence)
		