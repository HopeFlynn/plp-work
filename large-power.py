def large_power(base, exponent):
    result = base ** exponent  # Calculate power
    print(f"{base} to the power of {exponent} is {result}")
    
    if result > 5000:
        return True
    else:
        return False

# Example calls
print(large_power(10, 3))   # Output: 1000 → False
print(large_power(10, 4))   # Output: 10000 → True
