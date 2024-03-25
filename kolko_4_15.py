# https://www.eolymp.com/uk/submissions/14555174
n = int(input())
res = 0
for i in range(10 ** (n - 1), 10 ** n):
    if '2' in str(i) or '4' in str(i) or '6' in str(i) or '8' in str(i) or '0' in str(i):
        pass
    else:
        res += 1
print(res)

# https://www.eolymp.com/uk/submissions/14569484
# Халтура. Але дійсно можна помітити що що таких чисел в n-цифровому числі 5**n
n=int(input())
print(5**n)