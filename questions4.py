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

# Calculate the mean color value
n = len(all_colors)
mean_value = sum(color_dict[color] for color in all_colors) / n

# Calculate the sum of squared differences from the mean
ssd = sum((color_dict[color] - mean_value)**2 for color in all_colors)

# Calculate the variance
variance = ssd / n

print("The variance of the colors is:", variance)
