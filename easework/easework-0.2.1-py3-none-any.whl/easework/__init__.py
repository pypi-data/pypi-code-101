def add(num1 , num2):
	return num1 + num2

def substract(num1 , num2):
	return num1 - num2

def multiply(num1 , num2):
	return num1 * num2

def divide(num1, num2):
	return num1 / num2

def sq(num):
	return num * num 

def cb(num):
	return num * num * num 

def sqrt(num):
	return num ** 0.5 

def cbrt(num):
	return num ** 1/3

def area_sq(side):
	return side * side

def area_rect(length, width):
	return length * width 

def area_triangle(base, height):
	return 1/2 * base * height

def area_pgram(base, height):
	return base * height 

def area_kite(diag1, diag2):
	return 1/2 * diag1 * diag2

def area_quad(diag, h1, h2):
	return 1/2 * diag * h1 + h2

def area_trapzium(a, b, h):
	return 1/2 * a + b * h

def area_rhombus(diag1, diag2):
	return 1/2 * diag1 * diag2

def peri_sq(side):
	return 4 * side

def peri_rect(length, width):
	return 2 * length + width

def peri_pgram(b, h):
	return 2 * b * h

def peri_triangle(a, b, c):
	return a + b + c

def peri_kite(a, b): 
	return 2 * a + 2 * b
			
def peri_rhombus(side):
	return 4 * side

def peri_hexa(side):
	return 6 * side

def peri_trapzium(a, b, c, d):
	return a + b + c + d 

def peri_quad(a, b, c, d):
	return a + b + c + d 