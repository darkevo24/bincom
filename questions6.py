import psycopg2
from collections import Counter
from bs4 import BeautifulSoup

# Define a dictionary to map color names to numerical values
color_dict = {
    'GREEN': 1,
    'YELLOW': 2,
    'BROWN': 3,
    'BLUE': 4,
    'PINK': 5,
    'ORANGE': 6,
    'CREAM': 7,
    'RED': 8,
    'WHITE': 9,
    'BLACK': 10,
    'ARSH' : 11,
    'BLEW' : 12
}

# Parse the HTML code using BeautifulSoup
with open("index.html", "r") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

# Extract the table rows and their data
table = soup.find('table')
table_rows = table.find_all('tr')[1:]  # Skip the header row

# Create a list of all the colors in the table
all_colors = []
for row in table_rows:
    color_str = row.find_all('td')[1].text
    all_colors.extend(color_str.split(', '))

# Count the frequency of each color
color_counts = Counter(all_colors)

# Connect to the database
conn = psycopg2.connect(
    host="localhost",
    database="mydatabase",
    user="myusername",
    password="mypassword"
)

# Insert the color frequencies into the database
with conn.cursor() as cur:
    for color, frequency in color_counts.items():
        cur.execute(
            "INSERT INTO color_frequencies (color, frequency) VALUES (%s, %s)",
            (color, frequency)
        )
    conn.commit()

# Close the database connection
conn.close()
