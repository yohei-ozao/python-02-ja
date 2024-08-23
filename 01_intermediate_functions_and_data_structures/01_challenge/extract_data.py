import re

def extract_data(text):
    pattern = r'\b\w+:\w+\b'
    matches = re.findall(pattern, text)
    return matches

def better_extract_data(text):
    pattern = r'\b(\w+):(\w+)\b'
    matches = re.findall(pattern, text)
    return matches