
#from curso.hola import curso


import tkinter as tk
from tkinter import Label
from tkinter.messagebox import showwarning, askyesno
from time import   strftime
from pygame import mixer
from padres import padres,persona

#Carga de archivos de carreras existentes


#Guarda en archivos el registro en memoria de carreras


#Ventana principal de la aplicación
ventana_principal = tk.Tk()
ventana_principal.title("Aplicación principal")
ventana_principal.minsize(400,200)

#Ventana secundaria para módulos de mantenimiento
ventana_modal=None
def administrar_curso():
    ventana_principal.withdraw()
    from curso.registro_personas import ventana_curso
    ventana_curso()

#Acciones de la ventana principal y su menú
def cerrarVentana(v):
    v.destroy()
    
# def administrar_carreras():
#     global ventana_modal
#     try:
#         ventana_modal.mostrar()
#     except:
#         ventana_modal=vCarrera(padre=ventana_principal,geometria='400x300',titulo='Administración de carreras')
#         ventana_modal.mostrar()
def administrar_curso():
    global ventana_modal
def administrar_actividades():
    from actividades import cargar_archivo_personas
    cargar_archivo_personas()
def administrar_reportes():
    print
def reconocer():
    from proyecto1 import rostro
    rostro()
def distra():
    from proyecto2 import rostro2
    rostro2()
# def noreconocer():
#     pass
# def nodistra():
#     pass
def asignar_padres():
    persona()
    pass
#Reloj
lista_horas = []
lista_minutos = []
lista_segundos = []

for  i in range(0,24):
	lista_horas.append(i)

for  i in range(0,60):
	lista_minutos.append(i)

for  i in range(0,60):
	lista_segundos.append(i)
def obtener_tiempo():
	# x_hora = combobox1.get()
	# x_minutos = combobox2.get()
	# x_segundos = combobox3.get()

	hora =  strftime('%H')
	minutos = strftime('%M')
	segundos = strftime('%S')

	hora_total = (hora + ' : '+ minutos+ ' : '+ segundos)
	texto_hora.config(text=hora_total, font = ('Radioland', 25))

	texto_hora.after(100, obtener_tiempo)


texto_hora = Label(ventana_principal,  fg = 'green2')
texto_hora.grid(columnspan=10, row=5,sticky="nsew", ipadx=100, ipady=40)

obtener_tiempo()
#boton de salir de la ventana principal
btn_salir = tk.Button(ventana_principal, text="Salir", command=lambda: cerrarVentana(ventana_principal))
btn_salir.place(x=50, y=150)
btn_reco = tk.Button(ventana_principal, text="Reconcimiento de emociones", command= reconocer)
btn_reco.place(x=190, y=150)
btn_des = tk.Button(ventana_principal, text="Destraciones", command=distra)
btn_des.place(x=100, y=150)
# btn_desreco = tk.Button(ventana_principal, text="Desabilitar  reconicimiento", command=nodistra)
# btn_desreco.place(x=30, y=120)
# btn_desreco = tk.Button(ventana_principal, text="Desabilitar  Destarciones", command=noreconocer)
# btn_desreco.place(x=210, y=120)
# Oculta la ventana pero no se cierra
#ventana_principal.protocol("WM_DELETE_WINDOW", ventana_principal.iconify)
# Si queremos asociar la tecla scape a la acción de cerrar la ventana
ventana_principal.bind('<Escape>', lambda e: ventana_principal.destroy())

# Menú del sistema
menubar = tk.Menu(ventana_principal)
ventana_principal.config(menu=menubar)

# primer opción del menú
menu_archivo = tk.Menu(menubar, tearoff=1)
#menu_archivo.add_command(label="Guardar",  command=guardar)
menu_archivo.add_checkbutton(label="Autoguardado", onvalue=1, offvalue=0)
menu_archivo.add_separator()
menu_archivo.add_command(label="Exit", command=ventana_principal.destroy)

# Segunda opción del menú
menu_mantenimiento = tk.Menu(menubar, tearoff=0)
#menu_mantenimiento.add_command(label="Modificar y Consultar Carreras", command=administrar_carreras)

# Segunda opción del menú
menu_cursos = tk.Menu(menubar, tearoff=0)
menu_cursos.add_command(label="Modificar Y Consultar Cursos", command=administrar_curso)

menu_reporte=menu_cursos = tk.Menu(menubar, tearoff=0)
menu_reporte.add_command(label="Agregar Reportes", command=asignar_padres)

menu_actividades=menu_cursos = tk.Menu(menubar, tearoff=0)
menu_actividades.add_command(label="activiades", command=administrar_actividades)


# Adicionar al menu pirncipal los dos submenus
menubar.add_cascade(label="Archivo", menu=menu_archivo)
menubar.add_cascade(label="Consultar adtiviadades", menu=menu_actividades)
menubar.add_cascade(label="Reportes", menu=menu_reporte)

# Ciclo principal de la aplicación

# Ciclo principal de la aplicación
ventana_principal.mainloop()
