import tkinter as Ventana #Colocar sobre-nombre 


class Formulario:
    def __init__(self):
        self.color = "rojo"
        self.entry_nombre = ""
        self.label_resultado = ""
        self.formulario = ""

    
    def iniciar_ventana(self):
        self.formulario = Ventana.Tk() # Widgets
        self.formulario.title("Registro de ususario")
        self.formulario.geometry("800x400")
        self.formulario.resizable(False, True)
        self.formulario.config(bg="red", cursor ="hand2")
        return self.formulario
    
    def iniciar_preguntas(self):
        label_nombre = Ventana.Label(self.formulario, text="Ingrese su nombre: ")
        label_nombre.config(padx=10 , pady=10, borderwidth=2 , fg="blue")
        label_nombre.pack()
        
        #entry --> input text --> cajitas de texto
        self.entry_nombre = Ventana.Entry(self.formulario)
        self.entry_nombre.config(bg="yellow")
        self.entry_nombre.pack()

#se crean los botones del formulario
        boton_enviar = Ventana.Button(self.formulario, text="Enviar", command="onclick")
        boton_enviar.configure(bg="organge")
        boton_enviar.pack(padx=10, pady=10)