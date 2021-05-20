flower_type = input()
count_flowers = int(input())
budget = int(input())
price_per_flower = 0

if flower_type == "Roses":
    price_per_flower = 5
    if count_flowers > 80:
        price_per_flower = price_per_flower * 0.9
elif flower_type == "Dahlias":
    price_per_flower = 3.80
    if count_flowers > 90:
        price_per_flower = price_per_flower * 0.85
elif flower_type == "Tulips":
    price_per_flower = 2.80
    if count_flowers > 80:
        price_per_flower = price_per_flower * 0.85
elif flower_type == "Narcissus":
    price_per_flower = 3
    if count_flowers < 120:
        price_per_flower += price_per_flower * 0.15
elif flower_type == "Gladiolus":
    price_per_flower = 2.50
    if count_flowers < 80:
        price_per_flower += price_per_flower * 0.2

total_price = count_flowers * price_per_flower

if total_price > budget:
    money_needed = total_price - budget
    print(f"Not enough money, you need {money_needed:.2f} leva more.")
else:
    money_left = budget - total_price
    print(f"Hey, you have a great garden with {count_flowers} {flower_type} and {money_left:.2f} leva left.")