import sqlite3

conn = sqlite3.connect('fabric.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS countries(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL)
''')

cursor.execute("INSERT INTO countries (title) VALUES ('Kyrgyzstan')")
cursor.execute(" INSERT INTO countries (title) VALUES('Kazakhstan')")
cursor.execute("INSERT INTO countries (title) VALUES('Turkey')")

cursor.execute('''
    CREATE TABLE IF NOT EXISTS cities(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        area DOUBLE NOT NULL DEFAULT 0,
        country_id INTEGER,
        FOREIGN KEY (country_id)
        REFERENCES countries (id))
''')

cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Bishkek', 1)")
cursor.execute("INSERT INTO cities(title, country_id) VALUES ('Osh', 1)")
cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Zaysan', 2)")
cursor.execute("INSERT INTO cities(title, country_id) VALUES ('Zhitikara', 2)")
cursor.execute("INSERT INTO cities(title, country_id) VALUES ('Istanbul', 3)")
cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Adana', 3)")
cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Naryn', 1)")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        city_id INTEGER,
        FOREIGN KEY (city_id) REFERENCES city(id))
""")
cursor.execute("INSERT INTO employees(first_name, last_name, city_id) VALUES ('Larry','Johnson', 1)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Sally','Fisher', 1)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Dilnoza','Umetalieva', 2)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Jackson','Murdochiv', 2) ")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Ru','Stebelson', 3)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Dea','Noviana', 3)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Gwynplaine','Futcher', 1)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Sergey','Sergeevich', 1)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Anna','Umetova', 2)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Tatyana','Vladimirovna', 2)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Mikhail','Mikhalovich', 3)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Ksyusha','Lyubovnaya', 3)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Bakyt','Rakhmatovich', 1)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Angelika','Krasnovaya', 1)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Lola','Milakhova', 2)")

while True:
    print(
        'You can display a list of employees by selected city id from the list of cities below, \n'
        'for exit the program, enter 0:'
    )
    cursor.execute('SELECT id, title FROM cities')
    cities = cursor.fetchall()
    for city in cities:
        print(f'{city[0]}. {city[1]}')

    selected_city_id = input('Enter city id (enter "0" to exit)): ')
    if selected_city_id == "0":
        break

    cursor.execute('''
        SELECT e.first_name, e.last_name, c.title, c.area, co.title
        FROM employees e 
        JOIN cities c ON e.city_id = c.id
        JOIN countries co ON c.country_id = co.id
        WHERE c.id = ?
        ''', (selected_city_id))

    employees = cursor.fetchall()
    if not employees:
        print('There are no employees in this city')
    else:
        print('First name|Last name|City|City area|Country')
        for employee in employees:
            print(f'{employee[0]} | {employee[1]} | {employee[2]} | {employee[3]} | {employee[4]}')


conn.close





