# Coffee Shop Challenge

A small Python project modeling a coffee shop domain with three core classes—`Customer`, `Coffee`, and `Order`—in an object‑oriented way. It demonstrates:

- **One‑to‑many** (Customer → Orders; Coffee → Orders)  
- **Many‑to‑many** (Customer ↔ Coffee through Order)  
- Data validation, immutability of key attributes  
- Aggregation methods and a “most aficionado” bonus feature  
- A full test suite using pytest  

---

## 📁 Folder Structure

coffee‑shop‑challenge/
├── customer.py # Customer model
├── coffee.py # Coffee model
├── order.py # Order model (tracks all orders globally)
├── debug.py # Quick manual test script
├── Pipfile # (optional) Pipenv dependencies
└── tests/
├── test_customer.py # pytest tests for Customer
├── test_coffee.py # pytest tests for Coffee
└── test_order.py # pytest tests for Order

yaml
Copy
Edit

---

## 🛠️ Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/<your-username>/coffee-shop-challenge.git
   cd coffee-shop-challenge
(Optional) Create & activate a virtual environment

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
Install dependencies

If using Pipenv:

bash
Copy
Edit
pipenv install --dev pytest
pipenv shell
Otherwise:

bash
Copy
Edit
pip install pytest
▶️ Usage
1. Manual Testing
Run the debug.py script to see sample objects, relationships, and aggregate outputs in action:

bash
Copy
Edit
python debug.py
You should see printed lists of orders, unique coffees, number of orders, average prices, and the top aficionado.

2. Automated Tests
Execute the full test suite with pytest:

bash
Copy
Edit
pytest -q
You should see output like:

python-repl
Copy
Edit
...   # one dot per passing test
9 passed in 0.12s
🧩 Design Highlights
Validation:

Customer.name must be a str 1–15 chars.

Coffee.name must be a str ≥3 chars (immutable).

Order.price must be a float between 1.0–10.0.

Relationships:

Customer.orders() & Customer.coffees()

Coffee.orders() & Coffee.customers()

Aggregates:

Coffee.num_orders(), Coffee.average_price()

Customer.create_order()

Bonus:

Customer.most_aficionado(coffee) returns the customer who spent the most on a given coffee, or None.

📜 License
This project is released under the MIT License. Feel free to copy, modify, and use for your own learning!
