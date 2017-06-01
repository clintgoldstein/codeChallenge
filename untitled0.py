
print (" input numbers")

# get input
buffer =input()

#create a list of string length 8
codes = []
while buffer:
    codes.append(buffer[:8])
    buffer = buffer[8:]
 
#initilize count
total=0

for code in codes:
    #convert to dec and store
    num=int(code, 2)
    
    #convert to list count 1s
    list_form=list(code)
    ones=0
    for bit in range(0, 8):
        if list_form[bit]=='1':
            ones+=1
    
    #add or subtract
    if ones % 2 == 0:
        total+=num
    else:
        total-=num
        
print(total)