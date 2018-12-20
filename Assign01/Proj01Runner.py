import turtle


class Runner(object):
   
       
   @classmethod
   def run(self, aTuple):

       prueba = aTuple[0]
       prueba.shape("turtle")
       prueba.pensize(2) 
       prueba.color('red')
       prueba.forward(0.5)

       prueba1 = aTuple[1]
       prueba1.pensize(3)
       prueba1.shape('circle')
       prueba1.color('dark green')

       prueba2 = aTuple[2]
       prueba2.pensize(4)
       prueba2.shape('triangle') 
       prueba2.color('blue') 

       
       return [aTuple[0],aTuple[1],aTuple[2],"Daniel E. Mendoza Pupo"]

        
        #Code in body of method omitted.
        #Required code to be inserted by students
    #end run
#end class Runner
