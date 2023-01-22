# aliengen
Generates low-res pixel art aliens, big and small, bland and colorful, common and exotic. Requires Pillow.
How to use: run `generator.py`, the image will be saved as alien.png. The stats of your alien (rarity name, size, pixel probability, color deviation) will be printed in the console. `config.py` contains a list of rarities, from Common to some random Unicode characters. Each rarity has it's own stats (a range of values for each characteristic, to make images more random). If you want to generate some high-rarity images, comment out the low rarities from `config.py`. Have fun.
