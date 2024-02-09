import turtle


def draw_pifagor_tree(t, branch_length, level):
    if level == 0:
        return
    t.forward(branch_length * level)
    t.right(45)
    draw_pifagor_tree(t, branch_length, level-1)
    t.left(90)
    draw_pifagor_tree(t, branch_length, level-1)
    t.right(45)
    t.backward(branch_length * level)


def main():
    level = int(input("Введіть рівень рекурсії: "))

    screen = turtle.Screen()

    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    t.color("green")

    t.setheading(90)
    t.penup()
    t.goto(0, -200)
    t.pendown()

    draw_pifagor_tree(t, 10, level)

    screen.mainloop()


if __name__ == "__main__":
    main()
