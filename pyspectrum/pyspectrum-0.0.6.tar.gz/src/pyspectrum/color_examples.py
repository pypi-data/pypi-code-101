import pyspectrum

c = pyspectrum.Colors()
redRGB = c.RGB(255, 0, 0)
redHex = c.Hexadecimal("#ff0000")
redCMYK = c.CMYK(0, 100, 100, 0)
print(f"Red RGB tuple: {redRGB.to_tuple()}")
print(f"Red Hex code: {redHex.to_string()}")
print(f"Red CMYK tuple: {redCMYK.to_tuple()}")
print(f"Red Hex converted to RGB: {redHex.to_rgb().to_tuple()}")
print(f"Red CMYK converted to RGB: {redCMYK.to_rgb().to_tuple()}")
print(f"Red RGB converted to Hex: {redRGB.to_hex().to_string()}")