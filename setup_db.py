mport sqlite3

# Create user_data.db
conn1 = sqlite3.connect('user_data.db')
conn1.execute('''CREATE TABLE IF NOT EXISTS users (
    number_plate TEXT PRIMARY KEY,
    user_name TEXT,
    vehicle_type TEXT,
    contact TEXT
)''')

conn1.executemany('INSERT OR IGNORE INTO users VALUES (?, ?, ?, ?)', [
    ('TS09AB1234', 'Ravi Kumar', 'Car', '9876543210'),
    ('TS09CD5678', 'Anita Sharma', 'Truck', '9876543211'),
    ('TS09EF9012', 'Rakesh Reddy', 'Bike', '9876543212'),
    ('TS09GH3456', 'Neha Singh', 'Car', '9876543213'),
    ('TS09IJ7890', 'Vikram Rao', 'Truck', '9876543214')
])
conn1.commit()
conn1.close()

# Create toll_data.db
conn2 = sqlite3.connect('toll_data.db')
conn2.execute('''CREATE TABLE IF NOT EXISTS tolls (
    number_plate TEXT PRIMARY KEY,
    balance REAL,
    fine REAL
)''')

conn2.executemany('INSERT OR IGNORE INTO tolls VALUES (?, ?, ?)', [
    ('TS09AB1234', 150.0, 0.0),
    ('TS09CD5678', 40.0, 0.0),
    ('TS09EF9012', 200.0, 0.0),
    ('TS09GH3456', 20.0, 0.0),
    ('TS09IJ7890', 300.0, 0.0)
])
conn2.commit()
conn2.close()

print("✅ Databases created successfully.")
