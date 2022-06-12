'''
En python no existe el concepto de variable privada
Para emularlo, como convención se usa __ delante de una variable, atributo o método.
'''

class GrupoPropulsor():
    def __init__(self, modelo):
        self.modelo = modelo
        self.__motor = Motor()
        self.__embrague = Embrague()
        self.__caja_cambios = CajaCambios()

    def encender(self):
        self.__motor.encender()

    def apagar(self):
        self.__motor.apagar()

    def acelerar(self):
        self.__motor.acelerar()


class Motor():
    __is_active = False
    __run = False

    def __init__(self):
        self.__modelo = "SM4"

    def encender(self):
        self.__is_active = True

    def apagar(self):
        self.__is_active = False

    def acelerar(self):
        self.__run = True


class Embrague():
    def __init__(self):
        self.__modelo = "EM-90"


class CajaCambios():
    def __init__(self):
        self.__modelo = "CH-45"


class SistemaDireccion():
    def __init__(self, modelo):
        self.modelo = modelo
        self.__ruedas_directrices = RuedasDirectrices()
        self.__eje_delantero = EjeDelantero()

    def girar_dcha(self):
        self.__ruedas_directrices.girar_dcha()

    def girar_izq(self):
        self.__ruedas_directrices.girar_izq()


class RuedasDirectrices():
    __turn_right = True

    def __init__(self):
        self.__modelo = "RD-87"

    def girar_dcha(self):
        self.__turn_right = True

    def girar_izq(self):
        self.__turn_right = False


class EjeDelantero():
    def __init__(self):
        self.__modelo = "ED-32"


class SistemaFrenado():
    __brake = False
    def __init__(self, modelo):
        self.modelo = modelo
        self.__frenado_izq = FrenadoIzquierdo()
        self.__frenado_dch = FrenadoDerecho()

    def frenar(self):
        if self.__frenado_izq.frenar_izq() and self.__frenado_dch.frenar_dch():
            self.__brake = True


class FrenadoIzquierdo():
    __brake = False

    def __init__(self):
        self.__modelo = "DFI-82"

    def frenar_izq(self):
        self.__brake = True


class FrenadoDerecho():
    __brake = False

    def __init__(self):
        self.__modelo = "DFD-82"

    def frenar_dch(self):
        self.__brake = True


class Coche():
    velocidad = 0

    def __init__(self, modelo, marca, grupoPropulsor, sistemaDireccion, sistemaFrenado):
        self.modelo = modelo
        self.marca = marca
        self.__grupo_propulsor = grupoPropulsor
        self.__sistema_direcc = sistemaDireccion
        self.__sistema_frenado = sistemaFrenado

    def encender(self):
        self.__grupo_propulsor.encender()

    def apagar(self):
        self.__grupo_propulsor.apagar()

    def girar_dcha(self):
        self.__sistema_direcc.girar_dcha()

    def girar_izq(self):
        self.__sistema_direcc.girar_izq()

    def acelerar(self):
        self.__grupo_propulsor.acelerar()
        self.velocidad +=1

    def frenar(self):
        self.__sistema_frenado.frenar()
        if self.velocidad > 0:
            self.velocidad -=1

    @property
    def modelo_grupo_propulsor(self):
        return self.__grupo_propulsor.modelo

    @property
    def modelo_sist_direcc(self):
        return self.__sistema_direcc.modelo

    @property   
    def modelo_sist_frenado(self):
        return self.__sistema_frenado.modelo



if __name__ == "__main__":
    print("-------------------- Coche 1 --------------------")
    coche1 = Coche("5008", "Renault", GrupoPropulsor("PropX3"), SistemaDireccion("SDM5"), SistemaFrenado("SF78"))
    print(coche1.marca)
    print(coche1.modelo)
    print(coche1.modelo_grupo_propulsor)
    print(coche1.modelo_sist_direcc)
    print(coche1.modelo_sist_frenado)
    print("-------------------- Coche 2 --------------------")
    coche2 = Coche("2056", "Seat", GrupoPropulsor("PropV9"), SistemaDireccion("SFP4"), SistemaFrenado("SLO3"))
    print(coche2.marca)
    print(coche2.modelo)
    print(coche2.modelo_grupo_propulsor)
    print(coche2.modelo_sist_direcc)
    print(coche2.modelo_sist_frenado)
    print("-------------------- Coche 3 --------------------")
    coche3 = Coche("6984", "Mercedes", GrupoPropulsor("PropT5"), SistemaDireccion("SDO6"), SistemaFrenado("SFR0"))
    print(coche3.marca)
    print(coche3.modelo)
    print(coche3.modelo_grupo_propulsor)
    print(coche3.modelo_sist_direcc)
    print(coche3.modelo_sist_frenado)
    