import turtle

# Draw one fractal edge
def draw_edge(length, depth):
    if depth == 0:
        turtle.forward(length)
        return
    segment = length / 3

    # Draw edge into three parts
    draw_edge(segment, depth - 1)
    turtle.left(60)
    draw_edge(segment, depth - 1) 
    turtle.right(120)
    draw_edge(segment, depth - 1)
    turtle.left(60)
    draw_edge(segment, depth - 1)

# Draw Polygons using fractal edges.
def draw_polygon(sides, length, depth):
   
    angle = 360 / sides

    for _ in range(sides):
        draw_edge(length, depth)
        turtle.left(angle)

# Main program 
def main():
    # Get user input
    sides = int(input("Enter the number of sides: "))
    length = int(input("Enter the side length: "))
    depth = int(input("Enter the recursion depth: "))

    # Turtle setup
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()

    # Position turtle
    turtle.goto(-length / 2, -length / 2.5)
    turtle.pendown()
    turtle.pencolor("black")

    # Draw Polygon
    draw_polygon(sides, length, depth)
    turtle.done()

main()