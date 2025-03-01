# Input the age in Earth years
earth_age = float(input("Enter your age in Earth years: "))

# Conversion factor: 1 Earth year = 365.25 days
# 1 Martian year = 687 days
earth_days = earth_age * 365.25
mars_age = earth_days / 687

# Print the results
print("Your age on Earth is:", earth_age, "years")
print("Your age on Mars is:", "%.2f" % mars_age, "years")
