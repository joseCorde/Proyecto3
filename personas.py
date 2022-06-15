from tkinter.messagebox import showerror


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
    fechai:None
    fechaf:None
    horario:None
    carrera:None

    def __init__(self,nombre,credito,hora,fechai,fechaf,horario,carrera) -> None:
        super().__init__()
        self.nombre=nombre
        self.credito=credito
        self.hora=hora
        self.fechai=fechai
        self.fechaf=fechaf
        self.horario=horario
        self.carrera=carrera
        pass

    def guardar(self):
        puntero=self
        try:
            with open("personas.dat","tw") as archivo:
                archivo.writelines([puntero.nombre,puntero.credito,puntero.hora,puntero.fechai,puntero.fechaf,puntero.horario,puntero.carrera].__str__()+"\n")
                while puntero.sig!=None:
                    puntero=puntero.sig
                    archivo.writelines([puntero.nombre,puntero.credito,puntero.hora,puntero.fechai,puntero.fechaf,puntero.horario,puntero.carrera].__str__()+"\n")
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



class arbol_persona():
    nombre=None
    papa=None
    mama=None

    def __init__(self,nombre) -> None:
        self.nombre=nombre

if  __name__=='__main__':
    yo=arbol_persona("Leonardo Víquez")
    mi_papa=arbol_persona("Óscar Víquez")
    mi_mama=arbol_persona("Idalí Acuña")

    yo.papa=mi_papa
    yo.mama=mi_mama

    mi_mama.mama=arbol_persona('Marta Majías')
    mi_mama.papa=arbol_persona('Ignacio')

    yo.papa.papa=arbol_persona("Carlos")
    yo.papa.mama=arbol_persona("Alicia")

    danna=arbol_persona("Danna")
    danna.papa=yo

    pass