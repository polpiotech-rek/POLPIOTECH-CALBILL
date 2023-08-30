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
    for i in range(quantityCustomer):
        listCustomer.append(str(input('Nazwa zamawiającego: ')))
        listMoney.append(float(input('Kwota na zakupy [PLN]: ')))
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
    
else:
    cprint('Czy chcesz uruchomić ponownie program? (T/N)', 'white', 'on_green')
    answerRep = str(input('WYBÓR: '))
    if answerRep == 't':
        system('cls')
        cprint('TRWA PONOWNE URUCHOMIENIE PROGRAMU...', 'white', 'on_green')
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