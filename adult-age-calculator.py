print("Adult Age Calculator")
print("=" * 40)

age = int(input("Enter your age: "))

print("\n" + "=" * 40)

if age < 18:
    years_left = 18 - age
    target_year = 2026 + years_left
    print(f"You have {years_left} years left,")
    print(f"You will be adult in year {target_year}")
    
elif age == 18:
    print("You just became adult!")
    print("This year (2026) is your adult year")
    
else:
    years_passed = age - 18
    adult_year = 2026 - years_passed
    print(f"You became adult in year {adult_year},")
    print(f"{years_passed} years passed since adulthood")

print("=" * 40)
