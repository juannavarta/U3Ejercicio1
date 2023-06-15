from classFacultad import Facultad
from classCarrera import Carrera
import csv

class ManejadorFacultad:
    __facultad: list

    def __init__(self, facu=[]):
        self.__facultad = facu
    
    def carga(self):
        archivo = open("C://Users//csv//Facultades.csv", "r")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            if "Facultad" in fila[1]:
                cod = fila[0]
                nom = fila[1]
                dire = fila[2]
                loc = fila[3]
                tel = fila[4]
                xfac = Facultad(cod, nom, dire, loc, tel)
                self.__facultad.append(xfac)
        for i in range(len(self.__facultad)):
            for fila2 in reader:
                if "Facultad" not in fila[1]:
                    xCodF = fila[0]
                    xCodC = fila[1]
                    xNom = fila[2]
                    tit = fila[3]
                    dur = fila[4]
                    xcar = Carrera(xCodF, xCodC, xNom, tit, dur)
                    if xCodF == "I":
                        self.__facultad[0].setCarrera(xcar)
                    if xCodF == "E":
                        self.__facultad[1].setCarrera(xcar)
                    if xCodF == "S":
                        self.__facultad[2].setCarrera(xcar)
        archivo.close()
    
    def mostrarDatos(self):
        for j in range(len(self.__facultad)):
            print(self.__facultad[j].getNombre())
            for c in range(2):
                print("HOla")
                print(c)
                print(self.__facultad[j].getCarrera(c))