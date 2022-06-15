from msilib.schema import Class
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showwarning, askyesno,showerror
#Carga de archivos de carreras existentes
#carreras=a.recuperar_cursos()

#Guarda en archivos el registro en memoria de carreras
def guardar():
    global carreras
    #a.guardar_en_archivo(carreras)

#Ventana principal de la aplicación
#clase de punteros
class lista():
    sig=None
    def __init__(self) -> None:
        pass

    def insertar (self,rn):
        puntero=self
        while (puntero.sig!=None):
            puntero=puntero.sig
        puntero.sig=rn

    def largo (self):
        puntero=self
        cont=1
        while (puntero.sig!=None):
            puntero=puntero.sig
            cont+=1
        return (cont)

    def extraer (self,pos):
        puntero=self
        while (pos>0):
            puntero=puntero.sig
            pos-=1
        return (puntero)
class persona(lista):
    nombre:None    
    credito:None    
    hora:None
    horai:None
    horaf:None

    def __init__(self,nombre,credito,hora,horai,horaf) -> None:
        super().__init__()
        self.nombre=nombre
        self.credito=credito
        self.hora=hora
        self.horai=horai
        self.horaf=horaf
        pass

    def guardar(self):
        puntero=self
        try:
            with open("actividades.dat","tw") as archivo:
                archivo.writelines([puntero.nombre,puntero.credito,puntero.hora,puntero.horai,puntero.horaf].__str__()+"\n")
                while puntero.sig!=None:
                    puntero=puntero.sig
                    archivo.writelines([puntero.nombre,puntero.credito,puntero.hora,puntero.horai,puntero.horaf].__str__()+"\n")
        except FileNotFoundError as error:
            showerror(message='No se pudo guardar en el archivo de carreras')

    def listar_personas (self):
        respuesta=[]
        puntero=self
        respuesta.append(puntero.nombre)
        while (puntero.sig!=None):
            puntero=puntero.sig
            respuesta.append(puntero.nombre)
        return (respuesta)

#cargar datos de actividades
def cargar_archivo_personas():
    respuesta=None
    try:
        with open("actividades.dat","tr") as lector:
            lectura= eval(lector.readline()[:-1])
            if lectura!='':
                respuesta=persona(nombre=lectura[0],credito=lectura[1],hora=lectura[2],horai=lectura[3],horaf=lectura[4])
            lectura= eval(lector.readline()[:-1])
            while (lectura!=''):
                respuesta.insertar(persona(nombre=lectura[0],credito=lectura[1],hora=lectura[2],horai=lectura[3],horaf=lectura[4]))
                lectura= eval(lector.readline()[:-1])
    except FileNotFoundError as error:
        respuesta=askyesno(title="Error", message="No encontramos el archivo de datos desea crear un nuevo archivo de registro (s/n)")
        if respuesta:
            open("actividades.dat","tw").close()
    finally:
        return respuesta
lista_activiadades=cargar_archivo_personas()
posicion_registro=0
registro_actual=None
def registro_anterior():
    global sv_nombre,sv_credi,sv_hora,sv_horaF,sv_horaI,posicion_registro,registro_actual
    if (lista_activiadades!=None):
        if posicion_registro>0:
            posicion_registro-=1
            r=lista_activiadades.extraer(posicion_registro)
            sv_nombre.set(r.nombre)
            sv_credi.set(r.credito)
            sv_hora.set(r.hora)
            sv_horaI.set(r.horai)
            sv_horaF.set(r.horaf)
            registro_actual=r
def registro_siguiente():
    global sv_nombre,sv_carrera,sv_credi,sv_hora,sv_fechaf,sv_fechai,sv_horario, posicion_registro, registro_actual
    if (lista_activiadades!=None):
        if lista_activiadades.largo()-1>posicion_registro:
            posicion_registro+=1
            r=lista_activiadades.extraer(posicion_registro)
            sv_nombre.set(r.nombre)
            sv_credi.set(r.credito)
            sv_hora.set(r.hora)
            sv_horaI.set(r.horai)
            sv_horaF.set(r.horaf)
            registro_actual=r


ventana_actividades = tk.Tk()
ventana_actividades.title("Actividades")
ventana_actividades.minsize(500,300)
#nombre
lb_nombre=tk.Label(ventana_actividades,text="Descricion de la actividad:").place(x=10, y=40)
sv_nombre = tk.StringVar()
e_nombre = ttk.Entry(ventana_actividades, textvariable = sv_nombre, width=50).place(x=160, y=40)

#creditos 
lb_credi=tk.Label(ventana_actividades,text="Curso asociado a la actividad:").place(x=10, y=70)
sv_credi = tk.StringVar()
e_credi = ttk.Entry(ventana_actividades, textvariable = sv_credi, width=30).place(x=170, y=70)

#horas
lb_hora =tk.Label(ventana_actividades,text="Horas de duracion de la actividad:").place(x=10, y=100)
sv_hora = tk.StringVar()
e_hora = ttk.Entry(ventana_actividades, textvariable = sv_hora, width=30).place(x=210, y=100)

lb_horaI =tk.Label(ventana_actividades,text="Fecha de inicio de la actividad:").place(x=10, y=130)
sv_horaI = tk.StringVar()
e_horaI = ttk.Entry(ventana_actividades, textvariable = sv_horaI, width=30).place(x=180, y=130)

lb_horaF =tk.Label(ventana_actividades,text="Fecha de conclusion de la actividad:").place(x=10, y=160)
sv_horaF = tk.StringVar()
e_horaF = ttk.Entry(ventana_actividades, textvariable = sv_horaF, width=30).place(x=210, y=160)
lb_mensaje=tk.Label(ventana_actividades, text="Para buscar activiades dar click en siguiente y anterior").place (x=180, y=220)
sv_mensaje=tk.StringVar()
tk.Button(ventana_actividades, text="Anterior", command=registro_anterior).place(x=320, y=260)
tk.Button(ventana_actividades, text="Siguiente", command=registro_siguiente).place(x=420, y=260)
ventana_actividades.mainloop()