def lindenmayer_turtle(string, step_size, turtle, angle=90):
    for step in string:
        if step == 'F':
            turtle.go_forward(step_size)
        if step == '-':
            turtle.turn_left(angle)
        if step == '+':
            turtle.turn_left(-angle)
    return turtle
