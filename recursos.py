__autor__='Stiven Cardona'

import pygame as py
from clases import *

def persecution(enemy,jugador):
	if jugador.rect.x>enemy.rect.x:
		enemy.var_x=8
        bl.dir=1
        bl.mover=True
        bl.combo=False
        bl.estatico=False
        bl.orien=True
	if jugador.rect.x<enemy.rect.x:
		enemy.var_x-=8
        bl.dir=1
        bl.mover=True
        bl.combo=False
        bl.estatico=False
        bl.orien=False
	if jugador.rect.x==enemy.rect.x:
		enemy.var_x-=8
        bl.dir=7
        bl.mover=False
        bl.combo=False
        bl.estatico=True