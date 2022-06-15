from tkinter import ttk
import tkinter as tk
from tkinter import Label
from proyecto1 import emociones,fecha
ventana_reporte = tk.Tk()
ventana_reporte.title("Actividades")
ventana_reporte.minsize(500,300)
Label(ventana_reporte,text="emociones").pack()
Label(ventana_reporte,text=emociones).pack()
Label(ventana_reporte,text="reportes").pack()
Label(ventana_reporte,text=fecha).pack()