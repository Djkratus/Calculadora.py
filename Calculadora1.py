from tkinter import *
from tkinter import ttk
import math

#las casas
def clase():
    pass
def clase2():
    pass
def TemaOscuro(*args): #Creamos el tema oscuro
    
    estilos.configure('mainframe.TFrame', background="#363636")

    estilos_label1.configure('Label1.TLabel',background="#363636", foreground="White")
    estilos_label2.configure('Label2.TLabel',background="#363636", foreground="White")

    estilos_botones_numeros.configure('Botones_numeros.TButton',background="#282828", foreground="White")
    estilos_botones_numeros.map('Botones_numeros.TButton.focus',
                                background=[{'active', '#1E1E1E'}])

    estilos_botones_borrar.configure('Botones_borrar.TButton',background="#282828", foreground="White")
    estilos_botones_borrar.map('Botones_borrar.TButton',
                                background=[{'active', '#1E1E1E'}])
    
    estilos_botones_restantes.configure('Botones_restantes.TButton',background="#282828", foreground="White")
    estilos_botones_restantes.map('Botones_restantes.TButton',
                                  background=[{'active', '#1E1E1E'}])

def TemaClaro(*args): #Creamos el tema claro
    
    
    estilos.configure('mainframe.TFrame', background="#ECECEC")

    estilos_label1.configure('Label1.TLabel',background="#ECECEC", foreground="Black")
    estilos_label2.configure('Label2.TLabel',background="#ECECEC", foreground="Black")

    estilos_botones_numeros.configure('Botones_numeros.TButton',background="#F0F0F0", foreground="Black")
    estilos_botones_numeros.map('Botones_numeros.TButton.focus',
                                background=[{'active', '#D3D3D3'}])

    estilos_botones_borrar.configure('Botones_borrar.TButton',background="#F0F0F0", foreground="Black")
    estilos_botones_borrar.map('Botones_borrar.TButton',
                                background=[{'active', '#D3D3D3'}])
    
    estilos_botones_restantes.configure('Botones_restantes.TButton',background="#F0F0F0", foreground="Black")
    estilos_botones_restantes.map('Botones_restantes.TButton',
                                  background=[{'active', '#D3D3D3'}])

      
    #ahora creremos el metodo por teclado al final

def IngresarVAlores(tecla):
    if tecla >= '0' and tecla <= '9' or tecla =='(' or tecla ==')' or tecla =='.':
        entrada2.set(entrada2.get()+tecla)
    
    if tecla == '*' or tecla == '/' or tecla == '+' or tecla == '-':
        if tecla == '*':
            entrada1.set(entrada2.get()+'*')
        elif tecla == '/':
            entrada1.set(entrada2.get()+'/')
        elif tecla == '+':
            entrada1.set(entrada2.get()+'+')
        elif tecla == '-':
            entrada1.set(entrada2.get()+'-') #El set es para asignar un valor y el get es para obtenerlo

        entrada2.set('')
        #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    if tecla == '=':
        resultado = str(eval(entrada1.get() + entrada2.get()))
        entrada1.set('')
        entrada2.set(resultado)

def IngresarVAloresTeclado(event):
    tecla =event.char

    if tecla >= '0' and tecla <= '9' or tecla =='(' or tecla ==')' or tecla =='.':
        entrada2.set(entrada2.get()+tecla)
    
    if tecla == '*' or tecla == '/' or tecla == '+' or tecla == '-':
        if tecla == '*':
            entrada1.set(entrada2.get()+'*')
        elif tecla == '/':
            entrada1.set(entrada2.get()+'/')
        elif tecla == '+':
            entrada1.set(entrada2.get()+'+')
        elif tecla == '-':
            entrada1.set(entrada2.get()+'-') #El set es para asignar un valor y el get es para obtenerlo

        entrada2.set('')
        
    if tecla == '=':
        resultado = str(eval(entrada1.get() + entrada2.get()))
        entrada1.set('')
        entrada2.set(resultado)

def raizCuadrada(): 
    entrada1.set('')
    resultado = math.sqrt(float(entrada2.get()))
    entrada2.set(resultado) 

def borrar(*args):
    inicio = 0
    final = len(entrada2.get())

    entrada2.set(entrada2.get()[inicio:final-1])

def borrar_todo(*args):
    entrada1.set('')
    entrada2.set('')
    

