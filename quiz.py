N = int(input("Enter number of apps sold: "))

total_income = 0
pro_count = 0

for i in range(1, N + 1):
    price = float(input(f"Enter price of app {i}: "))
    
    total_income += price

    if price > 300:
        print("Pro App")
        pro_count += 1
    else:
        print("Regular App")

print("\nTotal Income =", total_income)
print("Number of Pro Apps =", pro_count)
