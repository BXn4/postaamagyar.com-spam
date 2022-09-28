import requests
from random import *
import random


url = 'https://postaamagyar.com/send.php'
print(requests.get(url))

#Vezetéknevek
vezeteknevek = ["Nagy", "Kiss", "Kovács", "Horváth", "Varga", "Tóth", "Szabó", "Farkas",
                "Szűcs", "Balogh", "Polgár", "Molnár", "Lakatos", "Mészáros", "Orbán",
                "Varga", "Csonka", "Pataki", "Török", "Fehér", "Balázs", "Juhász",
                "Simon", "Oláh", "Németh", "Orsós", "Lukács", "Kocsis",
                "Pintér", "Kis", "Balogh", "Nemes", "Barna", "Deák", "Vass"]

#Keresztnevek
keresztnevek = ["Bence", "Károly", "Béla", "Ernő", "Pál", "Zsolt", "Nándor", "Gyula",
                "János", "Ferenc", "Béla", "Pista", "Gábor", "Tímea", "Anna", "Vivien",
                "Natasa", "Tamara", "Ábel", "Bende", "Bonifác", "Levente", "Máté", "Noel",
                "Zalán", "Botond", "Dávid", "Maja", "Sára", "Mira", "Dominika", "Laura",
                "Nóra", "Milán", "Nimród", "Zente", "Gergő", "Márton", "Kornél", "Liza"]

while(True):
    
    #############/----------------------------------------------------------------------\#############
    kartyaszamRND = randint(1000000000000000, 9999999999999999)
    karytaszamSTR = str(kartyaszamRND)
    kartyaszam = [karytaszamSTR[index : index + 4] for index in range(0, len(karytaszamSTR), 4)]
    lejarho = randint(1, 9)
    lejarev = randint(23, 29)
    cvc = randint(100, 999)
    sms = randint(100000, 999999)
    
    ertekek = {
        'nom': random.choice(vezeteknevek),
        'prenom': random.choice(keresztnevek),
        'cc': (f'{kartyaszam[0]} {kartyaszam[1]} {kartyaszam[2]} {kartyaszam[3]}'),
        'exp': (f'0{lejarho}/{lejarev}'),
        'cvc': (f'{cvc}'),
        'sms': (f'{sms}'),
               }
    #############/----------------------------------------------------------------------\#############
    
    valasz = requests.post(url, data=ertekek)
    if valasz.ok:
        print(ertekek)
    else:
        print("nemjo :(")
