__author__ = 'Goose V'
__email__ = '82774618+GooseterV@users.noreply.github.com'
__version__ = '0.0.6'

class Colors:
	class Errors:
		class InvalidHex(Exception):
			def __init__(self, hexCode):
				self.hex = hexCode
				self.message = f"Invalid hexadecimal code. {hexCode} is not formatted #xxxxxx (x; 0-9, aA-fF)"
				super().__init__(self.message)
			pass
		class InvalidNumberRange(Exception):
			def __init__(self):
				self.message = f"Invalid color number(s). Make sure the number is in the correct range! (CMYK; 0-100 RGB; 0-255)"
				super().__init__(self.message)
			pass
		class InvalidColorName(Exception):
			def __init__(self):
				self.message = f"Invalid color name. Make sure the name is a TRUE html/css color."
				super().__init__(self.message)
			pass
	class RGB:
		"""
		Create an `RGB` color object out of r, g, and b.

		r, g, b must be in `range(0, 255)`

		Parameters:
			r:int - the red value for the color
			g:int - the green value for the color
			b:int - the blue value for the color
		Returns:
			an RGB color object
		Raises:
			`InvalidNumberRange`; if any of the color values is less than 0 or greater than 255
		"""
		def __init__(self, r, g, b):
			if any(n for n in (r, g, b) if n > 255 or n < 0):
				raise Colors.Errors.InvalidNumberRange()
			self._red = r
			self._green = g
			self._blue = b
		def to_tuple(self):
			"""
			Converts the RGB color into a tuple containing the three values; red, green, and blue.
			
			Parameters:
				`none`
			Returns:
				a tuple of the values; (r, g, b)
			"""
			return (self._red, self._green, self._blue)
		def print_color(self):
			"""
			Prints the color in rgb form, colored that same color.
			
			Parameters:
				`none`
			Returns:
				`none`
			"""
			print(f"\033[38;2;{self._red};{self._green};{self._blue}mrgb{self.to_tuple()}\033[0m")
		def to_hex(self):
			"""
			Converts the RGB color into a hexadecimal color 
			
			Parameters:
				`none`
			Returns:
				an `Hexadecimal` color object		
			"""
			return Colors.Hexadecimal(f"#{self._red:02x}{self._green:02x}{self._blue:02x}")
		def to_cmyk(self):
			"""
			Converts the RGB color into a CMYK color 
			
			Parameters:
				`none`
			Returns:
				an `CMYK` color object		
			"""
			c, m, y = 1 - self._red / 255, 1 - self._green / 255, 1 - self._blue / 255
			c, m, y = (c - min(c, m, y)) / (1 - min(c, m, y)), (m - min(c, m, y)) / (1 - min(c, m, y)), (y - min(c, m, y)) / (1 - min(c, m, y))
			k = min(c, m, y)
			return Colors.CMYK(int(c * 100), int(m * 100), int(y * 100), int(k * 100))

	class Hexadecimal:
		"""
		Create a Hexadecimal color object from a string

		`hex_string` must be formatted `#xxxxxx`, where x is a hexadecimal character from 0-F

		Parameters:
			hex_string:str - a hexadecimal string
		Returns:
			a `Hexadecimal` color obkect
		Raises:
			`InvalidHex`; if the string is not formatted properly or has non-hexadecimal characters
		"""
		def __init__(self, hex_string:str):
			if "#" not in hex_string or len(hex_string) < 7 or any(c not in "0123456789abcdefABCDEF#" for c in set(hex_string)):
				raise Colors.Errors.InvalidHex(hex_string)
			self._hex_string = hex_string.replace("#", "").lower()
		def to_rgb(self):
			"""
			Converts the hex color into an RGB color 
			
			Parameters:
				`none`
			Returns:
				an `RGB` color object		
			"""
			return Colors.RGB(int(self._hex_string[0:2], 16), int(self._hex_string[2:4], 16), int(self._hex_string[4:6], 16))
		def to_string(self):
			"""
			Converts the Hexadecimal color into a string formatted `#xxxxxx`
			
			Parameters:
				`none`
			Returns:
				a hexadecimal string
			"""
			return f"#{self._hex_string}"
		
	class CMYK:
		"""
		Create a CMYK color object out of c, m, y, and k

		c, m, y, k must be in `range(0, 100)`

		Parameters:
			c:int - the cyan value for the color
			m:int - the magenta value for the color
			y:int - the yellow value for the color
			k:int - the black value for the color
		Returns:
			a CMYK color object
		Raises:
			`InvalidNumberRange`; if any of the color values is less than 0 or greater than 100
		"""
		def __init__(self, c, m, y, k):
			self._cyan = c
			self._magenta = m
			self._yellow = y
			self._black = k
		def to_tuple(self):
			"""
			Converts the CMYK color into a tuple containing the four values; cyan, magenta, yellow, black.
			
			Parameters:
				`none`
			Returns:
				a tuple of the values; (c, m, y, k)
			"""
			return (self._cyan, self._magenta, self._yellow, self._black)
		def to_rgb(self):
			"""
			Converts the CMYK color into an RGB color 
			
			Parameters:
				`none`
			Returns:
				an `RGB` color object		
			"""
			return Colors.RGB(int(255*(1.0-(self._cyan+self._black)/100)), int(255*(1.0-(self._magenta+self._black)/100)), int(255*(1.0-(self._yellow+self._black)/100)))
	def __init__(self):
		self._color_names = {
		"aliceblue": "f0f8ff",   
		"antiquewhite": "faebd7",
		"aqua": "00ffff",        
		"aquamarine": "7fffd4",  
		"azure": "f0ffff",       
		"beige": "f5f5dc",       
		"bisque": "ffe4c4",      
		"black": "000000",       
		"blanchedalmond": "ffebcd",
		"blue": "0000ff",
		"blueviolet": "8a2be2",
		"brown": "a52a2a",
		"burlywood": "deb887",
		"cadetblue": "5f9ea0",
		"chartreuse": "7fff00",
		"chocolate": "d2691e",
		"coral": "ff7f50",
		"cornflowerblue": "6495ed",
		"cornsilk": "fff8dc",
		"crimson": "dc143c",
		"cyan": "00ffff",
		"darkblue": "00008b",
		"darkcyan": "008b8b",
		"darkgoldenrod": "b8860b",
		"darkgray": "a9a9a9",
		"darkgrey": "a9a9a9",
		"darkgreen": "006400",
		"darkkhaki": "bdb76b",
		"darkmagenta": "8b008b",
		"darkolivegreen": "556b2f",
		"darkorange": "ff8c00",
		"darkorchid": "9932cc",
		"darkred": "8b0000",
		"darksalmon": "e9967a",
		"darkseagreen": "8fbc8f",
		"darkslateblue": "483d8b",
		"darkslategray": "2f4f4f",
		"darkslategrey": "2f4f4f",
		"darkturquoise": "00ced1",
		"darkviolet": "9400d3",
		"deeppink": "ff1493",
		"deepskyblue": "00bfff",
		"dimgray": "696969",
		"dimgrey": "696969",
		"dodgerblue": "1e90ff",
		"firebrick": "b22222",
		"floralwhite": "fffaf0",
		"forestgreen": "228b22",
		"fuchsia": "ff00ff",
		"gainsboro": "dcdcdc",
		"ghostwhite": "f8f8ff",
		"gold": "ffd700",
		"goldenrod": "daa520",
		"gray": "808080",
		"grey": "808080",
		"green": "008000",
		"greenyellow": "adff2f",
		"honeydew": "f0fff0",
		"hotpink": "ff69b4",
		"indianred": "cd5c5c",
		"indigo": "4b0082",
		"ivory": "fffff0",
		"khaki": "f0e68c",
		"lavender": "e6e6fa",
		"lavenderblush": "fff0f5",
		"lawngreen": "7cfc00",
		"lemonchiffon": "fffacd",
		"lightblue": "add8e6",
		"lightcoral": "f08080",
		"lightcyan": "e0ffff",
		"lightgoldenrodyellow": "fafad2",
		"lightgray": "d3d3d3",
		"lightgrey": "d3d3d3",
		"lightgreen": "90ee90",
		"lightpink": "ffb6c1",
		"lightsalmon": "ffa07a",
		"lightseagreen": "20b2aa",
		"lightskyblue": "87cefa",
		"lightslategray": "778899",
		"lightslategrey": "778899",
		"lightsteelblue": "b0c4de",
		"lightyellow": "ffffe0",
		"lime": "00ff00",
		"limegreen": "32cd32",
		"linen": "faf0e6",
		"magenta": "ff00ff",
		"maroon": "800000",
		"mediumaquamarine": "66cdaa",
		"mediumblue": "0000cd",
		"mediumorchid": "ba55d3",
		"mediumpurple": "9370db",
		"mediumseagreen": "3cb371",
		"mediumslateblue": "7b68ee",
		"mediumspringgreen": "00fa9a",
		"mediumturquoise": "48d1cc",
		"mediumvioletred": "c71585",
		"midnightblue": "191970",
		"mintcream": "f5fffa",
		"mistyrose": "ffe4e1",
		"moccasin": "ffe4b5",
		"navajowhite": "ffdead",
		"navy": "000080",
		"oldlace": "fdf5e6",
		"olive": "808000",
		"olivedrab": "6b8e23",
		"orange": "ffa500",
		"orangered": "ff4500",
		"orchid": "da70d6",
		"palegoldenrod": "eee8aa",
		"palegreen": "98fb98",
		"paleturquoise": "afeeee",
		"palevioletred": "db7093",
		"papayawhip": "ffefd5",
		"peachpuff": "ffdab9",
		"peru": "cd853f",
		"pink": "ffc0cb",
		"plum": "dda0dd",
		"powderblue": "b0e0e6",
		"purple": "800080",
		"rebeccapurple": "663399",
		"red": "ff0000",
		"rosybrown": "bc8f8f",
		"royalblue": "4169e1",
		"saddlebrown": "8b4513",
		"salmon": "fa8072",
		"sandybrown": "f4a460",
		"seagreen": "2e8b57",
		"seashell": "fff5ee",
		"sienna": "a0522d",
		"silver": "c0c0c0",
		"skyblue": "87ceeb",
		"slateblue": "6a5acd",
		"slategray": "708090",
		"slategrey": "708090",
		"snow": "fffafa",
		"springgreen": "00ff7f",
		"steelblue": "4682b4",
		"tan": "d2b48c",
		"teal": "008080",
		"thistle": "d8bfd8",
		"tomato": "ff6347",
		"turquoise": "40e0d0",
		"violet": "ee82ee",
		"wheat": "f5deb3",
		"white": "ffffff",
		"whitesmoke": "f5f5f5",
		"yellow": "ffff00",
		"yellowgreen": "9acd32"
	}
	def from_name(self, colorName:str):
		"""
		Get an RGB color from a web color name; `red`, `seagreen`, `chartreuse`

		Parameters:
			colorName:str - html/css color name
		Returns:
			rgbColor - an `RGB` object from the color
		Raises:
			`InvalidColorName`; if the designated color literal is not an HTML/CSS color.
		"""
		if colorName not in self._color_names.keys():
			raise Colors.Errors.InvalidColorName()
		return Colors.Hexadecimal(f"#{self._color_names[colorName]}").to_rgb()
	def color_text(self, text:str, color:RGB):
		"""
		Colors a string with the color of `color` 

		Parameters:
			text:str - the string you want to color
			color:RGB - the color you want the text to be
		Returns:
			coloredText - the colored string, when printing will show up colored
		"""
		return f"\033[38;2;{color._red};{color._green};{color._blue}m{text}\033[0m"
