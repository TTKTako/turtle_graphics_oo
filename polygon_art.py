import turtle
import random

class drawPic:
    def __init__(self):
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)

    def draw_polygon(self, num_sides, size, orientation, location, color, border_size):
        turtle.penup()
        turtle.goto(location[0], location[1])
        turtle.setheading(orientation)
        turtle.color(color)
        turtle.pensize(border_size)
        turtle.pendown()
        for _ in range(num_sides):
            turtle.forward(size)
            turtle.left(360/num_sides)
        turtle.penup()

    def get_new_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw_sub(self, num_sides, size, orientation, location, color, border_size):
        # specify a reduction ratio to draw a smaller polygon inside the one above
        reduction_ratio = 0.618
        # reposition the turtle and get a new location
        turtle.penup()
        turtle.forward(size*(1-reduction_ratio)/2)
        turtle.left(90)
        turtle.forward(size*(1-reduction_ratio)/2)
        turtle.right(90)
        location[0] = turtle.pos()[0]
        location[1] = turtle.pos()[1]
        # adjust the size according to the reduction ratio
        size *= reduction_ratio
        # draw the second polygon embedded inside the original
        self.draw_polygon(num_sides, size, orientation, location, color, border_size)



print("Which art do you want to generate? Enter a number between 1 to 9")
a = int(input("inclusive: "))

draw = drawPic()

if a == 1:
    for i in range(20):
        num_sides = 3
        border_size = random.randint(1, 7)
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = draw.get_new_color()
        draw.draw_polygon(num_sides, size, orientation, location, color, border_size)
elif a == 2:
    for i in range(20):
        num_sides = 4
        border_size = random.randint(1, 7)
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = draw.get_new_color()
        draw.draw_polygon(num_sides, size, orientation, location, color, border_size)
elif a == 3:
    for i in range(20):
        num_sides = 5
        border_size = random.randint(1, 7)
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = draw.get_new_color()
        draw.draw_polygon(num_sides, size, orientation, location, color, border_size)
elif a == 4:
    for i in range(20):
        num_sides = random.randint(3, 5)
        border_size = random.randint(1, 7)
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = draw.get_new_color()
        draw.draw_polygon(num_sides, size, orientation, location, color, border_size)
elif a == 5:
    for i in range(20):
        num_sides = 3
        border_size = random.randint(1, 7)
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = draw.get_new_color()
        draw.draw_polygon(num_sides, size, orientation, location, color, border_size)
        for i in range(random.randint(2,3)):
            draw.draw_sub(num_sides, size/((i/2)+1), orientation, location, color, border_size)
elif a == 6:
    for i in range(20):
        num_sides = 4
        border_size = random.randint(1, 7)
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = draw.get_new_color()
        draw.draw_polygon(num_sides, size, orientation, location, color, border_size)
        for i in range(random.randint(2,3)):
            draw.draw_sub(num_sides, size/((i/2)+1), orientation, location, color, border_size)
elif a == 7:
    for i in range(20):
        num_sides = 5
        border_size = random.randint(1, 7)
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = draw.get_new_color()
        draw.draw_polygon(num_sides, size, orientation, location, color, border_size)
        for i in range(random.randint(2,3)):
            draw.draw_sub(num_sides, size/((i/2)+1), orientation, location, color, border_size)
elif a == 8:
    for i in range(20):
        num_sides = random.randint(3, 5)
        border_size = random.randint(1, 7)
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = draw.get_new_color()
        draw.draw_polygon(num_sides, size, orientation, location, color, border_size)
        for i in range(random.randint(2,3)):
            draw.draw_sub(num_sides, size/((i/2)+1), orientation, location, color, border_size)
elif a == 9:
    for i in range(20):
        num_sides = random.randint(3, 5)
        border_size = random.randint(1, 7)
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = draw.get_new_color()
        draw.draw_polygon(num_sides, size, orientation, location, color, border_size)
        if bool(random.randint(0, 1)):
            for i in range(random.randint(2,3)):
                draw.draw_sub(num_sides, size/((i/2)+1), orientation, location, color, border_size)





# hold the window; close it by clicking the window close 'x' mark
turtle.done()