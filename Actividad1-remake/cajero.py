class Cajero:
    def __init__(self, idc, dinerodisponible):
        self.__id_cajero = idc
        self.__dinerodisponible = dinerodisponible
        self.__dinerodis = False

    @property
    def id_cajero(self):
        return self.__id_cajero

    @property
    def dinerodisponible(self):
        return self.__dinerodisponible

    @property
    def dinerodis(self):
        return self.__dinerodis

    def consultardd(self, dineroaextraer):
        if dineroaextraer <= 0:
            return False
        return self.__dinerodisponible >= dineroaextraer

    def extraerdinero(self, dineroaextraer):
        if self.consultardd(dineroaextraer):
            self.__dinerodisponible -= dineroaextraer
            self.__dinerodis = True
            return True

        self.__dinerodis = False
        return False