root = Tk() #Ventana raiz
root.title("Calculadora") #Asignamos el titulo 
root.geometry("+500+80") # Esto indica la cordenada donde va a salir 
root.columnconfigure( 0, weight=1)  #Ahora se configura las columnas para que la ventana sea adaptable al cambiar de tamaño la ventana
root.rowconfigure(0,weight=1) #Ahora se configuran las filas  

    #Despue de crear todo los botones le daremos estilo 
estilos = ttk.Style()
estilos.theme_use("clam")
estilos.configure('mainframe.TFrame', background="DBDBDB")

mainframe = ttk.Frame(root, style="mainframe.TFrame") #Aqui se va a ver reflejado el estilo que se coloco en la fila 11,12
mainframe = ttk.Frame(root)
mainframe.grid(column=0,row=0, sticky=(W,N,E,S)) #ADAPTABILIDAD DE LAS FILAS Y COLIMNAS
mainframe.columnconfigure( 0, weight=1)
mainframe.columnconfigure( 1, weight=1)
mainframe.columnconfigure( 2, weight=1)
mainframe.columnconfigure( 3, weight=1)

mainframe.rowconfigure(0,weight=1)
mainframe.rowconfigure(1,weight=2)
mainframe.rowconfigure(2,weight=1)
mainframe.rowconfigure(3,weight=1)
mainframe.rowconfigure(4,weight=1)
mainframe.rowconfigure(5,weight=1)
mainframe.rowconfigure(6,weight=1)
mainframe.rowconfigure(7,weight=1)

#Los label que en español significa etiquetas, son widget o componentes de python que permite agregar texto.
#le damos estilo a los label 
estilos_label1 = ttk.Style()
estilos_label1.configure('label.TLabel', font="arial 15", anchor = "e")

estilos_label2 = ttk.Style()
estilos_label2.configure('Label2.TLabel', font="arial 40", anchor = "e") 

entrada1= StringVar() #Va a estar vinculada label_entrada1 
label_entrada1 = ttk.Label(mainframe, textvariable=entrada1, style="label.TLabel") #Label va a vivir en mainframe
label_entrada1.grid(column=0,row=0, columnspan=4, sticky=(W,N,E,S))

entrada2 = StringVar()
label_entrada2 = ttk.Label(mainframe, textvariable=entrada2, style="Label2.TLabel")
label_entrada2.grid(column=0,row=1,columnspan=4, sticky=(W,N,E,S))

#Ahora creamos los botones de los numeros

estilos_botones_numeros = ttk.Style()
estilos_botones_numeros.configure('Botones_numeros.TButton', font="arial 22", Widget=5, background="#FFFFFF", relief="flat")
estilos_botones_numeros.map('Botones_numeros.TButton', #Cramos un diccionario
                           foreground=[('active', '#6347c9')],
                           background=[('active', '#FF0000')])

estilos_botones_borrar = ttk.Style()
estilos_botones_borrar.configure('Botones_borrar.TButton',font="arial 22", width=5, relief="flat", background="#CECECE")
estilos_botones_borrar.map('Botones_borrar.TButton',
                           foreground=[('active', '#6347c9')],
                           background=[('active', '#FF0000')])

estilos_botones_restantes = ttk.Style()
estilos_botones_restantes.configure('Botones_restantes.TButton',font="arial 22", widh=5, relief = "flat", background="#CECECE")
estilos_botones_restantes.map('Botones_restantes.TButton',
                           foreground=[('active', '#6347c9')],
                           background=[('active', '#FF0000')])


button0 = ttk.Button(mainframe,text=0, style="Botones_numeros.TButton",command=lambda:IngresarVAlores('0')) 
button1 = ttk.Button(mainframe,text=1, style="Botones_numeros.TButton",command=lambda:IngresarVAlores('1'))
button2 = ttk.Button(mainframe,text=2, style="Botones_numeros.TButton",command=lambda:IngresarVAlores('2')) 
button3 = ttk.Button(mainframe,text=3, style="Botones_numeros.TButton",command=lambda:IngresarVAlores('3'))
button4 = ttk.Button(mainframe,text=4, style="Botones_numeros.TButton",command=lambda:IngresarVAlores('4'))
button5 = ttk.Button(mainframe,text=5, style="Botones_numeros.TButton",command=lambda:IngresarVAlores('5'))
button6 = ttk.Button(mainframe,text=6, style="Botones_numeros.TButton",command=lambda:IngresarVAlores('6'))
button7 = ttk.Button(mainframe,text=7, style="Botones_numeros.TButton",command=lambda:IngresarVAlores('7'))
button8 = ttk.Button(mainframe,text=8, style="Botones_numeros.TButton",command=lambda:IngresarVAlores('8'))
button9 = ttk.Button(mainframe,text=9, style="Botones_numeros.TButton",command=lambda:IngresarVAlores('9'))

