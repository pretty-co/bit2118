
import numpy as np

temperatures = np.array([
    4.2, 4.5, 5.0, 4.8,
    5.3, 6.1, 8.5, 5.2
])

minimum_safe = 2.0
maximum_safe = 8.0

average = np.mean(temperatures)
lowest = np.min(temperatures)
highest = np.max(temperatures)


unsafe_readings = temperatures[
    (temperatures < minimum_safe) |
    (temperatures > maximum_safe)
]

print(f"Average temperature: {average:.2f} C")
print(f"Minimum temperature: {lowest:.2f} C")
print(f"Maximum temperature: {highest:.2f} C")

print("Unsafe readings:", unsafe_readings)

if len(unsafe_readings) > 0:
    print("WARNING: Temperature limit exceeded!")
else:
    print("All readings are within the acceptable range.")
