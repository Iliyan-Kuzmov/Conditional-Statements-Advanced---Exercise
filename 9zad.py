import math
wid_godina = input()
p = int(input())
h = int(input())
uikendi_sofiq = 48 - h
igri_sofiq = uikendi_sofiq * 3/4
igrae_praznik = p * 2/3
if wid_godina == "normal":
    obsto = igri_sofiq + h + igrae_praznik
    print(math.floor(obsto))
elif wid_godina == "leap":
    obsto = igri_sofiq + h + igrae_praznik
    obsto = obsto * 1.15
    print(math.floor(obsto))