#Creamos ahora los botones de borrrar, parentesis, etc

button_borrar = ttk.Button(mainframe, text=chr(9003), style="Botones_borrar.TButton",command=lambda:borrar()) #Se usa el caracter 9003 el cual es el simbolo de borrar
button_borrar_todo = ttk.Button(mainframe,text="C",style="Botones_borrar.TButton",command=lambda:borrar_todo())
button_parentesis_izq = ttk.Button(mainframe,text="(",style="Botones_restantes.TButton",command=lambda:IngresarVAlores('('))
button_parentesis_der = ttk.Button(mainframe,text=")",style="Botones_restantes.TButton",command=lambda:IngresarVAlores(')'))
button_punto = ttk.Button(mainframe,text=".",style="Botones_restantes.TButton",command=lambda:IngresarVAlores('.'))

#Ahora se crean los botones de =, raiz cuadrada, etc

button_division = ttk.Button(mainframe,text=chr(247),style="Botones_restantes.TButton",command=lambda:IngresarVAlores('/'))
button_multiplicacion = ttk.Button(mainframe,text="x",style="Botones_restantes.TButton",command=lambda:IngresarVAlores('*'))
button_restar = ttk.Button(mainframe,text="-",style="Botones_restantes.TButton",command=lambda:IngresarVAlores('-'))
button_suma = ttk.Button(mainframe,text="+",style="Botones_restantes.TButton",command=lambda:IngresarVAlores('+'))
button_igual = ttk.Button(mainframe,text="=",style="Botones_restantes.TButton",command=lambda:IngresarVAlores('='))
button_raiz_cuadrada = ttk.Button(mainframe,text="√",style="Botones_restantes.TButton",command=lambda: raizCuadrada())

#Colocar botones en pantalla 


button_parentesis_izq.grid(column=0, row=2, sticky=(W,N,E,S))
button_parentesis_der.grid(column=1,row=2, sticky=(W,N,E,S))
button_borrar_todo.grid(column=2,row=2,columnspan=1,  sticky=(W,N,E,S))
button_borrar.grid(column=3,row=2,columnspan=1, sticky=(W,N,E,S))

button7.grid(column=0,row=3, sticky=(W,N,E,S))
button8.grid(column=1,row=3, sticky=(W,N,E,S))
button9.grid(column=2,row=3, sticky=(W,N,E,S))
button_division.grid(column=3, row=3, sticky=(W,N,E,S))

button4.grid(column=0,row=4, sticky=(W,N,E,S))
button5.grid(column=1,row=4, sticky=(W,N,E,S))
button6.grid(column=2,row=4, sticky=(W,N,E,S))
button_multiplicacion.grid(column=3,row=4, sticky=(W,N,E,S))

button1.grid(column=0,row=5, sticky=(W,N,E,S))
button2.grid(column=1,row=5, sticky=(W,N,E,S))
button3.grid(column=2,row=5, sticky=(W,N,E,S))
button_suma.grid(column=3,row=5, sticky=(W,N,E,S))

button0.grid(column=0,row=6, columnspan=2, sticky=(W,N,E,S)) #sticky y columnspa es la cantidad de columnas que va a ocupar
button_punto.grid(column=2,row=6, sticky=(W,N,E,S))
button_restar.grid(column=3,row=6, sticky=(W,N,E,S))

button_igual.grid(column=0,row=7, columnspan=3, sticky=(W,N,E,S))
button_raiz_cuadrada.grid(column=3,row=7, sticky=(W,N,E,S))

for i in mainframe.winfo_children():
    i.grid_configure(ipady=10, padx=1, pady=1)

root.bind('<KeyPress-o>', TemaOscuro)
root.bind('<KeyPress-c>', TemaClaro)
root.bind('<Key>',IngresarVAloresTeclado)
root.bind('<KeyPress-b>',borrar)
root.bind('<KeyPress-v>',borrar_todo)
root.bind('<key')

root.mainloop()




