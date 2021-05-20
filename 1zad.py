tip = input()
redowe = int(input())
koloni = int(input())
prihodi = 0
kapacitet = redowe * koloni
if tip == "Premiere":
    prihodi = kapacitet * 12.00
elif tip == "Normal":
    prihodi = kapacitet * 7.50
elif tip == "Discount":
    prihodi = kapacitet * 5.00
print(f"{prihodi:.2f} leva")