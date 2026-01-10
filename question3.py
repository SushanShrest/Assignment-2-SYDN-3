import turtle

def draw_edge(length, depth):
    if depth == 0:
        turtle.forward(length)
        return
    segment = length / 3

    draw_edge(segment, depth - 1)
    turtle.left(60)
    draw_edge(segment, depth - 1) 
    turtle.right(120)
    draw_edge(segment, depth - 1)
    turtle.left(60)
    draw_edge(segment, depth - 1)