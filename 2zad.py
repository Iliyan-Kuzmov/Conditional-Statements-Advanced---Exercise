gradusi = int(input())
wreme = str(input())
if 10 <= gradusi <= 18:
    if wreme == "Morning":
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif wreme == "Afternoon":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif wreme  == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
elif 18 < gradusi <= 24:
    if wreme == "Morning":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif wreme == "Afternoon":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif wreme  == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
elif 25 <= gradusi:
    if wreme == "Morning":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif wreme == "Afternoon":
        outfit = "Swim Suit"
        shoes = "Barefoot"
    elif wreme  == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
print(f"It's {gradusi} degrees, get your {outfit} and {shoes}.")