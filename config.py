BACKGROUND = (0, 0, 0)

# Structure - probability: {rarity info}
rarities = {
    0.00001: {
        "name": "❻⟕ⰰ♳⎞⫷ⵓ⻀⿕⋝",
        "size": range(26, 39),
        "pixel_probability": range(12, 20),
        "color_deviation": range(120, 141),
    },  

    0.0001: {
        "name": "Exceptional",
        "size": range(20, 27),
        "pixel_probability": range(15, 30),
        "color_deviation": range(85, 111),
    },

    0.001: {
        "name": "Exotic",
        "size": [18, 19, 20],
        "pixel_probability": range(18, 32),
        "color_deviation": range(65, 85),
    },

    0.01: {
        "name": "Arcane",
        "size": [16, 17],
        "pixel_probability": range(20, 29),
        "color_deviation": range(63, 79),
    },


    0.1: {
        "name": "Legendary",
        "size": [14, 15],
        "pixel_probability": range(24, 28),
        "color_deviation": range(55, 70),
    },

    1: {
        "name": "Mythic",
        "size": [12, 13],
        "pixel_probability": range(26, 30),
        "color_deviation": range(49, 60),
    },

    5: {
        "name": "Epic",
        "size": [10, 11],
        "pixel_probability": range(28, 35),
        "color_deviation": range(40, 51),
    },

    10: {
        "name": "Rare",
        "size": [8, 9],
        "pixel_probability": range(30, 37),
        "color_deviation": range(28, 47),
    },

    50: {
        "name": "Uncommon",
        "size": [6, 7],
        "pixel_probability": range(36, 47),
        "color_deviation": range(20, 30),
    },

    100: {
        "name": "Common",
        "size": [4, 5],
        "pixel_probability": range(40, 56),
        "color_deviation": range(10, 21),
    }
}
