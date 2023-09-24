# Kalkulator rozliczenia paragonów fiskalnych

from os import system
from time import gmtime, strftime, sleep
from sys import exit
from termcolor import cprint, colored

system('cls')
cprint('                              POLPIOTECH®                             ', 'red', 'on_white')
cprint('                      -- KALKULATOR PARAGONÓW --                      ', 'white', 'on_red')
print()
date_app_reckoning = strftime("%a, %d %b %Y", gmtime())
time_app_reckoning = strftime("%r")
print(date_app_reckoning, time_app_reckoning)
print()
try:
    nameStore = str(input('Wpisz nazwę sklepu: '))
    quantityCustomer = int(input('Wpisz ilość zamówień: '))
    print()
    listCustomer = []
    listMoney = []
    amountShopping = []
    for i in range(quantityCustomer):
        listCustomer.append(str(input('Nazwa zamawiającego: ')))
        listMoney.append(float(input('Kwota na zakupy [PLN]: ')))
        amountShopping.append(float(input('Kwota z paragonie [PLN]: ')))
        print()

except(ValueError):
    system('cls')
    cprint('BŁĄD WPROWADZONEJ WARTOŚCI!', 'white', 'on_red')
    print()
    print('TRWA PONOWNE URUCHOMIENIE PROGRAMU...')
    for i in range(101):
        print("\rLOADING {}%".format(i), end='')
        sleep(0.01)
    system('cls')
    system('python calbill.py')
except:
    system('cls')
    cprint('NIEZIDENTYFIKOWANY BŁĄD!', 'white', 'on_red')
    print()
    print('TRWA PONOWNE URUCHOMIENIE PROGRAMU...')
    for i in range(101):
        print("\rLOADING {}%".format(i), end='')
        sleep(0.01)
    system('cls')
    system('python calbill.py')

print()
cprint('Czy podsumować łączną ilość pobranej gotówki? (T/N)', 'white', 'on_green')
answerSum = str(input('WYBÓR: '))
print()
if answerSum == 't':
    sumMoney = sum(listMoney)
    allCash = print('Łączna kwota na zakupy:', sumMoney, 'zł')
    sumBill = int(input('Wpisz ilość paragonów: '))
    sumCustomers = quantityCustomer
    print('Ilość zamawiających:', quantityCustomer)
    sumOrder = sumBill - quantityCustomer  
    print('Różnica pomiędzy dokumentami fiskalnymi a zamówieniami:', sumOrder, 'szt.')
    sumProc = (sumBill / sumCustomers) 
    print('Różnica wyrażona w procentach: ', colored(f" {sumProc:.2%} ", 'white', 'on_green'))
    print()

    if sumBill > sumCustomers:
        cprint('[ WIĘCEJ ] - ilość dokumentów fiskalnych jest większa od ilości zamówień! --> TO SIĘ NALATAŁEŚ! :) ', 'white', 'on_blue')

    elif sumBill == sumCustomers:
        cprint('[ POKRYCIE ] - ilość dokumentów fiskalnych jest równa ilości zamówień! --> PORZĄDNA FIRMA - WSZYSTKO ZGADZA SIĘ ;) ', 'white', 'on_yellow')

    else:
        cprint('[ MNIEJ ] - ilość dokumentów fiskalnych jest mniejsza od ilości zamówień! --> PRAWDOPODOBNIE O CZYMŚ ZAPOMNIAŁEŚ :( ', 'white', 'on_red')
    
    print()
    #print()
    #cprint('ROZLICZENIE:', 'white', 'on_red')
    #print()
    for x in range(len(listCustomer)):
        sumShopping = amountShopping[x] / listMoney[x]
        result = listMoney[x] - amountShopping[x]
        print(f'ZAMAWIAJĄCY: {listCustomer[x]}', end =" ")
        print(f'KWOTA NA ZAKUPY: {listMoney[x]} zł -', end =" ")
        print(f'KWOTA Z PARAGONU: {amountShopping[x]} zł = ', end ="")
        print(f'KWOTA DO ZWROTU: {round(result,2)} zł \n', end ="")
        print(colored(f' WYDANO [%]: {sumShopping:.2%} ', 'white', 'on_green'))
        print()
    cprint('ROZLICZONO WSZYSTKIE ZAMÓWIENIA...', 'white', 'on_red')
    print()
    print()
    cprint('Czy chcesz zakończyć pracę programu? (T/N)', 'white', 'on_green')
    answerClose = str(input('WYBÓR: '))
    if answerClose == 't':
        system('cls')
        cprint('TRWA ZAMYKANIE PROGRAMU...', 'white', 'on_red')
        for i in range(101):
            print("\rLOADING {}%".format(i), end='')
            sleep(0.01)
        system('cls')
        exit
    else:
        system('cls')
        cprint('TRWA PONOWNE URUCHOMIENIE PROGRAMU...', 'white', 'on_red')
        for i in range(101):
            print("\rLOADING {}%".format(i), end='')
            sleep(0.01)
        system('cls')
        system('python calbill.py')

else:
    cprint('Czy chcesz uruchomić ponownie program? (T/N)', 'white', 'on_green')
    answerRep = str(input('WYBÓR: '))
    if answerRep == 't':
        system('cls')
        cprint('TRWA PONOWNE URUCHOMIENIE PROGRAMU...', 'white', 'on_red')
        for i in range(101):
            print("\rLOADING {}%".format(i), end='')
            sleep(0.01)
        system('cls')
        system('python calbill.py')
    else:
        system('cls')
        cprint('ZAMYKANIE PROGRAMU...', 'white', 'on_red')
        for i in range(101):
            print("\rLOADING {}%".format(i), end='')
            sleep(0.01)
        exit