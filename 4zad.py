budget = int(input())
season = input()
broi_ribari = int(input())
ship_spring = 3000
ship_summer = 4200
ship_autumn = 4200
ship_winter = 2600
if season == "Spring":
    if broi_ribari <= 6:
        ship_spring = ship_spring * 0.9
    elif 7 < broi_ribari <= 11:
        ship_spring = ship_spring * 0.85
    elif broi_ribari >= 12:
        ship_spring = ship_spring * 0.75
    if broi_ribari % 2 == 0:
        ship_spring = ship_spring * 0.95
    if ship_spring < budget:
        ostanali_pari = budget - ship_spring
        print(f"Yes! You have {ostanali_pari:.2f} leva left.")
    elif ship_spring > budget:
        nedostigasti_pari = ship_spring - budget
        print(f"Not enough money! You need {nedostigasti_pari:.2f} leva.")
elif season == "Summer":
    if broi_ribari <= 6:
        ship_summer = ship_summer * 0.9
    elif 7 < broi_ribari <= 11:
        ship_summer = ship_summer * 0.85
    elif broi_ribari >= 12:
        ship_summer = ship_summer * 0.75
    if broi_ribari % 2 == 0:
        ship_summer = ship_summer * 0.95
    if ship_summer < budget:
        ostanali_pari = budget - ship_summer
        print(f"Yes! You have {ostanali_pari:.2f} leva left.")
    elif ship_summer > budget:
        nedostigasti_pari = ship_summer - budget
        print(f"Not enough money! You need {nedostigasti_pari:.2f} leva.")
elif season == "Autumn":
    if broi_ribari <= 6:
        ship_autumn = ship_autumn * 0.9
    elif 7 < broi_ribari <= 11:
        ship_autumn = ship_autumn * 0.85
    elif broi_ribari >= 12:
        ship_autumn = ship_autumn * 0.75
    if ship_autumn < budget:
        ostanali_pari = budget - ship_autumn
        print(f"Yes! You have {ostanali_pari:.2f} leva left.")
    elif ship_autumn > budget:
        nedostigasti_pari = ship_autumn - budget
        print(f"Not enough money! You need {nedostigasti_pari:.2f} leva.")
elif season == "Winter":
    if broi_ribari <= 6:
        ship_winter = ship_winter * 0.9
    elif 7 < broi_ribari <= 11:
        ship_winter = ship_winter * 0.85
    elif broi_ribari >= 12:
        ship_winter = ship_winter * 0.75
    if broi_ribari % 2 == 0:
        ship_winter = ship_winter * 0.95
    if ship_winter < budget:
        ostanali_pari = budget - ship_winter
        print(f"Yes! You have {ostanali_pari:.2f} leva left.")
    elif ship_winter > budget:
        nedostigasti_pari = ship_winter - budget
        print(f"Not enough money! You need {nedostigasti_pari:.2f} leva.")

