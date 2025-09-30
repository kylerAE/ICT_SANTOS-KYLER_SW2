from pyscript import display

# Strings
shop_name = "Kyler's Hobby Shop"
owner_name = "Kyler the Boss"

# Integer
year_since = 2025

# Float
tax_rate = 0.08

# Booleans
has_delivery = True
is_dine_in = True
is_takeaway = False

# List
product_names = [
    "Pokemon EX Box",
    "Jordan 11s",
    "Pokemon elite trainer box",
    "Pokemon booster box",
    "Jordan 1s"
]

# Tuple
business_hours = (
    "Monday - Friday: 10am - 8pm",
    "Saturday: 10am - 6pm",
    "Sunday: Closed"
)

# Dictionary
menu = {
    "Pokemon EX Box": 120.00,
    "Jordan 11s": 250.00,
    "Pokemon elite trainer box": 60.00,
    "Pokemon booster box": 90.00,
    "Jordan 1s": 180.00
}

# Set
common_items = {"Pokemon cards", "Jordan shoes", "Funko Pops", "Sports cards"}

# Display shop info
display(shop_name, target="shop-name")
display(f"Owner: {owner_name} | Since {year_since}", target="owner-info")

# Display products in table
rows = ""
for product, price in menu.items():
    rows += f"<tr><td>{product}</td><td>{price:.2f}</td></tr>"
display(rows, target="product-table")

# Display business hours
hours = "<br>".join(business_hours)
display(hours, target="hours")

# Decide order type
if is_dine_in:
    order_type = "Dine-in Available"
elif is_takeaway:
    order_type = "Takeaway Available"
elif has_delivery:
    order_type = "Delivery Available"
else:
    order_type = "Order Type Unavailable"

# Extra info
extra_text = f"💰 Tax Rate: {tax_rate * 100}%<br>🔥 Popular items: {', '.join(common_items)}<br>📦 {order_type}"
display(extra_text, target="extra")
