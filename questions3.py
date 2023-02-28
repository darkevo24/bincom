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

# Sort the list of colors
sorted_colors = sorted(all_colors, key=lambda x: color_dict[x])

# Find the median color
n = len(sorted_colors)
if n % 2 == 1:
    median_color = sorted_colors[n//2]
else:
    i = n//2
    median_value = (color_dict[sorted_colors[i-1]] + color_dict[sorted_colors[i]]) / 2
    for color, value in color_dict.items():
        if value == median_value:
            median_color = color
            break

print("The median color is:", median_color)
