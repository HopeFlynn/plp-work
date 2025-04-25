def divisible_by_ten(num):
    if num % 10 == 0:
        print(f"{num} is divisible by 10.")
        return True
    else:
        print(f"{num} is not divisible by 10.")
        return False

# User interaction
num = int(input("Enter a number to check if it is divisible by 10: "))
result = divisible_by_ten(num)
print("Result:", result)
