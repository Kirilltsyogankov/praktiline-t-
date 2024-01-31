

#for j in range(0,105,1):

#for i in range (0,105,1):
#    print(i,end=" ")
#print()


n = 3
tree = [
"   /V\    ",
"  / V \   ",
" / V V \  ",
"/VV V VV\  "
]

for _ in range (n):
    for line in tree:
        print(line, end=' ')
    print()



R = 5
result = 1

for i in range (1, R + 1, 2):
    result *= i

print(result)


import random

N = 10
random_numbers = [random.randint(-10, 10) for _ in range(N)]
positive_count = sum(1 for num in random_numbers if num > 0)
print("Количество положительных чисел:", positive_count)




number = 34560
even_count, odd_count = 0, 0

for digit in str(number):
    if int(digit) % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Четные цифры:", even_count)
print("Нечетные цифры:", odd_count)




A, B = 1, 5
result = sum(range(A, B + 1))
print("Сумма ряда чисел от A до B:", result)