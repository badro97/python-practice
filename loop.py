
numbers = [1, 2, 3, 4, 5, 6]

new_numbers = []

for num in numbers:
    new_numbers.append(num*2) 
    
print(new_numbers)

####################################  
   
    
for i in range(2, 10):
    for j in range(1,10):
        print(i ,'X', j, '=', i*j)
    print('\n')
    
#################################### 
  

munzi = int(input('미세먼지 농도를 입력하세요.: '))

if munzi > 150:
    print("미세먼지 농도 매우 나쁨")
elif 80 < munzi <=150:
    print("미세먼지 농도 나쁨")
elif 30 < munzi <=80:
    print("미세먼지 농도 보통")
else:
    print("미세먼지 농도 좋음")
    
#################################### 

evenlist = []
oddlist = []

for num in range(1,11):
    if num%2 ==1:
        oddlist.append(num)
    else:
        evenlist.append(num)
        
print(oddlist)
print(evenlist)