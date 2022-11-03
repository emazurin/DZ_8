import os


def input_money(text):
    return (input(text))


def p_hist(hist):
    for j in hist:
        print(j[0], '  ', j[1])
    pass


def get_money():
    if not os.path.exists('account.txt'):
        f = open('account.txt', 'w')
        f.write('0.00\n')
        f.close()

    with open('account.txt', 'r') as f:
        money = float(f.read())

    return (money)


def add_money(money):
    sum = money + get_money()
    with open('account.txt', 'w') as f:
        f.write(str(sum))


def pay_money(money):
    sum = get_money() - money
    with open('account.txt', 'w') as f:
        f.write(str(sum))


def hist_append(data):
    with open('hist.txt', 'a') as f:
        f.writelines(data)


def get_hist():
    with open('hist.txt', 'r') as f:
        # 2. Читам все строки в цикле
        for line in f:
            # line - это каждая строка
            line = line.replace('\n', '')
            print(line)


def bank():
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        ch = input('Выберите пункт меню: ')
        if ch == '1':
            sum = float(input_money('Введите сумму пополнения: '))
            add_money(sum)
            print('На счете', get_money())
            pass
        elif ch == '2':
            deb = float(input_money('Введите сумму покупки: '))
            if deb > get_money():
                print('Сумма покупки больше доступного остатка')
            else:
                s = input_money('Введите название покупки: ')
                pay_money(deb)
                hist_append(['Покупка: ' + str(s) + '  ', 'Сумма покупки: ' + str(deb) + '\n'])
            pass
        elif ch == '3':
            get_hist()
            pass
        elif ch == '4':
            ch = '0'
            return
        else:
            print('Неверный пункт меню')
