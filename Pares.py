import Tarjetas.py;

def main(jugador, manos):
    





if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-j', '--jugador', dest='jugador', help=
    "nombre de jugador", required=True, type=str)
    parser.add_argument('-m', '--manos', dest='manos', help=
    "cartas en mano", required=True, type=int)
    args = parser.parse_args()
    manos= args.manos
    jugador = args.jugador
    main(jugador)
