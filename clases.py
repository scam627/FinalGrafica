__autor__='Stiven Cardona'

import pygame as pg
from constantes import *

class Bosque(pg.sprite.Sprite):
	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.name='Recursos/Mapas/forest.png'
		self.sheet=pg.image.load(self.name).convert_alpha()

class Fondo(Bosque):
	def __init__(self,x,y):
		Bosque.__init__(self)
		self.image=self.sheet.subsurface((12,13,512,512))
		self.rect=self.image.get_rect()
		self.x=x
		self.y=y
	def update(self):
		self.rect.x=self.x
		self.rect.y=self.y
class Arboles(Bosque):
	def __init__(self):
		Bosque.__init__(self)
		self.image=self.sheet.subsurface((11,547,630,250))
		self.rect=self.image.get_rect()
	def update(self):
		self.rect.x=0
		self.rect.y=0
class Prado(Bosque):
	def __init__(self):
		Bosque.__init__(self)
		self.image=self.sheet.subsurface((11,930,630,90))
		self.rect=self.image.get_rect()
	def update(self):
		self.rect.x=0
		self.rect.y=209
class Barranco(Bosque):
	def __init__(self):
		Bosque.__init__(self)
		self.image=self.sheet.subsurface((11,805,630,120))
		self.rect=self.image.get_rect()
	def update(self):
		self.rect.x=0
		self.rect.y=260

class Vidas(pg.sprite.Sprite):
	def __init__(self,x,y):
		pg.sprite.Sprite.__init__(self)
		self.name='Recursos/Objetos/vidas.png'
		self.sheet=pg.image.load(self.name).convert_alpha()
		self.existo=True
		self.rect=self.sheet.get_rect()
		self.get_mat()
		self.image=self.m[0][0]
		self.rect.x=x
		self.rect.y=y
	def get_mat(self):
		row_img=[]
		self.m=[]
		recorte=self.sheet.subsurface((0,0,72,96))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((74,0,72,96))
		row_img.append(recorte)
		self.m.append(row_img)
	def update(self):
		if self.existo:
			self.image=self.m[0][0]
		else:
			self.image=self.m[0][1]
class Enemyss(pg.sprite.Sprite):
    def __init__(self,d):
        pg.sprite.Sprite.__init__(self)
        self.name='Recursos/Personajes/enemy.png'
       	self.init_constantes()
       	self.init_bool_variables()
       	self.init_variables(d)

    def update(self):
        if self.mover :
        	self.movimiento()
    	if self.combo:  
    		self.animacion()
    	if self.golpeo:
    		self.golpe()
        if self.rect.x>=ANCHO-self.rect[2]:
            self.var_x=0
        if self.rect.x<=0:
            self.rect.x=0
            self.var_x=0
        if not self.orien:
        	if self.x<len(self.m[self.dir+8]):
    			self.image=self.m[self.dir+8][self.x]
    	else:
        	if self.x<len(self.m[self.dir+8]):
    			self.image=self.m[self.dir][self.x]

    def init_bool_variables(self):
    	print "Iniciando valores booleanos"
    	self.mover=False
    	self.golpeo=False
    	self.combo=True
    	self.orien=True

    def init_variables(self,d):
    	print "Iniciando valores variables"
    	self.my=d
    	self.salud=100
    	self.dir=0
    	self.x=0
    	self.get_mat()
    	self.image=self.m[self.dir][self.x]
        self.rect=self.image.get_rect()
        self.rect.y=self.my-self.image.get_size()[1]
        self.var_x=0

    def init_constantes(self):
    	print "Iniciando valores constantes"
    	self.gravedad=5
    	self.max_y_salto=112
    	self.sheet=pg.image.load(self.name).convert_alpha()

    def get_mat(self):
		ancho_img,alto_img=self.sheet.get_size()
		row_img=[]
		self.m=[]
		recorte=self.sheet.subsurface((0,319,34,40))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((36,319,34,40))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((72,319,34,40))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((108,319,34,40))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((0,361,42,41))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((44,361,42,41))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((88,361,42,41))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((132,361,42,41))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((175,361,42,41))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((218,361,42,41))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((0,404,32,48))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((0,454,33,40))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((35,454,33,40))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((0,496,32,32))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((0,530,42,30))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((44,530,42,30))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((88,530,42,30))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((132,530,42,30))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((0,562,32,32))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((0,596,50,40))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((52,596,50,40))
		row_img.append(recorte)    
		recorte=self.sheet.subsurface((104,596,50,40))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((156,596,50,40))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((571,319,34,40))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((535,319,34,40))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((499,319,34,40))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((463,319,34,40))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((563,361,42,41))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((519,361,42,41))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((475,361,42,41))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((431,361,42,41))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((387,361,42,41))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((343,361,42,41))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((573,404,32,48))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((572,454,33,40))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((537,454,33,40))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((573,496,32,32))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((563,530,42,30))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((519,530,42,30))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((475,530,42,30))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((431,530,42,30))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((573,562,32,32))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((555,596,50,40))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((503,596,50,40))
		row_img.append(recorte)    
		recorte=self.sheet.subsurface((451,596,50,40))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((399,596,50,40))
		row_img.append(recorte)
		self.m.append(row_img)
    
    def golpe(self):
    	if self.x<len(self.m[self.dir])-1:
    		self.x+=1
    	else:
    		self.x=0

    def movimiento(self):
    	self.rect.x+=self.var_x
    	self.rect.y=self.my-self.image.get_size()[1]
    	if self.x < len(self.m[self.dir])-1:
            self.x+=1
        else:
            self.x=0

    def animacion(self):
    	if self.x < len(self.m[self.dir])-1:
            self.x+=1
        else:
        	self.dir=0
        	self.x=0

