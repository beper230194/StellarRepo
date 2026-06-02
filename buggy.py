import hashlib

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()
    
def get_user(user_id):
    import sqlite3
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
    return cursor.fetchone()

def process_data(items):
    results = []
    try:
        for item in items:
            results.append(item['value'] * 2)
    except:
        pass
    return results