import tkinter as tk
from tkinter import ttk, messagebox
import math

# Sample house dataset
# Area, Bedrooms, Bathrooms, City, Price (Lakh)

data = [
    [1200, 3, 2, "Delhi", 65],
    [1500, 3, 3, "Delhi", 82],
    [900, 2, 1, "Noida", 48],
    [1800, 4, 3, "Gurugram", 105],
    [1100, 2, 2, "Ghaziabad", 58],
    [2000, 4, 4, "Delhi", 125],
    [800, 2, 1, "Faridabad", 42],
    [1400, 3, 2, "Noida", 70],
    [2200, 4, 3, "Gurugram", 140],
    [1000, 2, 2, "Ghaziabad", 55],
    [1600, 3, 3, "Delhi", 95],
    [2500, 5, 4, "Gurugram", 160],
    [1300, 3, 2, "Faridabad", 68],
    [1700, 4, 3, "Noida", 98],
    [700, 1, 1, "Ghaziabad", 35],
    [1450, 3, 2, "Delhi", 78],
    [1900, 4, 3, "Noida", 110],
    [950, 2, 1, "Faridabad", 50],
    [2100, 4, 3, "Delhi", 132]
]

# Prediction function using KNN
def predict_price(area, bedrooms, bathrooms, city):
    distances = []

    for house in data:
        distance = math.sqrt(
            ((area - house[0]) / 1000) ** 2 +
            (bedrooms - house[1]) ** 2 +
            (bathrooms - house[2]) ** 2 +
            (0 if city == house[3] else 2)
        )

        distances.append((distance, house[4]))

    distances.sort(key=lambda x: x[0])

    nearest_houses = distances[:3]

    price = sum(h[1] for h in nearest_houses) / 3

    return price


# Main window
root = tk.Tk()
root.title("House Price Prediction")
root.geometry("600x650")
root.resizable(False, False)
root.configure(bg="#eef2f7")

# Header
header = tk.Frame(root, bg="#1e3a8a", height=110)
header.pack(fill="x")

tk.Label(
    header,
    text="HOUSE PRICE PREDICTION",
    font=("Arial", 22, "bold"),
    bg="#1e3a8a",
    fg="white"
).pack(pady=(20, 5))

tk.Label(
    header,
    text="Machine Learning Based Property Price Estimator",
    font=("Arial", 10),
    bg="#1e3a8a",
    fg="#dbeafe"
).pack()

# Main content card
card = tk.Frame(root, bg="white", padx=35, pady=25)
card.pack(padx=30, pady=25, fill="both")

tk.Label(
    card,
    text="Enter House Details",
    font=("Arial", 16, "bold"),
    bg="white",
    fg="#1e293b"
).pack(anchor="w", pady=(0, 20))


def create_label(text):
    tk.Label(
        card,
        text=text,
        font=("Arial", 11, "bold"),
        bg="white",
        fg="#334155"
    ).pack(anchor="w", pady=(8, 4))


# Area
create_label("House Area (Square Feet)")
area_entry = ttk.Entry(card, font=("Arial", 12))
area_entry.pack(fill="x", ipady=6)

# Bedrooms
create_label("Number of Bedrooms")
bedrooms_box = ttk.Combobox(
    card,
    values=["1", "2", "3", "4", "5", "6"],
    state="readonly",
    font=("Arial", 12)
)
bedrooms_box.pack(fill="x", ipady=4)
bedrooms_box.set("3")

# Bathrooms
create_label("Number of Bathrooms")
bathrooms_box = ttk.Combobox(
    card,
    values=["1", "2", "3", "4", "5"],
    state="readonly",
    font=("Arial", 12)
)
bathrooms_box.pack(fill="x", ipady=4)
bathrooms_box.set("2")

# City
create_label("City")
city_box = ttk.Combobox(
    card,
    values=[
        "Delhi",
        "Noida",
        "Gurugram",
        "Ghaziabad",
        "Faridabad"
    ],
    state="readonly",
    font=("Arial", 12)
)
city_box.pack(fill="x", ipady=4)
city_box.set("Delhi")

# Result label
result_frame = tk.Frame(card, bg="#eff6ff", pady=15)
result_frame.pack(fill="x", pady=20)

tk.Label(
    result_frame,
    text="Estimated House Price",
    font=("Arial", 11),
    bg="#eff6ff",
    fg="#475569"
).pack()

result_label = tk.Label(
    result_frame,
    text="₹ 0.00 Lakh",
    font=("Arial", 24, "bold"),
    bg="#eff6ff",
    fg="#1d4ed8"
)
result_label.pack(pady=5)


# Prediction button function
def calculate_price():
    try:
        area = float(area_entry.get())

        if area <= 0:
            messagebox.showerror("Invalid Input", "Area must be greater than zero.")
            return

        bedrooms = int(bedrooms_box.get())
        bathrooms = int(bathrooms_box.get())
        city = city_box.get()

        if not city:
            messagebox.showerror("Error", "Please select a city.")
            return

        price = predict_price(area, bedrooms, bathrooms, city)

        result_label.config(
            text=f"₹ {price:.2f} Lakh"
            )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid house area and select all options."
        )


# Reset function
def reset_fields():
    area_entry.delete(0, tk.END)
    bedrooms_box.set("3")
    bathrooms_box.set("2")
    city_box.set("Delhi")
    result_label.config(text="₹ 0.00 Lakh")


# Buttons
button_frame = tk.Frame(card, bg="white")
button_frame.pack(fill="x")

predict_button = tk.Button(
    button_frame,
    text="PREDICT PRICE",
    font=("Arial", 11, "bold"),
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    activeforeground="white",
    cursor="hand2",
    relief="flat",
    command=calculate_price
)
predict_button.pack(fill="x", ipady=10)

reset_button = tk.Button(
    button_frame,
    text="RESET",
    font=("Arial", 10, "bold"),
    bg="#e2e8f0",
    fg="#334155",
    cursor="hand2",
    relief="flat",
    command=reset_fields
)
reset_button.pack(fill="x", pady=(10, 0), ipady=7)

# Footer
tk.Label(
    root,
    text="Python • Tkinter • KNN Prediction",
    font=("Arial", 9),
    bg="#eef2f7",
    fg="#64748b"
).pack(pady=5)

root.mainloop()
