import math 
def convert_to_16_9_resolution(x, y):
    new_x = x * (16/9)
    new_x = math.ceil(new_x)
    return (new_x, y)

def convert_to_4_3_resolution(x, y):
    new_x = x*4 / 3
    new_x = math.ceil(new_x)
    return (new_x, y)

import math

def convert_resolution(original_width, original_height, constant):
    # Calculate the aspect ratio as a floating-point number (16:9 => 16/9)
    aspect_ratio = 16 / 9

    if constant == "height":
        # Calculate new width while keeping the height constant
        new_width = round(original_height * aspect_ratio)
        return new_width, original_height

    elif constant == "width":
        # Calculate new height while keeping the width constant
        new_height = round(original_width / aspect_ratio)
        return original_width, new_height

    elif constant == "diagonal":
        # Calculate the diagonal using the Pythagorean theorem
        diagonal = math.sqrt(original_width**2 + original_height**2)

        # Calculate new dimensions while keeping the diagonal constant
        new_width = round(diagonal / math.sqrt(aspect_ratio**2 + 1))
        new_height = round(new_width / aspect_ratio)
        return new_width, new_height

    elif constant == "area":
        # Calculate the area of the original resolution
        original_area = original_width * original_height

        # Calculate new dimensions while keeping the area constant
        new_width = round(math.sqrt(original_area * aspect_ratio))
        new_height = round(new_width / aspect_ratio)
        return new_width, new_height

    else:
        raise ValueError("Invalid constant parameter. Please use 'height', 'width', 'diagonal', or 'area'.")

# Example usage:
original_width = 1280
original_height = 720
constant = "height"  # Choose 'height', 'width', 'diagonal', or 'area'
new_width, new_height = convert_resolution(original_width, original_height, constant)
print(f"Original resolution: {original_width}x{original_height}")
print(f"New resolution with constant {constant}: {new_width}x{new_height}")