class Enemys(pg.sprite.Sprite):
    def __init__(self,d):
        pg.sprite.Sprite.__init__(self)
        self.name='Recursos/Personajes/enemy.png'
       	self.init_constantes()
       	self.init_bool_variables()
       	self.init_variables(d)

    def update(self):
        if self.mover :
        	self.movimiento()
    	if self.combo:  
    		self.animacion()
    	if self.golpeo:
    		self.golpe()
        if self.rect.x>=ANCHO-self.rect[2]:
            self.var_x=0
        if self.rect.x<=0:
            self.rect.x=0
            self.var_x=0
        if not self.orien:
        	if self.x<len(self.m[self.dir+8]):
    			self.image=self.m[self.dir+8][self.x]
    	else:
        	if self.x<len(self.m[self.dir+8]):
    			self.image=self.m[self.dir][self.x]

    def init_bool_variables(self):
    	print "Iniciando valores booleanos"
    	self.mover=False
    	self.golpeo=False
    	self.combo=True
    	self.orien=True

    def init_variables(self,d):
    	print "Iniciando valores variables"
    	self.my=d
    	self.salud=50
    	self.dir=0
    	self.x=0
    	self.get_mat()
    	self.image=self.m[self.dir][self.x]
        self.rect=self.image.get_rect()
        self.rect.y=self.my-self.image.get_size()[1]
        self.var_x=0

    def init_constantes(self):
    	print "Iniciando valores constantes"
    	self.gravedad=5
    	self.max_y_salto=112
    	self.sheet=pg.image.load(self.name).convert_alpha()

    def get_mat(self):
		ancho_img,alto_img=self.sheet.get_size()
		row_img=[]
		self.m=[]
		recorte=self.sheet.subsurface((0,0,34,40))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((36,0,34,40))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((72,0,34,40))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((108,0,34,40))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((0,42,42,41))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((44,42,42,41))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((88,42,42,41))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((132,42,42,41))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((175,42,42,41))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((218,42,42,41))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((0,85,32,48))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((0,135,33,40))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((35,135,33,40))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((0,177,32,32))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((0,209,42,30))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((44,209,42,30))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((88,209,42,30))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((132,209,42,30))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((0,243,32,32))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((0,277,50,40))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((52,277,50,40))
		row_img.append(recorte)    
		recorte=self.sheet.subsurface((104,277,50,40))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((156,277,50,40))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((571,0,34,40))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((535,0,34,40))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((499,0,34,40))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((463,0,34,40))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((563,42,42,41))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((519,42,42,41))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((475,42,42,41))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((431,42,42,41))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((387,42,42,41))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((343,42,42,41))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((573,85,32,48))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((572,135,33,40))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((537,135,33,40))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((573,177,32,32))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((563,530,42,30))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((519,530,42,30))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((475,530,42,30))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((431,530,42,30))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((573,243,32,32))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((555,277,50,40))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((503,277,50,40))
		row_img.append(recorte)    
		recorte=self.sheet.subsurface((451,277,50,40))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((399,277,50,40))
		row_img.append(recorte)
		self.m.append(row_img)
    
    def golpe(self):
    	if self.x<len(self.m[self.dir])-1:
    		self.x+=1
    	else:
    		self.x=0

    def movimiento(self):
    	self.rect.x+=self.var_x
    	self.rect.y=self.my-self.image.get_size()[1]
    	if self.x < len(self.m[self.dir])-1:
            self.x+=1
        else:
            self.x=0

    def animacion(self):
    	if self.x < len(self.m[self.dir])-1:
            self.x+=1
        else:
        	self.dir=0
        	self.x=0

