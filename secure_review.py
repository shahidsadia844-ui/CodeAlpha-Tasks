import sqlite3

# 1. INSECURE FUNCTION (Is mein vulnerability hai)
def insecure_login(username, password):
    # Yeh bad tareeqa hai kyunkay is mein SQL Injection ho sakta hai
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print(f"[!] Executing Insecure Query: {query}")
    return query

# 2. SECURE FUNCTION (Yeh bilkul safe tareeqa hai)
def secure_login(username, password):
    # Yeh bilkul sahi tareeqa hai parameterized queries use karne ka
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    print(f"[+] Executing Secure Query: {query} with parameters ({username}, {password})")
    return query

if __name__ == "__main__":
    print("--- CodeAlpha Secure Coding Review ---")
    # Test cases
    insecure_login("admin' OR '1'='1", "password")
    secure_login("admin' OR '1'='1", "password")
                 
