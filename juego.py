from main import *
from constantes import *
from clases import *

if __name__=='__main__':
	pygame.init()
	pygame.display.set_caption('Naruto ninja')
	pantalla=pygame.display.set_mode([ANCHO,ALTO])
	reloj=pygame.time.Clock()
	pygame.mixer.music.load('Recursos/Sonidos/fondo.mp3')
	pygame.mixer.music.play(1)
	while not ACABAR:
		for event in pygame.event.get():
			if event.type==pygame.MOUSEBUTTONDOWN:
				if pygame.mouse.get_pressed() == (1,0,0):
					if (pygame.mouse.get_pos()[0]>250 and pygame.mouse.get_pos()[0] < 515) and (pygame.mouse.get_pos()[1]>180 and pygame.mouse.get_pos()[1] < 300):
						jugar=pygame.image.load('Recursos/Objetos/jugar_2.png')
						pantalla.blit(jugar,[250,180])
						pygame.display.flip()
						JUGAR=True
						reloj.tick(1) 
			if event.type==pygame.QUIT:
				print "Adios"
				ACABAR=True
			else:
				if JUGAR:
					number=level_one(pantalla)
					if number[0]> 0:
						JUGAR=False
						pasar(pantalla)
						reloj.tick(1)
						reloj.tick(1)
						reloj.tick(1)
						reloj.tick(1)
						level_two(pantalla,number[0],number[1],number[2])
					else:
						JUGAR=False	
						portada(pantalla)
				else:
					portada(pantalla)