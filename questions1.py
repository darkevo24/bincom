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
color_freq = Counter(all_colors)

# Calculate the total frequency and sum of numerical values
total_freq = sum(color_freq.values())
sum_of_values = sum(color_dict[color] * freq for color, freq in color_freq.items())

# Calculate the mean color
mean_color = sum_of_values / total_freq

# Find the name of the color with the closest numerical value to the mean color
closest_color = min(color_dict, key=lambda x: abs(color_dict[x]-mean_color))

print("The mean color is:", closest_color)