from tkinter import *

root = Tk()
#w = Label(root, text="Hello Daniel!")
#w.pack()
root.config(bg = "blue")# le da color al fondo de pantalla
root.geometry("500x500")#cambia tamano de ventana
def mostrar(ventana):ventana.deiconify()
def ocultar(ventana):ventana.withdraw()
def ejecutar(f):root.after(200,f)
#METODO PACK()
#b1 = Button(root,text="Abrir ventana V1")#primer boton
#b1.pack()#el boton es cargado
#b1=Button(root,text="ABRIR VENTANA V1").pack()

#METODO GRID()
#b1=Button(root,text="ABRIR VENTANA V1")#primer boton
#b1.grid(row=10,column=10)#El boton es cargado
b1=Button(root,text="abrir ventana v1").grid(row=1,column=1)#El boton es cargado

v1 = Toplevel(root)#crea una nueva ventana hija de la ventana principal
v1.withdraw() # oculta v1
root.mainloop()

#Toplevel: Crea una nueva ventana
#Frame: Coloca los páneles para ordenar los elementos
#Canvas: Para dibujar y graficar funciones etc..
#Button: Para colocar un botón
#Label: Coloca un texto
#Message: Coloca un texto
#Entry: Coloca una entrada de texto de una linea
#Text: Coloca una entrada de texto de varias lineas
#Listbox: Coloca una lista con elementos clickeables
#Menú: Coloca un menú que puede contener cascadas y elementos clickeables
