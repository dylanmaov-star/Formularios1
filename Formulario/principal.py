from formulario import Formulario


# Zona de codigo principal

obj_formulario = Formulario()

# linea 7 es traer la ventana
aux_formulario = obj_formulario.iniciar_ventana()
obj_formulario.iniciar_preguntas()
aux_formulario.mainloop() # Siempre ir al final