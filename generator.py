import random

def generate_name():
    prefixes = ["Dark", "Fire", "Ice", "Shadow"]
    suffixes = ["blade", "storm", "fang", "heart"]
    return random.choice(prefixes) + random.choice(suffixes)