#sort


num=[5,3,6,7,4,9,8,1,36,78,12,2]
count=0
mini=0
temp=0
count1=0

while count<len(num):
    if count==0:
        mini=num[count]
        count+=1
    elif count>=1:
        if num[count]<mini:
            mini=num[count]
            print"1",num
            temp=num[count1]
            print"2",num
            num[count1]=mini
            print"3",num
            num[count]=temp
            print"4",num
            
        count+=1



        

print mini
print num

