#sort


num=[4,3,6,7,4,9,8,10,36,78,12,2]
sort=[]
count=0
mini=0
count1=0

while count<len(num):
    if count==0:
        mini=num[count]
        count+=1
    elif count>=1:
        if num[count]<mini:
            mini=num[count]
            count+=1
        sort.append(mini)
        count1+=1

        

print mini
print sort

