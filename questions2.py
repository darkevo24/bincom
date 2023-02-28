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
    color_cell = row.find_all('td')[1]  # Get the second cell (index 1) in the row
    all_colors.extend(color_cell.text.split(', '))

# Count the frequency of each color
color_freq = Counter(all_colors)

# Find the color with the highest frequency
most_common_color = color_freq.most_common(1)[0][0]

print("The color mostly worn throughout the week is:", most_common_color)
