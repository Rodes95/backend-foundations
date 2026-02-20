name = input("Name: ")
age = int(input("Age: "))
years = int(input("Additional Years: "))

if age < 0 or years < 0:
    print("Invalid data")

else:
    future_age = age + years    
    print(f"{name}, you're {age} years old. In {years} years from now, you will be {future_age}!")
    
    if future_age > 100:
        print("Legend mode activated!")
