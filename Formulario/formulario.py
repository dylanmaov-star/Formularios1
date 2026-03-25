import tkinter as ventana # colocar sobrenombre 

class Formulario:
    def _init_(self):
        self.color = "rojo"
        self.entry_nombre = " "
        self.label_resultado = " "
        self.formulario = " "
        
    def iniciar_ventana(self):
        self.formulario = ventana.Tk() #widgets
        self.formulario.title("Registro de usuario")
        self.formulario.geometry("800x800")
        self.formulario.resizable(False, True)
        self.formulario.configure(bg=r"red", cursor="hand2")
        return self.formulario
    
    def iniciar_preguntas(self):
        #label --> titulos 
        label_nombre = ventana.Label(self.formulario, text="Ingrese su nombre: ")
        label_nombre.config(padx=10 , pady=10, borderwidth=2 , fg="blue")
        label_nombre.pack()
        
        #entry --> input text --> cajitas de texto
        self.entry_nombre = ventana.Entry(self.formulario)
        self.entry_nombre.configure(bg="yellow")
        self.entry_nombre.pack()
        
        #button --> botones
        boton_enviar = ventana.Button(self.formulario, text="Enviar", command="onclick()")
        boton_enviar.configure(bg="blue")
        boton_enviar.pack()