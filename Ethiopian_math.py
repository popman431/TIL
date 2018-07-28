# Thinking algorithm 1
num1 = 13
num2 = 12
_sum =0
for i in range(1,2+1):
    if num1 % 2 == 1:
        _sum = _sum + num2
        num1 = int(num1 /2) 
        num2 = num2 *2
    elif num1 % 2 == 0:
        _sum = _sum
        num1 = int(num1 /2) 
        num2 = num2 *2
    elif num1 ==1:
        _sum = num2 + _sum

print(_sum)
print(num1)
print(num2)
