# Finish Algorithm
num1 = int(input("Type num1 : "))
num2 = int(input("Type num2 : "))
_sum = 0
while True:
    if int(num1 / 2 ==0):
        break
    else:
        if num1 % 2 == 1:
            print(num1)
            print(num2)
            print(_sum)
            print("\n")
            _sum = _sum + num2
            num1 = int(num1 /2) 
            num2 = num2 *2
            
        elif num1 % 2 == 0:
            print(num1)
            print(num2)
            print(_sum)
            print("\n")
            _sum = _sum
            num1 = int(num1 /2) 
            num2 = num2 *2
         
        elif num1 ==1:
            print(num1)
            print(num2)
            print(_sum)
            print("\n")
            _sum = num2 + _sum
print(num1)
print(num2)
print(_sum)
