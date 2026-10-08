# Analisador de Personagens
# Você está criando um sistema para analisar 8 personagens de RPG.
# Para cada personagem, peça:
# Nome
# Idade
# Força
# Vida (HP)
# No final, mostre: 
# 🏆 Personagem com maior força
# 💪 Maior valor de força
# ❤️ Personagem com maior vida
# ❤️ Maior HP
# 📊 Soma de todas as forças
# 📊 Média das forças
# 👴 Quantidade de personagens com 18 anos ou mais
# 👶 Quantidade de personagens com menos de 18 anos

mais_fort = ''
maior_forca = 0
mais_vida = ''
hp = 0
som_for = 0
velho = 0
novo = 0

for p in range(1, 9):
  per = input(f'Digite o nome do {p}º personagem: ')
  id = int(input(f'Digite a idade do {p}º personagem: '))
  forca = int(input(f'Digite a força do {p}º personagem: '))
  vida = int(input(f'Digite o HP do {p}º personagem: '))

  som_for += forca

  if p == 1:
    mais_fort = per
    mais_vida = per
    maior_forca = forca
    hp = vida

  else:
    if forca > maior_forca:
      maior_forca = forca
      mais_fort = per

    if vida > hp:
      hp = vida
      mais_vida = per

  if id >= 18:
      velho += 1

  else:
    novo += 1

media = som_for / 8

print('===== RESULTADO =====')
print(f'O {mais_fort} é o personagem mais forte da mesa!')
print(f'Sua força: {maior_forca}')
print(f'O {mais_vida} é o personagem com mais vida da mesa!')
print(f'Seu hp: {hp}')
print(f'Soma das forças: {som_for}')
print(f'Média das forças: {media:.2f}')
print(f'Personagens com 18 anos ou mais: {velho}')
print(f'Personagens com menos de 18 anos: {novo}')
