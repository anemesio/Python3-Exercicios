num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))
num4 = int(input('Digite o último número: '))
nums = (num1, num2, num3, num4)
print(f'Você digitou os números: {nums}')
if 9 not in nums:
    print('O número 9 não apareceu nenhuma vez.')
else:
    print(f'O valor 9 apareceu {nums.count(9)} vezes.')
if 3 not in nums:
    print('O número 3 não apareceu em nenhuma posição.')
else:
    print(f'O número 3 apareceu na {nums.index(3) + 1}ª posição.')
print('Os valores pares digitados foram: ', end='')
for c in sorted(nums):
    if c % 2 == 0:
        print(c, end=' ')







