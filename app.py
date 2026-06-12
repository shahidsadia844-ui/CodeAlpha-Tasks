import string
import random
import sqlite3
from flask import Flask, request, redirect, render_template_string, jsonify

app = Flask(__name__)
DB_NAME = "urls.db"

# 1. Database Initialization Function
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS url_mapping (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            long_url TEXT NOT NULL,
            short_code TEXT UNIQUE NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# 2. Unique Short Code Generator (e.g., 'aB3x9')
def generate_short_code(length=5):
    characters = string.ascii_letters + string.digits
    while True:
        code = ''.join(random.choice(characters) for _ in range(length))
        # Check if code already exists in DB
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM url_mapping WHERE short_code = ?", (code,))
        exists = cursor.fetchone()
        conn.close()
        if not exists:
            return code

# 3. Simple Frontend HTML (Optional task bhi isi mein cover ho jayega)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>URL Shortener</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { font-family: Arial, sans-serif; margin: 30px; text-align: center; background-color: #f4f4f9; }
        .container { max-width: 500px; margin: auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0px 0px 10px rgba(0,0,0,0.1); }
        input[type="url"] { width: 80%; padding: 10px; margin: 10px 0; border: 1px solid #ccc; border-radius: 4px; }
        button { padding: 10px 20px; background-color: #28a745; color: white; border: none; border-radius: 4px; cursor: pointer; }
        .result { margin-top: 20px; font-weight: bold; color: #0056b3; }
    </style>
</head>
<body>
    <div class="container">
        <h2>✂️ Simple URL Shortener</h2>
        <form method="POST" action="/shorten">
            <input type="url" name="long_url" placeholder="Enter long URL here..." required>
            <br>
            <button type="submit">Shorten URL</button>
        </form>
        {% if short_url %}
            <div class="result">
                <p>Your Shortened URL:</p>
                <a href="{{ short_url }}" target="_blank">{{ short_url }}</a>
            </div>
        {% endif %}
    </div>
</body>
</html>
"""

# 4. Home Route (Frontend render karne ke liye)
@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

# 5. API Endpoint: Long URL ko accept karke short code banana
@app.route('/shorten', methods=['POST'])
def shorten_url():
    # Form submission ya JSON input dono ko handle karega
    long_url = request.form.get('long_url') or request.json.get('long_url')
    
    if not long_url:
        return jsonify({"error": "URL is required"}), 400

    # Generate unique code
    short_code = generate_short_code()

    # Save to SQLite database
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO url_mapping (long_url, short_code) VALUES (?, ?)", (long_url, short_code))
    conn.commit()
    conn.close()

    # Create full short URL path
    # request.host_url automatic local ya live server ka domain utha legi
    full_short_url = f"{request.host_url}{short_code}"

    # Agar form se request aayi to page refresh karke result dikhao
    if request.form.get('long_url'):
        return render_template_string(HTML_TEMPLATE, short_url=full_short_url)
    
    # Agar API client (Postman/Json) se aayi to JSON response do
    return jsonify({"short_url": full_short_url}), 201

# 6. Redirect Route: Short code ko original URL par redirect karna
@app.route('/<short_code>')
def redirect_to_original(short_code):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT long_url FROM url_mapping WHERE short_code = ?", (short_code,))
    row = cursor.fetchone()
    conn.close()

    if row:
        original_url = row[0]
        # Agar URL ke sath http/https nahi laga to add kar dein taake external redirect sahi ho
        if not original_url.startswith(('http://', 'https://')):
            original_url = 'https://' + original_url
        return redirect(original_url)
    
    return "<h3>Error: Short URL not found!</h3>", 404

if __name__ == '__main__':
    init_db()  # Server start hote hi table ban jayegi
    app.run(debug=True, port=5000)
      
