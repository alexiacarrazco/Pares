import Tarjetas.py;




def main( archivo ):
    """Se manda a llamar leer archivo y este archivo leido devuelve texto, ese texto se le contaran sus palabras . Se manda a leer el stopwords y se crea un nuevo diccionario quitando     las stop de las palabras leidas, se imprime el nuevo diccionario con la condicion de palabras minimas que se le pida.
    """
    texto = leer_archivo( archivo )
    dip   = contar_palabras( texto )
    stopwords= leer_stopwords ("StopWords.txt")
    nuevo_diccionario= eliminar_stopwords(dip, stopwords)
    imprime_diccionario(nuevo_diccionario,minimo)

if __name__ == "__main__":
    """se declara a pedir el archivo y el minimo de palabras a imprimir
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--archivo', dest='archivo', help=
    "nombre de archivo", required=True)
    parser.add_argument('-m', '--minimo', dest='minimo', help=
    "minimo de palabras repetidas", required=False, type=int)
    args = parser.parse_args()
    minimo= args.minimo
    archivo = args.archivo
    #./lector.py -a /tmp/episodio4.txt
    #archivo = "/tmp/episodio4.txt"
    main(archivo)
