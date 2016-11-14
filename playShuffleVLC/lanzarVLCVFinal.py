import random
import subprocess
import shlex
import os

playList = []



def seleccionaCancionRandom(libreria, playList):
	try:
		assert isinstance(libreria, dict), "a petado"
	
		playList = list(libreria.keys())
		random.shuffle(playList)
		
		return playList
	except IndexError:
		return "Error en el diccionario"





def lanzarVLC(libreria, playList):

	linuxPathVLC = "C:\Program Files (x86)\VideoLAN\VLC\melo.exe"
	lineaComandoVLC = linuxPathVLC
	separador = " "
	

	for numeroCancion in range(0,len(playList)):
		tituloCancion = playList[numeroCancion]
		rutaAccesoFichero = libreria[tituloCancion]["location"]
		lineaComandoVLC = lineaComandoVLC + separador + str(rutaAccesoFichero)
		print(tituloCancion)

	try:
		procesoVLC = subprocess.call(lineaComandoVLC)
		print(lineaComandoVLC)
        # procesoVLC = subprocess.Popen(["/usr/bin/vlc", "California_Uber_Alles.mp3", "Seattle_Party.flac"])
	except OSError:
		print("el fichero no existe")
	except ValueError:
		print("argumentos invalidos")
	else:
		print("lanzando VLC con lista aleatoria")





		
		
		
		
#


## PROGRAMA PRINCIPAL ##



libreria = {"California_Uber_Alles": 
                {"track-number": 3, "artist": "Dead Kennedys", "album": "Dead Kennedys", "location": "\Musica\sistersnoise.mp3"},
            "Seattle_Party": 
                {"track-number": 1, "artist": "Chastity Belt", "album": "No regrets", "location": "\Musica\llYwpqbjlhxA.128.mp3"},
            "King_Kunta":
                {"track-number": 3, "artist": "Kendrick Lamar", "album": "To Pimp A Butterfly", "location": "\Musica\Anastasia.mp3"},  
			"Hikari_no_senritsu":
				{"track-number": 2, "artist": "Karafina", "album": "Red Moon", "location": "\Musica\Hikari_no_senritsu.mp3"}
				
            }

# for i in range(1,1001):


# libreriaLista = []
# assert playSuffle(libreriaLista)



lanzarVLC(libreria, seleccionaCancionRandom(libreria, playList))