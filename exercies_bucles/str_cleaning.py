import re

def remove_random_numbers(text):
    # Use a regular expression to match and remove any sequences of digits
    cleaned_text = re.sub(r'\d+', '', text)
    return cleaned_text