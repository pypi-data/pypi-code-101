from shapes import Rectangle
from link import Link
from canvas import Canvas
from server import svg_server

canvas = Canvas(500, 500)
link = Link("Something", "https://google.com", canvas)
rect = Rectangle(100, 200, link)
svg_server(canvas)

