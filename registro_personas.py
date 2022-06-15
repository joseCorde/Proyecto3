import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showwarning, askyesno
#from padres import padres

from curso.personas import persona
def asignar_padres():
    #padres(lista_personas)
    pass

def cargar_archivo_personas():
    respuesta=None
    try:
        with open("personas.dat","tr") as lector:
            lectura= eval(lector.readline()[:-1])
            if lectura!='':
                respuesta=persona(nombre=lectura[0],credito=lectura[1],hora=lectura[2],fechai=lectura[3],fechaf=lectura[4],
                horario=lectura[5],carrera=lectura[6])
            lectura= eval(lector.readline()[:-1])
            while (lectura!=''):
                respuesta.insertar(persona(nombre=lectura[0],credito=lectura[1],hora=lectura[2],fechai=lectura[3],fechaf=lectura[4],
                horario=lectura[5],carrera=lectura[6]))
                lectura= eval(lector.readline()[:-1])
    except FileNotFoundError as error:
        respuesta=askyesno(title="Error", message="No encontramos el archivo de datos desea crear un nuevo archivo de registro (s/n)")
        if respuesta:
            open("personas.dat","tw").close()
    finally:
        return respuesta
            


lista_personas=cargar_archivo_personas()
posicion_registro=0
registro_actual=None

ventana_curso = tk.Tk()
ventana_curso.title("Aplicación principal")
ventana_curso.minsize(700,300)

def cerrarVentana(v):
    v.destroy()

def agregar_registro():
    global sv_nombre,sv_carrera,sv_credi,sv_hora,sv_fechaf,sv_fechai,sv_horario,lista_personas
    try:
        np=persona(nombre=sv_nombre.get(),credito=int(sv_credi.get()),carrera=sv_carrera.get(),hora=sv_hora.get(),
        fechai=sv_fechai.get(),fechaf=sv_fechaf.get(),horario=sv_horario.get())
        if lista_personas==None:
            lista_personas=np
        else:
            lista_personas.insertar(np)

        sv_nombre.set('')
        sv_credi.set('')
        sv_hora.set('')
        sv_fechai.set('')
        sv_fechai.set('')
        sv_horario.set('')
        sv_carrera.set('')

        lista_personas.guardar()
    except:
        showwarning(title="alerta", message="Usted ha digitado una edad inválida!")
    pass

def modificar_registro():
    global sv_nombre,sv_carrera,sv_credi,sv_hora,sv_fechaf,sv_fechai,sv_horario,registro_actual
    try:
        registro_actual.nombre=sv_nombre.get()
        registro_actual.credito=int(sv_credi.get())
        registro_actual.hora=sv_hora.get()
        registro_actual.fechai=sv_fechai.get()
        registro_actual.fechaf=sv_fechaf.get()
        registro_actual.horario=sv_horario.get()
        registro_actual.carrera=sv_carrera.get()
        lista_personas.guardar()
    except:
        showwarning(title="alerta", message="Usted ha digitado una edad inválida!")
    pass
    

def registro_anterior():
    global sv_nombre,sv_carrera,sv_credi,sv_hora,sv_fechaf,sv_fechai,sv_horario,posicion_registro,registro_actual
    if (lista_personas!=None):
        if posicion_registro>0:
            posicion_registro-=1
            r=lista_personas.extraer(posicion_registro)
            sv_nombre.set(r.nombre)
            sv_credi.set(r.credito)
            sv_hora.set(r.hora)
            sv_fechai.set(r.fechai)
            sv_fechaf.set(r.fechaf)
            sv_horario.set(r.horario)
            sv_carrera.set(r.carrera)
            registro_actual=r


def registro_siguiente():
    global sv_nombre,sv_carrera,sv_credi,sv_hora,sv_fechaf,sv_fechai,sv_horario, posicion_registro, registro_actual
    if (lista_personas!=None):
        if lista_personas.largo()-1>posicion_registro:
            posicion_registro+=1
            r=lista_personas.extraer(posicion_registro)
            sv_nombre.set(r.nombre)
            sv_credi.set(r.credito)
            sv_hora.set(r.hora)
            sv_fechai.set(r.fechai)
            sv_fechaf.set(r.fechaf)
            sv_horario.set(r.horario)
            sv_carrera.set(r.carrera)
            registro_actual=r
#nombre
lb_nombre=tk.Label(ventana_curso,text="Nombre:").place(x=10, y=40)
sv_nombre = tk.StringVar()
e_nombre = ttk.Entry(ventana_curso, textvariable = sv_nombre, width=50).place(x=80, y=40)

#creditos 
lb_credi=tk.Label(ventana_curso,text="Créditos del curso").place(x=10, y=70)
sv_credi = tk.StringVar()
e_credi = ttk.Entry(ventana_curso, textvariable = sv_credi, width=30).place(x=130, y=70)

#horas
lb_hora =tk.Label(ventana_curso,text="Horas lectivas:").place(x=10, y=100)
sv_hora = tk.StringVar()
e_hora = ttk.Entry(ventana_curso, textvariable = sv_hora, width=30).place(x=120, y=100)

#fecha de inicio de clases
lb_fechai=tk.Label(ventana_curso, text="Fecha de inicio: ").place (x=10, y=130)
sv_fechai=tk.StringVar()
e_fechai=ttk.Entry(ventana_curso, textvariable=sv_fechai, width=30).place (x=140, y=130)

#fecha de finalizacion de clases
lb_fechaf=tk.Label(ventana_curso, text="Fecha de finalizacion: ").place (x=10, y=160)
sv_fechaf=tk.StringVar()
e_fechaf=ttk.Entry(ventana_curso, textvariable=sv_fechaf, width=30).place (x=140, y=160)

#Horarios
lb_horario=tk.Label(ventana_curso, text="Horario de clases: ").place (x=10, y=190)
sv_horario=tk.StringVar()
e_horario=ttk.Entry(ventana_curso, textvariable=sv_horario, width=30).place (x=140, y=190)

#Carreras
lb_carrera=tk.Label(ventana_curso, text="Carrera a la que pertenece: ").place (x=10, y=220)
sv_carrera=tk.StringVar()
e_carrera=ttk.Entry(ventana_curso, textvariable=sv_carrera, width=30).place (x=180, y=220)
lb_mensaje=tk.Label(ventana_curso, text="Para consulatal dar click en siguiente").place (x=380, y=220)
sv_mensaje=tk.StringVar()

#botónes de acción de la ventana
tk.Button(ventana_curso, text="Modificar", command=modificar_registro).place(x=320, y=260)
tk.Button(ventana_curso, text="Anterior", command=registro_anterior).place(x=420, y=260)
tk.Button(ventana_curso, text="Siguiente", command=registro_siguiente).place(x=520, y=260)
tk.Button(ventana_curso, text="Agregar", command=agregar_registro).place(x=620, y=260)
tk.Button(ventana_curso, text="Salir", command=lambda: cerrarVentana(ventana_curso)).place(x=180, y=260)




ventana_curso.mainloop()