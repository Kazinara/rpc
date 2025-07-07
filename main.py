import random
count = 0
for number in range(10):
    player = int(input('Сделай выбор: 1) камень 2) ножницы 3) бумага : '))
    if player == 1:
        print('Вы выбрали камень')
    elif player == 2:
        print('Вы выбрали ножницы')
    elif player == 3:
        print('Вы выбрали бумагу')
    comp = random.randint(1,3)
    if comp == 1:
        print('Противник выбрал камень')
    elif comp == 2:
        print('Противник выбрал ножницы')
    elif comp == 3:
        print('Противник выбрал бумагу')
    if player == comp:
        print('Ничья!')
    elif player == 1 and comp == 2 or player == 2 and comp == 3 or player == 3 and comp == 1 :
        print('Вы победили!')
        count += 1
    elif comp == 1 and player == 2 or comp == 2 and player == 3 or comp == 3 and player == 1 :
        print('Вы проиграли...')
    print(f'Мои победы: {count}')
    if count == 3:
        break

