import random

def baraj(figuras, diccionario):
    lista_cartas = []
    for figura in figuras:
        for carta, valor in diccionario_cartas.items():
            naipe = carta + " " + figura
            carta = Carta(valor,naipe)
            lista_cartas.append(carta)
    return lista_cartas

class Jugador: 
    def _init_(self, nombre, mano):
        self.nombre = nombre
        self.mano = mano
    def despliega_mano(self):
        print(self.nombre)
        for x in self.mano:
            print(x)
        print("*****")
        

class Carta:
    def _init_(self, valor, figura):
        self.valor=valor
        self.figura=figura
    def _str_(jugador):
        self.carta=self.valor+self.figura;
        return self.carta
        

class Baraja:
    def _init_(self):
        self.diccionario= {'A':20, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13}
        self.lista_cartas= ['AP', '2P', '3P', '4P', '5P', '6P', '7P', '8P', '9P', '10P', 'JP', 'QP', 'KP',
                       'AT', '2T', '3T', '4T', '5T', '6T', '7T', '8T', '9T', '10T', 'JT', 'QT', 'KT',
                       'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC',
                       'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD']
        self.lista_figuras= ['P', 'T', 'C', 'D'] 
        lista_jugadores= []
        self.lista_cartas = baraj(self.figuras, self.diccionario)
        
    
    def genera_mano(manos):
        i = 0
        mano= []
        while i < 5:
         if len(manos.lista_cartas)==0:
                print("Se han acabado las cartas!")
                break
            r = random.choice(manos.lista_jugadores)
            mano.append(r)
            manos.lista_cartas.remove(r)
            i += 1
        return mano
        
    def guarda_jugador(manos,jugador):
        manos.lista_jugadores.append(jugador);
