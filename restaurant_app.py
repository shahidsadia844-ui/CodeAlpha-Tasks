import sqlite3
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)
DB_NAME = "restaurant.db"

# ==========================================
# 1. DATABASE SETUP (Tables initialization)
# ==========================================
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Menu Items Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS menu (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            category TEXT NOT NULL
        )
    ''')
    
    # Restaurant Tables Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS restaurant_tables (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            table_number INTEGER UNIQUE NOT NULL,
            status TEXT DEFAULT 'Available'
        )
    ''')
    
    # Orders Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            table_number INTEGER NOT NULL,
            items TEXT NOT NULL,
            total_amount REAL NOT NULL,
            status TEXT DEFAULT 'Pending'
        )
    ''')
    
    # Insert dummy menu data if empty
    cursor.execute("SELECT COUNT(*) FROM menu")
    if cursor.fetchone()[0] == 0:
        dummy_menu = [
            ('Biryani', 350.0, 'Main Course'),
            ('Chicken Karahi', 1200.0, 'Main Course'),
            ('Garlic Naan', 60.0, 'Bread'),
            ('Mint Margarita', 180.0, 'Beverages')
        ]
        cursor.executemany("INSERT INTO menu (name, price, category) VALUES (?, ?, ?)", dummy_menu)
        
    # Insert dummy tables if empty
    cursor.execute("SELECT COUNT(*) FROM restaurant_tables")
    if cursor.fetchone()[0] == 0:
        for i in range(1, 6):
            cursor.execute("INSERT INTO restaurant_tables (table_number, status) VALUES (?, 'Available')", (i,))
            
    conn.commit()
    conn.close()

# ==========================================
# 2. FRONTEND TEMPLATE
# ==========================================
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Restaurant Management System</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { font-family: Arial, sans-serif; background-color: #f8f9fa; margin: 10px; padding: 10px; }
        .card { background: white; padding: 15px; margin-bottom: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        h2, h3 { color: #343a40; border-bottom: 2px solid #e9ecef; padding-bottom: 5px; }
        table { width: 100%; border-collapse: collapse; margin-top: 10px; }
        th, td { border: 1px solid #dee2e6; padding: 8px; text-align: left; }
        th { background-color: #e9ecef; }
        input, select, button { padding: 8px; margin: 5px 0; width: 100%; box-sizing: border-box; }
        button { background-color: #007bff; color: white; border: none; border-radius: 4px; cursor: pointer; font-weight: bold; }
        .badge { padding: 4px 8px; border-radius: 4px; font-size: 12px; font-weight: bold; }
        .Available { background-color: #28a745; color: white; }
        .Booked { background-color: #dc3545; color: white; }
    </style>
</head>
<body>
    <div style="max-width: 800px; margin: auto;">
        <h1 style="text-align: center; color: #212529;">🍽️ Restaurant Admin Panel</h1>
        
        <div class="card">
            <h3>📖 Menu & 🪑 Tables Status</h3>
            <div style="display: flex; gap: 20px; flex-wrap: wrap;">
                <div style="flex: 1; min-width: 250px;">
                    <h4>Today's Menu</h4>
                    <table>
                        <tr><th>Item</th><th>Price</th></tr>
                        {% for item in menu %}
                        <tr><td>{{ item[1] }}</td><td>Rs. {{ item[2] }}</td></tr>
                        {% endfor %}
                    </table>
                </div>
                <div style="flex: 1; min-width: 200px;">
                    <h4>Table Seating</h4>
                    <table>
                        <tr><th>Table No.</th><th>Status</th></tr>
                        {% for table in tables %}
                        <tr><td>Table {{ table[1] }}</td><td><span class="badge {{ table[2] }}">{{ table[2] }}</span></td></tr>
                        {% endfor %}
                    </table>
                </div>
            </div>
        </div>

        <div class="card">
            <h3>📝 Place New Order</h3>
            <form method="POST" action="/api/orders">
                <label>Select Table:</label>
                <select name="table_number" required>
                    {% for table in tables %}
                        {% if table[2] == 'Available' %}
                            <option value="{{ table[1] }}">Table {{ table[1] }}</option>
                        {% endif %}
                    {% endfor %}
                </select>
                
                <label>Select Food Item:</label>
                <select name="item_name" required>
                    {% for item in menu %}
                        <option value="{{ item[1] }}">{{ item[1] }} (Rs. {{ item[2] }})</option>
                    {% endfor %}
                </select>
                
                <button type="submit">Submit Order & Book Table</button>
            </form>
        </div>

        <div class="card">
            <h3>🛎️ Active Orders & Billing</h3>
            <table>
                <tr><th>Order ID</th><th>Table</th><th>Items Ordered</th><th>Total Bill</th><th>Status</th></tr>
                {% for order in orders %}
                <tr>
                    <td>#{{ order[0] }}</td>
                    <td>Table {{ order[1] }}</td>
                    <td>{{ order[2] }}</td>
                    <td>Rs. {{ order[3] }}</td>
                    <td><span class="badge" style="background-color: #ffc107; color: black;">{{ order[4] }}</span></td>
                </tr>
                {% endfor %}
            </table>
        </div>
    </div>
</body>
</html>
"""

# ==========================================
# 3. API ENDPOINTS & ROUTES
# ==========================================

@app.route('/')
def dashboard():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM menu")
    menu_data = cursor.fetchall()
    cursor.execute("SELECT * FROM restaurant_tables")
    table_data = cursor.fetchall()
    cursor.execute("SELECT * FROM orders")
    order_data = cursor.fetchall()
    conn.close()
    return render_template_string(HTML_TEMPLATE, menu=menu_data, tables=table_data, orders=order_data)

@app.route('/api/menu', methods=['GET'])
def get_menu():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM menu")
    rows = cursor.fetchall()
    conn.close()
    return jsonify([{"id": r[0], "name": r[1], "price": r[2], "category": r[3]} for r in rows])

@app.route('/api/orders', methods=['POST'])
def place_order():
    table_number = request.form.get('table_number') or request.json.get('table_number')
    item_name = request.form.get('item_name') or request.json.get('item_name')
    
    if not table_number or not item_name:
        return jsonify({"error": "Missing table number or item name"}), 400
        
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("SELECT status FROM restaurant_tables WHERE table_number = ?", (table_number,))
    table_status = cursor.fetchone()
    
    if not table_status or table_status[0] == 'Booked':
        conn.close()
        return jsonify({"error": f"Table {table_number} is already occupied"}), 400

    cursor.execute("SELECT price FROM menu WHERE name = ?", (item_name,))
    item_price_row = cursor.fetchone()
    if not item_price_row:
        conn.close()
        return jsonify({"error": "Item not found in menu"}), 400
    
    total_amount = item_price_row[0]

    cursor.execute("INSERT INTO orders (table_number, items, total_amount, status) VALUES (?, ?, ?, 'Processing')", 
                   (table_number, item_name, total_amount))
    cursor.execute("UPDATE restaurant_tables SET status = 'Booked' WHERE table_number = ?", (table_number,))
    
    conn.commit()
    conn.close()
    
    if request.form.get('table_number'):
        return redirect('/')
        
    return jsonify({"message": "Order placed successfully", "table_status": "Booked"}), 201

# Yahan humne file check ko thoda update kiya hai name change ke mutabiq
if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)

