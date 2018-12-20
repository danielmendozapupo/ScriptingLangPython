import turtle


class Runner(object):

    pruebaRandom = []    

    def __init__(self, turt_value):

        self.pruebaRandom.append(turt_value)

    def run(self):

        prueba = turtle.Turtle("turtle")
        prueba.pensize(5)
        #prueba.color("red")
        return self.pruebaRandom[1], prueba, 'Daniel Mendoza'
