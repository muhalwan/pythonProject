from turtle import *
from random import randint
from random import random

while True:
    up()
    goto(randint(-400, 400),
         randint(-400, 400))
    down()
    R = random()
    G = random()
    B = random()
    color(R, G, B)
    dot(randint(20, 80))
