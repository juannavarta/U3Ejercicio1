class Carrera:
    __codF: str
    __codC: int
    __nom: str
    __tit: str
    __dur: str

    def __init__(self, codF="", codC=0, nom="", tit="", dur=""):
        self.__codF = codF
        self.__codC = codC
        self.__nom = nom
        self.__tit = tit
        self.__dur = dur
    
    def getNombre(self):
        return self.__nom