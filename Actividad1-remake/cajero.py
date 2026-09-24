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
        self.__dinerodis = (
            dineroaextraer > 0
            and self.__dinerodisponible >= dineroaextraer
        )
        return self.__dinerodis

    def extraerdinero(self, dineroaextraer):
        if not self.consultardd(dineroaextraer):
            return False

        self.__dinerodisponible -= dineroaextraer
        return True


