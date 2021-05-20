budget = float(input())
season = input()
if budget <= 100:
    if season == "summer":
        budget = budget * 0.3
        wid_pochiwka = "Camp"
    elif season == "winter":
        budget = budget * 0.7
        wid_pochiwka = "Hotel"
    destination = "Bulgaria"
elif 100 < budget <= 1000:
    if season == "summer":
        budget = budget * 0.4
        wid_pochiwka = "Camp"
    elif season == "winter":
        budget = budget * 0.8
        wid_pochiwka = "Hotel"
    destination = "Balkans"
elif budget > 1000:
    budget = budget * 0.9
    destination = "Europe"
    wid_pochiwka = "Hotel"
print(f"Somewhere in {destination}")
print(f"{wid_pochiwka} - {budget:.2f}")
budget = float(input())
season = input()
if budget <= 100:
    if season == "summer":
        budget = budget * 0.3
        wid_pochiwka = "Camp"
    elif season == "winter":
        budget = budget * 0.7
        wid_pochiwka = "Hotel"
    destination = "Bulgaria"
elif 100 < budget <= 1000:
    if season == "summer":
        budget = budget * 0.4
        wid_pochiwka = "Camp"
    elif season == "winter":
        budget = budget * 0.8
        wid_pochiwka = "Hotel"
    destination = "Balkans"
elif budget > 1000:
    budget = budget * 0.9
    destination = "Europe"
    wid_pochiwka = "Hotel"
print(f"Somewhere in {destination}")
print(f"{wid_pochiwka} - {budget:.2f}")