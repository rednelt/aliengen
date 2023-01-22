# Generates one randomized image of an alien, based on input
# ----------------------------------------------------------
from PIL import Image
from config import *

import random


def generate(filename="alien.png"):

    rarities_copy = rarities.copy()

    # Decide on a rarity based on the probabilities defined in config.py
    n = random.uniform(0, max(rarities_copy.keys()))
    for prob in sorted(rarities_copy.keys()):
        if n <= prob:
            rarity = rarities_copy[prob]
            break

    # Some stats may be a range
    for stat, value in rarity.items():
        if type(value) == list or type(value) == range:
            rarity[stat] = random.choice(list(value))

    # I want the image to be either 40x40 or 41x41 (some alien sizes are uneven)
    padding = (40 - rarity["size"]) // 2

    # Debug
    for stat, value in rarity.items():
        print(f"{stat}: {value}")

    # Create and draw the alien based on the rarity
    initial_color = tuple([random.randint(0, 255) for _ in range(3)])
    image = Image.new("RGB", (rarity["size"] + padding * 2, rarity["size"] + padding * 2), BACKGROUND)

    for i in range(padding, rarity["size"] + padding):
        for j in range(padding, rarity["size"] + padding):
            if random.randint(0, 100) < rarity["pixel_probability"]:
                color = tuple(map(lambda c:
                                  c + random.randint(-rarity["color_deviation"],
                                                     rarity["color_deviation"]),
                                  list(initial_color)))

                image.putpixel((i, j), color)
                image.putpixel((rarity["size"] - i + padding * 2 - 1, j), color)

    # Save the image
    image.save(filename)
    id = 0
    for i in range(0, image.height):
        for j in range(0, image.width):
            id += i + j
            id += sum(list(image.getpixel((i, j))))

    print(id)


generate(filename="alien.png")
