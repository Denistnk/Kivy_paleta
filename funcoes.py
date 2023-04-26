from random import random
from kivy.utils import get_color_from_hex

def cores_aleatorias(end = 0xffffff):
    cor = get_color_from_hex('#%06X' % round(random() * end))
    return cor
