num = int(input())

primeiro = num // 1000
segundo = (num - primeiro * 1000) // 100
terceiro = (num - primeiro * 1000 - segundo * 100) // 10
quarto = (num - primeiro * 1000 - segundo * 100 - terceiro * 10)

if (primeiro == 9):
  primeiro = 0
else:
  primeiro += 1

if (segundo == 9):
  segundo = 0
else:
  segundo += 1

if (terceiro == 9):
  terceiro = 0
else:
  terceiro += 1

if (quarto == 9):
  quarto = 0
else:
  quarto += 1

print('{}{}{}{}'.format(primeiro, segundo, terceiro, quarto))