class Naruto(pg.sprite.Sprite):
    def __init__(self,d):
        pg.sprite.Sprite.__init__(self)
        self.name='Recursos/Personajes/naruto.png'
       	self.init_constantes()
       	self.init_bool_variables()
       	self.init_variables(d)

    def update(self):
        if self.mover :
        	self.movimiento()
    	if self.estatico:  
    		self.quieto()
        if self.rect.x>=ANCHO-self.rect[2]:
            self.var_x=0
        if self.rect.x<=0:
            self.rect.x=0
            self.var_x=0
        if not self.orien:
    		self.image=self.m[self.dir+13][self.x]
    	else:
    		self.image=self.m[self.dir][self.x]

    def init_bool_variables(self):
    	print "Iniciando valores booleanos"
    	self.mover=False
    	self.estatico=True
    	self.combo=False
    	self.orien=True
    	self.subir=False
    	self.caer=False

    def init_variables(self,d):
    	print "Iniciando valores variables"
    	self.my=d
    	self.salud=100
    	self.vidas=3
    	self.dir=11
    	self.x=0
    	self.get_mat()
    	self.image=self.m[self.dir][self.x]
        self.rect=self.image.get_rect()
        self.rect.y=self.my-self.image.get_size()[1]
        self.var_x=0

    def init_constantes(self):
    	print "Iniciando valores constantes"
    	self.gravedad=5
    	self.max_y_salto=112
    	self.sheet=pg.image.load(self.name).convert_alpha()

    def get_mat(self):
		self.ancho_img,self.alto_img=self.sheet.get_size()
		row_img=[]
		self.m=[]
		recorte=self.sheet.subsurface((0,0,56,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((58,0,56,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((116,0,56,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((174,0,56,48))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((0,50,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((50,50,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((100,50,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((150,50,48,48))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((0,100,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((50,100,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((100,100,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((150,100,48,48))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((0,150,40,56))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((42,150,40,56))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((84,150,40,56))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((126,150,40,56))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((168,150,40,56))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((0,208,40,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((42,208,40,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((84,208,40,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((126,208,40,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((168,208,40,48))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((0,258,48,52))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((50,258,48,52))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((100,258,48,52))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((150,258,48,52))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((0,312,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((50,312,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((100,312,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((150,312,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((200,312,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((250,312,48,48))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((0,362,32,40))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((0,404,32,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((34,404,32,48))
		row_img.append(recorte)    
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((0,454,40,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((42,454,40,48))
		row_img.append(recorte)    
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((0,504,32,56))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((34,504,32,56))
		row_img.append(recorte)    
		recorte=self.sheet.subsurface((68,504,32,56))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((102,504,32,56))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((0,562,32,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((34,562,32,48))
		row_img.append(recorte)    
		recorte=self.sheet.subsurface((68,562,32,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((102,562,32,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((136,562,32,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((170,562,32,48))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((0,612,40,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((40,612,40,48))
		row_img.append(recorte)    
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((910,0,56,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((852,0,56,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((794,0,56,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((736,0,56,48))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((918,50,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((868,50,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((818,50,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((768,50,48,48))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((918,100,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((868,100,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((818,100,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((768,100,48,48))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((926,150,40,56))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((884,150,40,56))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((842,150,40,56))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((800,150,40,56))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((758,150,40,56))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((926,208,40,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((884,208,40,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((842,208,40,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((800,208,40,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((758,208,40,48))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((918,258,48,52))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((868,258,48,52))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((818,258,48,52))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((768,258,48,52))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((918,312,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((868,312,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((818,312,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((768,312,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((718,312,48,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((668,312,48,48))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((934,362,32,40))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((934,404,32,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((900,404,32,48))
		row_img.append(recorte)    
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((926,454,40,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((884,454,40,48))
		row_img.append(recorte)    
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((934,504,32,56))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((900,504,32,56))
		row_img.append(recorte)    
		recorte=self.sheet.subsurface((866,504,32,56))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((832,504,32,56))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((934,562,32,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((900,562,32,48))
		row_img.append(recorte)    
		recorte=self.sheet.subsurface((866,562,32,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((832,562,32,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((798,562,32,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((764,562,32,48))
		row_img.append(recorte)
		self.m.append(row_img)
		row_img=[]
		recorte=self.sheet.subsurface((926,612,40,48))
		row_img.append(recorte)
		recorte=self.sheet.subsurface((884,612,40,48))
		row_img.append(recorte)    
		self.m.append(row_img)


    def movimiento(self):
    	self.rect.x+=self.var_x
    	self.rect.y=self.my-self.image.get_size()[1]
    	if self.x < len(self.m[self.dir])-1:
            self.x+=1
        else:
            self.x=0

    def quieto(self):
    	if self.x < len(self.m[self.dir])-1:
            self.x+=1
        else:
            self.x=0

