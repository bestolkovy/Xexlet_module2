# выдает ргб цвета по запросу цвета.

def rgb(red=0, green=0, blue=0):
    return f'rgb({red}, {green}, {blue})'


def get_colors():
    return {
                'red': rgb(red=255),
                'blue': rgb(blue=255),
                'green': rgb(green=255)
    }
