# Kalkulator rozliczenia paragonów fiskalnych

from os import system
from time import sleep
from sys import exit
from termcolor import cprint, colored


cprint('        -- KALKULATOR PARAGONÓW --        ', 'white', 'on_green')
print()

try:
    quantityCustomer = int(input('Podaj ilość klientów: '))
    listCustomer = []
    listMoney = []
    for i in range(quantityCustomer):
        listCustomer.append(str(input('Nazwa klienta: ')))
        listMoney.append(float(input('Kwota na zakupy [PLN]: ')))

except(ValueError):
    system('cls')
    print('BŁĄD WPROWADZONEJ WARTOŚCI!')
    print()
    print('TRWA PONOWNE URUCHOMIENIE PROGRAMU...')
    print()
    for i in range(101):
        print("\rLoading {}%".format(i), end='')
        sleep(0.08)
    system('cls')
    system('python calbill.py')
except:
    system('cls')
    print('NIEZIDENTYFIKOWANY BŁĄD!')
    print()
    print('TRWA PONOWNE URUCHOMIENIE PROGRAMU...')
    print()
    for i in range(101):
        print("\rLOADING {}%".format(i), end='')
        sleep(0.03)
    system('cls')
    system('python calbill.py')


print('Czy podsumować łączną ilość pobranej gotówki? (T/N)')
answerSum = str(input('WYBÓR: '))
if answerSum == 't':
    sumMoney = sum(listMoney)
    allCash = print('Łączna kwota na zakupy:', sumMoney, 'zł')
elif answerSum == 'n' or answerSum == 'N':
    system('cls')
    print('Czy chcesz uruchomić ponownie program? (T/N)')
    answerRep = str(input('WYBÓR: '))
    if answerRep == 't':
        print('TRWA PONOWNE URUCHOMIENIE PROGRAMU...')
        print()
        for i in range(101):
            print("\rLOADING {}%".format(i), end='')
            sleep(0.03)
        system('cls')
        system('python calbill.py')
    else:
        print('ZAMYKANIE PROGRAMU...')
        print()
        for i in range(101):
            print("\rLOADING {}%".format(i), end='')
            sleep(0.03)
        exit