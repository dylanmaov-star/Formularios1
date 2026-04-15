import tkinter as Ventana
from tkinter import scrolledtext

# zona de clases
class Formulario:

    def __init__(self):
        self.colorRojo = "red"
        self.colorAmarillo = "yellow"
        self.formulario = None
        self.clientes = []

    def iniciar_ventana(self):
        self.formulario = Ventana.Tk()
        self.formulario.title("Registro de Cliente")
        self.formulario.geometry("500x650")
        self.formulario.configure(bg=self.colorRojo)
        return self.formulario

    def iniciar_preguntas(self):
        Ventana.Label(self.formulario, text="Nombre:", bg=self.colorAmarillo).pack(pady=2)
        self.entryNombre = Ventana.Entry(self.formulario)
        self.entryNombre.pack()

        Ventana.Label(self.formulario, text="Apellido:", bg=self.colorAmarillo).pack(pady=2)
        self.entryApellido = Ventana.Entry(self.formulario)
        self.entryApellido.pack()

        Ventana.Label(self.formulario, text="Edad:", bg=self.colorAmarillo).pack(pady=2)
        self.entryEdad = Ventana.Entry(self.formulario)
        self.entryEdad.pack()

        Ventana.Label(self.formulario, text="Teléfono:", bg=self.colorAmarillo).pack(pady=2)
        self.entryTelefono = Ventana.Entry(self.formulario)
        self.entryTelefono.pack()

        Ventana.Label(self.formulario, text="Correo:", bg=self.colorAmarillo).pack(pady=2)
        self.entryCorreo = Ventana.Entry(self.formulario)
        self.entryCorreo.pack()

        botonEnviar = Ventana.Button(
            self.formulario,
            text="Registrar Cliente",
            command=self.procesar_formulario
        )
        botonEnviar.pack(pady=10)

        self.labelResultado = Ventana.Label(self.formulario, text="", bg=self.colorAmarillo)
        self.labelResultado.pack(pady=5)

        Ventana.Label(self.formulario, text="Lista de Clientes:", bg=self.colorAmarillo).pack(pady=5)
        self.areaLista = scrolledtext.ScrolledText(self.formulario, width=50, height=10)
        self.areaLista.pack(pady=5)

    def procesar_formulario(self):
        if self.validar_campos():
            datos = self.capturar_datos()
            self.guardar_datos(datos)
            self.actualizar_lista_visual()
            self.mostrar_resultado("Cliente registrado correctamente")
            self.limpiar_campos()
        else:
            self.mostrar_resultado("Hay campos vacíos")

    def validar_campos(self):
        return all([
            self.entryNombre.get(), 
            self.entryApellido.get(), 
            self.entryEdad.get(), 
            self.entryTelefono.get(), 
            self.entryCorreo.get()
        ])

    def capturar_datos(self):
        return {
            "Nombre": self.entryNombre.get(),
            "Apellido": self.entryApellido.get(),
            "Edad": self.entryEdad.get(),
            "Teléfono": self.entryTelefono.get(),
            "Correo": self.entryCorreo.get()
        }

    def guardar_datos(self, datos):
        self.clientes.append(datos)

    def actualizar_lista_visual(self):
        self.areaLista.delete('1.0', Ventana.END)
        for i, cliente in enumerate(self.clientes, 1):
            texto = f"{i}. {cliente['Nombre']} {cliente['Apellido']} - {cliente['Correo']}\n"
            self.areaLista.insert(Ventana.END, texto)

    def mostrar_resultado(self, mensaje):
        self.labelResultado.config(text=mensaje)

    def limpiar_campos(self):
        self.entryNombre.delete(0, Ventana.END)
        self.entryApellido.delete(0, Ventana.END)
        self.entryEdad.delete(0, Ventana.END)
        self.entryTelefono.delete(0, Ventana.END)
        self.entryCorreo.delete(0, Ventana.END)

# zona de codigo principal
if __name__ == "__main__":
    app = Formulario()
    ventana = app.iniciar_ventana()
    app.iniciar_preguntas()
    ventana.mainloop()