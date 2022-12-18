def is_in_figure(expression, x, y, object_x, object_y):
    x -= object_x
    y -= object_y
    return eval(expression, {"x" : x, "y" : y})
