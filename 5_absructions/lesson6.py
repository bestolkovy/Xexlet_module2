import math


def make_point(x, y):
    return {
        "angle": math.atan2(y, x),
        "radius": math.sqrt((x ** 2) + (y ** 2)),
    }


# BEGIN (write your solution here)
def get_x(point):
    angle = point['angle']
    radius = point['radius']
    return radius * math.cos(angle)


def get_y(point):
    angle = point['angle']
    radius = point['radius']
    return radius * math.sin(angle)

# END
