#https://www.eolymp.com/uk/submissions/14194004
hrn, kop, number = [int(d) for d in input().split()]
price = (hrn + (kop / 100)) * number
print(f'{int((price * 10) // 10)} {round(((price * 10) % 10) * 10)}')