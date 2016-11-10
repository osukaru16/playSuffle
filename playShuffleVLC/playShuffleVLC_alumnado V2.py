

## UTILIDADES DE DEPURACION ## 


def checkSeleccionaCancionRandom(cancion, libreria):


def checkPlaySuffle(playList):




## RUTINAS DE UTILIDADES ## 


def seleccionaCancionRandom(libreria):
    return tituloCancion


def iniciarPlayList(numeroCancion):
    Good bless you


def imprimirCancionesReproducidas(playList):
    muestra lista de canciones en consola

def lanzarVLC(libreria, playList):

    import subprocess
    import shlex
    import os

    linuxPathVLC = "/usr/bin/vlc"
    lineaComandoVLC = linuxPathVLC
    separador = " "

    for numeroCancion in sorted(playList.keys()):
        tituloCancion = playList[numeroCancion]
        try:
            rutaAccesoFichero = libreria[tituloCancion]["location"]
        except KeyError:
            print("la cancion " + str(tituloCancion) + " no se encuentra en la biblioteca")
        else:
            if os.path.exists(str(rutaAccesoFichero)):
                lineaComandoVLC = lineaComandoVLC + separador + str(rutaAccesoFichero)
            else:
                pass

    # Popen necesita una lista de string
    args = shlex.split(lineaComandoVLC)

    try:
        procesoVLC = subprocess.Popen(args)
        # procesoVLC = subprocess.Popen(["/usr/bin/vlc", "California_Uber_Alles.mp3", "Seattle_Party.flac"])
    except OSError:
        print("el fichero no existe")
    except ValueError:
        print("argumentos invalidos")
    else:
        print("lanzando VLC con lista aleatoria")


## FUNCION PRINCIPAL ## 


def playSuffle(libreria, playList):

    genera la lista aleatoria de canciones a partir de la libreria



## PROGRAMA PRINCIPAL ##

playList = {}

libreria = {"California_Uber_Alles.mp3": 
                {"track-number": 3, "artist": "Dead Kennedys", "album": "Dead Kennedys", "location": "./biblioteca/California_Uber_Alles.mp3"},
            "Seattle_Party": 
                {"track-number": 1, "artist": "Chastity Belt", "album": "No regrets", "location": "./biblioteca/Seattle_Party.flac"},
            "King_Kunta":
                {"track-number": 3, "artist": "Kendrick Lamar", "album": "To Pimp A Butterfly", "location": "./biblioteca/King_Kunta.mp3"}   
            }

# for i in range(1,1001):
assert playSuffle(libreria, playList)

# libreriaLista = []
# assert playSuffle(libreriaLista)

imprimirCancionesReproducidas(playList)

lanzarVLC(libreria, playList)