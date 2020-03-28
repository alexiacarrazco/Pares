import random
class Judador: 
    
    jugador = None
    mano = None
    puntos = None
    
    def __init__(self, jugador, baraja):
        self.nombre = jugador
        self.mano = mano
        self.puntos= 0
        baraja.guarda_jugador(self)
        
    def despliega_mano(self, baraja):
        mano_desplegada = []
        print(self.nombre)
        for c in self.mano:
            cartas = f"{c.display(baraja.diccionario_cartas)}"
            print(cartas)
            mano_desplegada.append(cartas)
        return mano_desplegada

class Carta:
    
    valor= None
    figura = None
    
    def __init__(self):
        self.valor= valor
        self.figura= figura
        
    def __str__(self, diccionario):
        carta_uno = diccionario[self.valor]
        return f"{carta_uno}-{self.figura}"
    
class Baraja:
    diccionario = None
    lista_figuras = None
    lista_jugadores= None
    lista_cartas= None
    
    def __init__(self, lista_cartas ):
        self.diccionario= {'A':20, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13}
        lista_cartas= ['AP', '2P', '3P', '4P', '5P', '6P', '7P', '8P', '9P', '10P', 'JP', 'QP', 'KP',
                       'AT', '2T', '3T', '4T', '5T', '6T', '7T', '8T', '9T', '10T', 'JT', 'QT', 'KT',
                       'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC',
                       'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD']
        self.lista_figuras= ['P', 'T', 'C', 'D']
        self.lista_jugadores= []
    def genera_mano(manos):
        for x in self.lista_jugadores:
            x.mano = random.sample(self.lista_cartas, num_cartas)

            for y in x.mano:
                self.lista_cartas.remove(y)
        
    def guarda_jugador(self, jugador):
        self.lista_jugadores.append(jugador)
