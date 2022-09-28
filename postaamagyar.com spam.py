import requests
from random import *
import random


url = 'https://postaamagyar.com/send.php'
#urlx = requests.get(url)
vezeteknevek = ["Nagy", "Kiss", "Kovács", "Horváth", "Varga", "Tóth", "Szabó", "Farkas"]
keresztnevek = ["Bence", "Károly", "Béla", "Ernő", "Pál", "Zsolt", "Nándor", "Gyula"]
while(True):
    kartyaszam0 = randint(1000, 9999)
    kartyaszam1 = randint(1000, 9999)
    kartyaszam2 = randint(1000, 9999)
    kartyaszam3 = randint(1000, 9999)
    lejarho = randint(1, 10)
    lejarev = randint(23, 29)
    cvc = randint(100, 999)
    exp = lejarho

    ertekek = {
        'nom': random.choice(vezeteknevek),
        'prenom': random.choice(keresztnevek),
        'cc': (f'{kartyaszam0} {kartyaszam1} {kartyaszam2} {kartyaszam3}'),
        'exp': (f'0{lejarho}/{lejarev}'),
        'cvc': (f'{cvc}'),
        #'sms': '012345',
            }
    
    #print(lejarev)
    #print(cvc)
    #print(f'{kartyaszam0} {kartyaszam1} {kartyaszam2} {kartyaszam3}')
    valasz = requests.post(url, data=ertekek)
    if valasz.ok:
        print(ertekek)
    else:
        print("nemjo :(")
