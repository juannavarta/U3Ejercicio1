from classCarrera import Carrera

class Facultad:
    __codF: str
    __nom: str
    __dir: str
    __loc: str
    __tel: str
    __carreras: list

    def __init__(self, codF="", nom="", dire="", loc="", tel="", carrera = []):
        self.__codF = codF
        self.__nom = nom
        self.__dir = dire
        self.__loc = loc
        self.__tel = tel
        self.__carreras = carrera
        
    def getCod(self):
        return self.__codF
        
    def setCarrera(self, car):
        return self.__carreras.append(car)
    
    def getNombre(self):
        return self.__nom
    
    def getCarrera(self, x):
        return self.__carreras[x].getNombre()
    
    def getLen(self):
        return len(self.__carreras)