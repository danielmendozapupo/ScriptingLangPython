import turtle


class Runner(object):


    def __init__(self, color):
        self.color = color
        self.color ="green"


    def run(self):

        prueba = turtle.Turtle("turtle")
        prueba.pensize(5)
        prueba.color("red")
        return self.color, prueba, 'Daniel Mendoza'
