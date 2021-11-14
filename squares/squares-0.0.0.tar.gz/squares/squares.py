from PIL import Image, ImageDraw
from hashlib import sha1

def _square(image, x, y, block, pad):
    x = x * block + pad
    y = y * block + pad

    image = ImageDraw.Draw(image)
    image.rectangle((x, y, x + block, y + block), fill="#ffffff")

def generate(seed, width=512, pad=0.1):
    """ Generates an identicon using the provided seed.

    :param seed: (str) the base used for generating the identicon
    :param width: (int, opt) the width of the image in pixels
    :param pad: (int, opt) distance b/w sprite and image boundary

    :return: PIL.Image object """

    if pad <= 0.0 or pad > 1.0:
        raise ValueError("0.0 < pad <= 1.0 only")

    seed = sha1(seed.encode()).hexdigest()[-15:]

    p = int(width * pad)
    b = (width - 2 * p) // 5
    w = b * 5 + 2 * p

    luminosity = 40 + int(seed[0], 16)
    hue = int(seed[-6:], 16) / 0xffffff * 360
    hsl = "hsl(%d, 80%%, %d%%)" % (hue, luminosity)
    
    image = Image.new("RGB", (w, w), hsl)
    colored = []

    for i, v in enumerate(seed):
        yes = ord(v) % 2 != 0
        colored.append(yes)

        if yes and i < 10:
            _square(image, i // 5, i % 5, b, p)
            _square(image, 4 - i // 5, i % 5, b, p)
        elif yes:
            _square(image, i // 5, i - 10, b, p)

    if all(colored) or not any(colored):
        return generate(seed, b, p)
    
    return image

if __name__ == "__main__":
	import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument("seed", nargs="?")
    parser.add_argument("-s", "--save", help="confirm save", action="store_true")
    parser.add_argument("-v", "--view", action="store_true")
    
    args = parser.parse_args()

    if args.seed == None:
        args.seed = input("Enter seed: ")

    image = generate(args.seed.strip())

    if args.view:
        image.show()
    
    if args.save or input("save (y/N): ").lower() == "y":
        image.save(f"{args.seed}.png")
