from tkinter import Toplevel
import tkinter as tk
from tkinter import ttk

class padres():
    ventana=None
    sv_nombre_persona=None
    lista_personas=None
    def __init__(self,l) -> None:
        """constructor de personas
        Args:
        - l (personas): lista de punteros de registros de personas
        """
        self.lista_personas=l

        self.ventana=Toplevel()
        self.ventana.geometry('400x400')
        self.ventana.resizable(False, False)
        self.ventana.title('Asignación de padres')

        # combobox
        self.sv_nombre_persona = tk .StringVar()
        cb_carrera = ttk.Combobox(self.ventana, textvariable=self.sv_nombre_persona)
        cb_carrera['values'] = self.lista_personas.listar_personas()
        cb_carrera['state'] = 'readonly'
        cb_carrera.place(x=80,y=10)
        #cb_carrera.bind('<<ComboboxSelected>>', self.cambio_carrera)
