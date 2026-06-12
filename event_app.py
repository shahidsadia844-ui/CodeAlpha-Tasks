import sqlite3
from flask import Flask, request, jsonify, render_template_string, redirect

app = Flask(__name__)
DB_NAME = "events.db"

# ==========================================
# 1. DATABASE SETUP (Tables initialization)
# ==========================================
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Events Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            date TEXT NOT NULL,
            available_seats INTEGER NOT NULL
        )
    ''')
    
    # Registrations Table (Linked to Events)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS registrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_id INTEGER NOT NULL,
            user_name TEXT NOT NULL,
            user_email TEXT NOT NULL,
            FOREIGN KEY (event_id) REFERENCES events (id)
        )
    ''')
    
    # Dummy Data: Agar tables khali hain toh kuch events pehle se add kar dete hain
    cursor.execute("SELECT COUNT(*) FROM events")
    if cursor.fetchone()[0] == 0:
        dummy_events = [
            ('Python Coding Workshop', '2026-07-15', 30),
            ('Web Design Seminar', '2026-08-02', 25),
            ('AI & Robotics Summit', '2026-09-10', 50)
        ]
        cursor.executemany("INSERT INTO events (title, date, available_seats) VALUES (?, ?, ?)", dummy_events)
        
    conn.commit()
    conn.close()

# ==========================================
# 2. FRONTEND TEMPLATE (HTML UI)
# ==========================================
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Event Registration System</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f7f6; margin: 10px; padding: 10px; }
        .card { background: white; padding: 15px; margin-bottom: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        h2, h3 { color: #2c3e50; border-bottom: 2px solid #ecf0f1; padding-bottom: 5px; }
        table { width: 100%; border-collapse: collapse; margin-top: 10px; }
        th, td { border: 1px solid #bdc3c7; padding: 8px; text-align: left; }
        th { background-color: #ecf0f1; }
        input, select, button { padding: 8px; margin: 5px 0; width: 100%; box-sizing: border-box; }
        button { background-color: #2980b9; color: white; border: none; border-radius: 4px; cursor: pointer; font-weight: bold; }
        button:hover { background-color: #3498db; }
        .badge { padding: 4px 8px; border-radius: 4px; font-size: 12px; font-weight: bold; background-color: #2ecc71; color: white; }
    </style>
</head>
<body>
    <div style="max-width: 700px; margin: auto;">
        <h1 style="text-align: center; color: #2c3e50;">📅 Event Registration Dashboard</h1>
        
        <div class="card">
            <h3>✨ Upcoming Events</h3>
            <table>
                <tr><th>ID</th><th>Event Title</th><th>Date</th><th>Available Seats</th></tr>
                {% for event in events %}
                <tr>
                    <td>#{{ event[0] }}</td>
                    <td><strong>{{ event[1] }}</strong></td>
                    <td>{{ event[2] }}</td>
                    <td><span class="badge">{{ event[3] }} Seats Left</span></td>
                </tr>
                {% endfor %}
            </table>
        </div>

        <div class="card">
            <h3>📝 Join an Event</h3>
            <form method="POST" action="/api/register">
                <label>Choose Event:</label>
                <select name="event_id" required>
                    {% for event in events %}
                        {% if event[3] > 0 %}
                            <option value="{{ event[0] }}">{{ event[1] }}</option>
                        {% endif %}
                    {% endfor %}
                </select>
                
                <input type="text" name="user_name" placeholder="Your Full Name" required>
                <input type="email" name="user_email" placeholder="Your Email Address" required>
                
                <button type="submit">Submit Registration</button>
            </form>
        </div>

        <div class="card">
            <h3>👥 Total Registered Users</h3>
            <table>
                <tr><th>Reg ID</th><th>User Name</th><th>Email</th><th>Event ID</th></tr>
                {% for reg in registrations %}
                <tr>
                    <td>#{{ reg[0] }}</td>
                    <td>{{ reg[2] }}</td>
                    <td>{{ reg[3] }}</td>
                    <td>Event #{{ reg[1] }}</td>
                </tr>
                {% endfor %}
            </table>
        </div>
    </div>
</body>
</html>
"""

# ==========================================
# 3. API ENDPOINTS & LOGIC ROUTES
# ==========================================

@app.route('/')
def index():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM events")
    events_data = cursor.fetchall()
    cursor.execute("SELECT * FROM registrations")
    regs_data = cursor.fetchall()
    conn.close()
    return render_template_string(HTML_TEMPLATE, events=events_data, registrations=regs_data)

# API Endpoint to View Events List (GET)
@app.route('/api/events', methods=['GET'])
def get_events():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM events")
    rows = cursor.fetchall()
    conn.close()
    return jsonify([{"id": r[0], "title": r[1], "date": r[2], "seats_left": r[3]} for r in rows])

# API Endpoint to Submit Registration Form (POST) - Auto Updates Seats Left
@app.route('/api/register', methods=['POST'])
def register_user():
    event_id = request.form.get('event_id') or request.json.get('event_id')
    user_name = request.form.get('user_name') or request.json.get('user_name')
    user_email = request.form.get('user_email') or request.json.get('user_email')
    
    if not event_id or not user_name or not user_email:
        return jsonify({"error": "All fields are required"}), 400
        
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Check if seats are available
    cursor.execute("SELECT available_seats FROM events WHERE id = ?", (event_id,))
    event_row = cursor.fetchone()
    
    if not event_row:
        conn.close()
        return jsonify({"error": "Event not found"}), 404
        
    seats_left = event_row[0]
    if seats_left <= 0:
        conn.close()
        return jsonify({"error": "Sorry, this event is already full!"}), 400

    # Save user registration data
    cursor.execute("INSERT INTO registrations (event_id, user_name, user_email) VALUES (?, ?, ?)", 
                   (event_id, user_name, user_email))
    
    # Auto-update logic for decreasing available seats counter
    cursor.execute("UPDATE events SET available_seats = available_seats - 1 WHERE id = ?", (event_id,))
    
    conn.commit()
    conn.close()
    
    if request.form.get('event_id'):
        return redirect('/')
        
    return jsonify({"message": "Successfully registered for the event!"}), 201

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)
  
