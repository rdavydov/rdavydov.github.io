import re

# Constants for the maximum x and y values
MAX_SCREEN_WIDTH = 3840
MAX_SCREEN_HEIGHT = 2160

# Function to calculate scaling ratio
def calculate_ratio(max_value):
    return MAX_SCREEN_WIDTH / max_value if max_value < MAX_SCREEN_WIDTH else 1

# Function to replace the pixel values
def replace_px(match):
    x = int(match.group(1))
    y = int(match.group(2))

    # Scale x and y by the scaling ratio
    x = round(x * x_ratio)
    y = round(y * y_ratio)

    return f'{x}px {y}px'

# Read the CSS file
with open('style.css', 'r') as file:
    css_content = file.read()

# Find all x and y values
xy_values = re.findall(r'(\d+)px (\d+)px', css_content)

# Calculate the maximum x and y values
max_x = max(int(x) for x, y in xy_values)
max_y = max(int(y) for x, y in xy_values)

# Calculate the scaling ratios
x_ratio = calculate_ratio(max_x)
y_ratio = calculate_ratio(max_y)

# Replace the values
css_content = re.sub(r'(\d+)px (\d+)px', replace_px, css_content)

# Write the changes back to the CSS file
with open('style.css', 'w') as file:
    file.write(css_content)
