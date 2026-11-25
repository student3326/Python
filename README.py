import math

# House Price Prediction using Python
# Machine Learning: K-Nearest Neighbors (KNN)

data = [
    [1200, 3, 2, 1, 65],
    [1500, 3, 3, 1, 82],
    [900,  2, 1, 1, 48],
    [1800, 4, 3, 2, 105],
    [1100, 2, 2, 2, 58],
    [2000, 4, 4, 3, 125],
    [800,  2, 1, 4, 42],
    [1400, 3, 2, 4, 70],
    [2200, 4, 3, 5, 140],
    [1000, 2, 2, 5, 55],
    [1600, 3, 3, 3, 95],
    [2500, 5, 4, 3, 160],
    [1300, 3, 2, 5, 68],
    [1700, 4, 3, 1, 98],
    [700,  1, 1, 4, 35]
]

cities = {
    1: "Delhi",
    2: "Noida",
    3: "Gurugram",
    4: "Ghaziabad",
    5: "Faridabad"
}

print("===================================")
print("     HOUSE PRICE PREDICTION")
print("===================================")
print("Cities:")
for key, value in cities.items():
    print(key, "-", value)

area = int(input("\nEnter house area (sq. ft.): "))
bedrooms = int(input("Enter number of bedrooms: "))
bathrooms = int(input("Enter number of bathrooms: "))
city = int(input("Select city number: "))

if city not in cities:
    print("Invalid city selection!")
else:
    # Calculate distance from input house to dataset houses
    distances = []

    for house in data:
        distance = math.sqrt(
            ((area - house[0]) / 1000) ** 2 +
            (bedrooms - house[1]) ** 2 +
            (bathrooms - house[2]) ** 2 +
            (city - house[3]) ** 2
        )

        distances.append((distance, house[4]))

    # Sort houses according to distance
    distances.sort(key=lambda x: x[0])

    # Select 3 nearest houses
    nearest = distances[:3]

    # Calculate predicted price
    predicted_price = sum(house[1] for house in nearest) / len(nearest)

    print("\n===================================")
    print("        PREDICTION RESULT")
    print("===================================")
    print("City:", cities[city])
    print("Area:", area, "sq. ft.")
    print("Bedrooms:", bedrooms)
    print("Bathrooms:", bathrooms)
    print("-----------------------------------")
    print("Estimated House Price: ₹",
          round(predicted_price, 2), "Lakh")
    print("===================================")
