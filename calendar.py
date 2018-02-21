from datetime import date

x = int( input("Give number of month (between 1 to 12): "))
y = int( input("Give year: "))
month = date (y , x , 1).strftime('%B')
start = date(y , x , 1).weekday()
days= [ 'Mo' , 'Tu' ,'We ' , 'Th' ,  'Fr',  'Sa' ,'Su'] 


print ('{0} {1}'.format(month , y).center(20 , ' '))
print(''.join(['{0:<3}'.format(k) for k in days]))
print ('{0:<3}'.format('')*start , end="")

for l in range (31):
        if x==2 :
                if ( y%4== 0 and y%100 != 0) or y%400 == 0 :
                        if l+ 1 == 30:
                                break
                elif l+1 == 29:
                        break
        print ('{0:<3}'.format(l+1) ,end="")
        start += 1 
        if start == 7:
                print()
                start = 0
                
