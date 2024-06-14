from tkinter import *
from tkinter import messagebox
from random import randrange
import time
import os

# Fonction principale du jeu

def move() :
	global x, y, a, b, direction, pX, pY, z, speed, warp, temps, tx, ty, temps_restant, tr, porte_v, porte_b, porte_g, porte_o, tmontre, key

	if direction == 'gauche':
		if x>a :	
			direction = 'droite' # Empêche de faire un demi-tour
		else :
			a = x
			x = x - dx # Permet le déplacement
			b = y

	# On fait la même pour chaque direction	
	elif direction == 'droite':
		if x<a :
			direction = "gauche"
		else :
			a = x
			x = x + dx
			b = y
		
	elif direction == 'haut':
		if y>b :
			direction = "bas"
		else :
			b = y
			y = y - dy
			a = x
	elif direction == 'bas':
		if y<b :
			direction = "haut"
		else :
			b = y
			y = y + dy
			a = x


	# Déplacement des personnages
	can.coords(perso, x, y, x+dx, y+dy)
	
	can.coords(perso2, a, b, a+dx, b+dy)

	### Détection de collision ###
			

	### Détection des portails ###

	# Téléportation du joueur : chaque fonction téléporte à un portail spécifique
	def tp_rouge() :
		global x, y, a, b, direction
		if direction == 'haut' :
			x = can.coords(p_rouge)[0] + (can.coords(p_rouge)[2] - can.coords(p_rouge)[0]) / 2
			y = can.coords(p_rouge)[1] - 15
			a = x 
			b = y + dy
		elif direction == 'bas' :
			x = can.coords(p_rouge)[0] + (can.coords(p_rouge)[2] - can.coords(p_rouge)[0]) / 2
			y = can.coords(p_rouge)[3] + 15
			a = x 
			b = y - dy
		elif direction == 'gauche' :
			x = can.coords(p_rouge)[0] - 15
			y = can.coords(p_rouge)[1] + (can.coords(p_rouge)[3] - can.coords(p_rouge)[1]) / 2
			a = x + dx
			b = y
		elif direction == 'droite' :
			x = can.coords(p_rouge)[2] + 15
			y = can.coords(p_rouge)[1] + (can.coords(p_rouge)[3] - can.coords(p_rouge)[1]) / 2
			a = x - dx
			b = y

	def tp_vert() :
		global x, y, a, b, direction
		if direction == 'haut' :
			x = can.coords(p_vert)[0] + (can.coords(p_vert)[2] - can.coords(p_vert)[0]) / 2
			y = can.coords(p_vert)[1] - 15
			a = x 
			b = y + dy
		elif direction == 'bas' :
			x = can.coords(p_vert)[0] + (can.coords(p_vert)[2] - can.coords(p_vert)[0]) / 2
			y = can.coords(p_vert)[3] + 15
			a = x 
			b = y - dy
		elif direction == 'gauche' :
			x = can.coords(p_vert)[0] - 15 
			y = can.coords(p_vert)[1] + (can.coords(p_vert)[3] - can.coords(p_vert)[1]) / 2
			a = x + dx
			b = y
		elif direction == 'droite' :
			x = can.coords(p_vert)[2] + 15
			y = can.coords(p_vert)[1] + (can.coords(p_vert)[3] - can.coords(p_vert)[1]) / 2
			a = x - dx
			b = y

	def tp_bleu() :
		global x, y, a, b, direction
		if direction == 'haut' :
			x = can.coords(p_bleu)[0] + (can.coords(p_bleu)[2] - can.coords(p_bleu)[0]) / 2
			y = can.coords(p_bleu)[1] - 15
			a = x
			b = y + dy
		elif direction == 'bas' :
			x = can.coords(p_bleu)[0] + (can.coords(p_bleu)[2] - can.coords(p_bleu)[0]) / 2
			y = can.coords(p_bleu)[3] + 15
			a = x 
			b = y - dy
		elif direction == 'gauche' :
			x = can.coords(p_bleu)[0] - 15 
			y = can.coords(p_bleu)[1] + (can.coords(p_bleu)[3] - can.coords(p_bleu)[1]) / 2
			a = x + dx
			b = y
		elif direction == 'droite' :
			x = can.coords(p_bleu)[2] + 15
			y = can.coords(p_bleu)[1] + (can.coords(p_bleu)[3] - can.coords(p_bleu)[1]) / 2
			a = x - dx
			b = y

	def tp_noir() :
		global x, y, a, b, direction
		if direction == 'haut' :
			x = can.coords(p_noir)[0] + (can.coords(p_noir)[2] - can.coords(p_noir)[0]) / 2
			y = can.coords(p_noir)[1] - 15
			a = x 
			b = y + dy
		elif direction == 'bas' :
			x = can.coords(p_noir)[0] + (can.coords(p_noir)[2] - can.coords(p_noir)[0]) / 2
			y = can.coords(p_noir)[3] + 15
			a = x 
			b = y - dy
		elif direction == 'gauche' :
			x = can.coords(p_noir)[0] - 15 
			y = can.coords(p_noir)[1] + (can.coords(p_noir)[3] - can.coords(p_noir)[1]) / 2
			a = x + dx
			b = y
		elif direction == 'droite' :
			x = can.coords(p_noir)[2] + 15
			y = can.coords(p_noir)[1] + (can.coords(p_noir)[3] - can.coords(p_noir)[1]) / 2
			a = x - dx
			b = y


    # Détection des portails et téléportation selon une logique
	if len(can.find_overlapping(can.coords(p_rouge)[0], can.coords(p_rouge)[1], can.coords(p_rouge)[2], can.coords(p_rouge)[3])) > 1:
		if warp == 1 :
			tp_vert()

		elif warp == 2 :
			tp_bleu()

		elif warp == 3 :
			tp_noir()

		warp +=1

	if len(can.find_overlapping(can.coords(p_vert)[0], can.coords(p_vert)[1], can.coords(p_vert)[2], can.coords(p_vert)[3])) > 1:
		if warp == 1 :
			tp_bleu()

		elif warp == 2 :
			tp_noir()

		elif warp == 3 :
			tp_rouge()
			
		warp +=1



	if len(can.find_overlapping(can.coords(p_bleu)[0], can.coords(p_bleu)[1], can.coords(p_bleu)[2], can.coords(p_bleu)[3])) > 1:
		if warp == 1 :
			tp_noir()

		elif warp == 2 :
			tp_rouge()

		elif warp == 3 :
			tp_vert()
			
		warp +=1

	if len(can.find_overlapping(can.coords(p_noir)[0], can.coords(p_noir)[1], can.coords(p_noir)[2], can.coords(p_noir)[3])) > 1:
		if warp == 1 :
			tp_rouge()

		elif warp == 2 :
			tp_vert()

		elif warp == 3 :
			tp_bleu()
			
		warp +=1

	if warp>3 :
		warp = 1


	# Détection des murs
	list_perso = can.find_overlapping(*can.coords(perso)) 
	colors = [can.itemcget(id, 'fill') for id in list_perso] # Création d'une liste avec toutes les couleurs d'où se trouve le perso
	list_perso2 = can.find_overlapping(*can.coords(perso)) 
	colors2 = [can.itemcget(id, 'outline') for id in list_perso2]
	list_pomme = can.find_overlapping(*can.coords(pomme))
	colors_pomme = [can.itemcget(id, 'fill') for id in list_pomme] # Liste des couleurs de la pomme
	list_pomme2 = can.find_overlapping(*can.coords(pomme2))
	colors_pomme2 = [can.itemcget(id, 'fill') for id in list_pomme2]
	list_pomme3 = can.find_overlapping(*can.coords(pomme3))
	colors_pomme3 = [can.itemcget(id, 'fill') for id in list_pomme3]


	# Change la direction du joueur lorsqu'il y a collision avec un mur
	if 'grey' in colors :
		if direction == 'droite':
			a = x
			x = x - dx
		elif direction == 'gauche' :
			a = x
			x = x + dx
		elif direction == 'haut' :
			b = y
			y = y + dy
		elif direction == 'bas':
			b = y
			y = y - dy

	if 'grey' in colors2 :
		if direction == 'droite':
			a = x
			x = x - dx
		elif direction == 'gauche' :
			a = x
			x = x + dx
		elif direction == 'haut' :
			b = y
			y = y + dy
		elif direction == 'bas':
			b = y
			y = y - dy		

	# Détection des objets
	
	# Montre jaune
	if 'yellow' in colors :
		if tmontre == 1:
			can.coords(montre, 325, 17, 335, 27)
			tr += 10
			tmontre += 1

		elif tmontre == 2:
			can.coords(montre, 485, 570, 495, 580)
			tr += 10
			tmontre += 1

		elif tmontre == 3:
			can.delete('montre')
			tr += 10
			tmontre += 1

	# Piège
	if "#6AE082" in colors :
		can.create_rectangle(125, 105, 165, 120, outline='grey', fill='grey')
		can.create_rectangle(55, 55, 165, 105, outline='green', fill='green')
		can.delete('piege')

	if "#64FFE3" in colors :
		can.delete("montre_piege")
		time.sleep(5.0)

	# Clef
	if "#FEB121" in colors :
		can.delete('clef')
		key = True

	# Détection des leviers et ouverture des portes

	# Levier orange
	if "orange" in colors :
		if porte_o :
			can.coords(levier_orange, 1260, 570, 1265, 590)
			can.create_rectangle(610, 260, 625, 310, outline='grey', fill='#FF7F0D', width=3, tag='porte_orange2')
			can.delete('porte_orange')
			porte_o = False

		elif not porte_o :
			can.coords(levier_orange, 1230, 570, 1235, 590)
			can.create_rectangle(1070, 350, 1110, 365, outline ='grey', fill='#FF7F0D', width=3, tag='porte_orange')
			can.delete('porte_orange2')
			porte_o = True
	
	# Levier violet
	if "purple" in colors :
		if porte_v :
			can.coords(porte_violet, 165, 0, 180, 40)
			can.coords(levier_violet, 395, 360, 400, 380)
			can.delete('porte_violet3')
			can.create_rectangle(40, 425, 55, 485, outline='grey', fill='#9033B3', width=3, tag="porte_violet2")
			porte_v = False
			
		elif not porte_v :
			can.coords(porte_violet, 300, 135, 315, 170)
			can.coords(levier_violet, 365, 360, 370, 380)
			can.delete("porte_violet2")
			can.create_rectangle(1215, 485, 1280, 500, outline='grey', fill='#9033B3', width=3, tag='porte_violet3')
			porte_v = True

	# Levier marron
	if "brown" in colors:
		if porte_b :
			can.delete("porte_marron")
			can.coords(levier_marron, 265, 467, 285, 472)
			can.delete('porte_marron3')
			can.move(porte_marron2, 0, 92)
			can.coords(porte_marron4, 755, 650, 770, 720)
			porte_b = False

		elif not porte_b :
			can.create_rectangle(0, 540, 40, 555, outline='grey', fill='#BB6533' , width=3, tag="porte_marron" )
			can.coords(levier_marron, 265, 437, 285, 442)
			can.move(porte_marron2, 0, -92)
			can.create_rectangle(1145, 600, 1200, 615, outline='grey', fill='#BB6533', width=3, tag='porte_marron3')
			can.coords(porte_marron4, 770, 635, 885, 650,)
			porte_b = True


	# Levier gris
	if "#BAB8B6" in colors :
		if porte_g :
			can.coords(levier_gris, 485, 53, 505, 58)
			can.delete('porte_gris3')
			can.move(porte_gris, 145, 0)
			porte_g = False

		elif not porte_g :
			can.coords(levier_gris, 485, 28, 505, 33)
			can.move(porte_gris, -145, 0)
			can.create_rectangle(1215, 665, 1280, 680, outline='grey', fill='#D5D3D2', width=3, tag='porte_gris3')
			porte_g = True

	# Bouton vert
	if "#20B33D" in colors :
		can.delete("laser")
		can.delete(bouton_vert)

	
	# Déplace les pommes si elles apparaîssent sur un mur /// Possibilité de faire pour tous les autres obstacles également mais trop long
	if 'grey' in colors_pomme :
		pX = randrange(250, 1055)
		pY = randrange (95, 625)
		can.coords(pomme, pX, pY, pX+10, pY+10)
		z += 10 # Rééquilibre la vitesse car elle augmente vu qu'il y a collision

	if 'grey' in colors_pomme2 :
		pX = randrange(250, 1055)
		pY = randrange (95, 625)
		can.coords(pomme2, pX, pY, pX+10, pY+10)
		z += 10

	if 'grey' in colors_pomme3 :
		pX = randrange(250, 1055)
		pY = randrange (95, 625)
		can.coords(pomme3, pX, pY, pX+10, pY+10)		
		z += 10


	# Détection des pommes /// Vitesse initiale aléatoire à cause de collision avec des objets autres que le personnage
	if len(can.find_overlapping(can.coords(pomme)[0], can.coords(pomme)[1], can.coords(pomme)[2], can.coords(pomme)[3])) > 1 :
		pX = randrange(250, 1055)
		pY = randrange (95, 625)
		can.coords(pomme, pX, pY, pX+10, pY+10)
		if z > 45:
			speed = 1
		if speed != 0:
			z -= 10 # Augmente la vitesse une fois la pomme mangée
			if z < 45:
				speed = 0


	if len(can.find_overlapping(can.coords(pomme2)[0], can.coords(pomme2)[1], can.coords(pomme2)[2], can.coords(pomme2)[3])) > 1 :
		pX = randrange(250, 1055)
		pY = randrange (95, 625)
		can.coords(pomme2, pX, pY, pX+10, pY+10)
		if z > 45:
			speed = 1
		if speed != 0:
			z -= 10 # Augmente la vitesse une fois la pomme mangée
			if z < 45:
				speed = 0		
				
	if len(can.find_overlapping(can.coords(pomme3)[0], can.coords(pomme3)[1], can.coords(pomme3)[2], can.coords(pomme3)[3])) > 1 :
		pX = randrange(250, 1055)
		pY = randrange (95, 625)
		can.coords(pomme3, pX, pY, pX+10, pY+10)
		if z > 45:
			speed = 1
		if speed != 0:
			z -= 10 # Augmente la vitesse une fois la pomme mangée
			if z < 45:
				speed = 0	

	# Laser vert
	if "green" in colors :
		tr -= 5
	
	# Portail de sortie 
	if "#B4FFAC" in colors :
		if not key :
			x = 20
			y = 375
			a = x - dx
			b = y
			Label(fen, text='Vous avez besoin de la clef pour sortir !').pack(side=TOP, padx =5, pady=5)
		elif key :
			# Création de la page de fin
			can.delete("all")
			can.create_rectangle(360, 100, 960, 720, outline='#C79312', fill = '#FFBB14')
			can.create_rectangle(400, 300, 420, 600, outline='#C26400', fill = '#F07B00')
			can.create_rectangle(500, 300, 520, 600, outline='#C26400', fill = '#F07B00')
			can.create_rectangle(680, 300, 700, 600, outline='#C26400', fill = '#F07B00')
			can.create_rectangle(830, 300, 850, 600, outline='#C26400', fill = '#F07B00')
			can.create_rectangle(420, 300, 500, 320, outline='#C26400', fill = '#F07B00')
			can.create_rectangle(420, 420, 500, 440, outline='#C26400', fill = '#F07B00')
			can.create_rectangle(600, 300, 680, 320, outline='#C26400', fill = '#F07B00')
			can.create_rectangle(600, 420, 680, 440, outline='#C26400', fill = '#F07B00')
			can.create_rectangle(600, 580, 680, 600, outline='#C26400', fill = '#F07B00')
			can.create_rectangle(770, 300, 910, 320, outline='#C26400', fill = '#F07B00')
			can.create_text(650, 160, text="Bravo ! Vous avez trouvé la stèle cachée !", justify='center')

	### Timer ###


	temps = time.time()

	# Toutes les 20 secondes, le personnage ralentit
	if tx < temps - temps_debut < ty :
		z += 10
		tx += 20
		ty += 20
		if z > 130 :
			z = 130

	# Temps écoulé : game over
	if temps - temps_debut > tr :
		result = messagebox.askyesno('Temps écoulé !', 'Vous avez perdu, voulez-vous recommencer ?')
		# Relance le jeu si "oui" sinon ferme le jeu
		if result :
			os.startfile("maze.py") 
			fen.destroy()
		if not result :
			fen.destroy()

	# Affichage du temps restant à l'écran
	temps_restant = tr - int(temps - temps_debut)
	can.delete('text')
	can.create_text(1220, 15, text='Temps restant : %ss' % (temps_restant), tag = 'text', fill='#CA0000')



	if flag != 0 : 
		fen.after(z, move) # Après un certain temps z en millisecondes, relance la fonction move


# Fonction pour lancer le jeu
def newgame():

	global flag, temps_debut

	if flag == 0:
		temps_debut = time.time()
		flag = 1
		move() # Met la valeur 1 à flag, ce qui empêche de relancer la fonction move (qui va accélérer le jeu)

# Fonction pour lancer le jeu avec le bouton espace du clavier
def space(event):
	newgame()

# On associe chaque touche à une fonction et à une direction
def left(event):
	global direction
	direction = 'gauche'

def right(event):
	global direction
	direction = 'droite'

def up(event):
	global direction
	direction = 'haut'

def down(event):
	global direction
	direction = 'bas'


# Entrée des variables
x = 20
y = 375
z=70 # Vitesse initiale /// Varie un peu de manière aléatoire
dx, dy = 10, 10 # Taille des personnages
tx, ty = 19.85, 20 # Temps initial pour la perte de vitesse
tr = 300 # Temps de jeu
a = x - dx
b = y
flag = 0
speed = 1
warp = 1
tmontre = 1
porte_v = True
porte_b = True
porte_g = True
porte_o = True
key = False
direction = None

# Règles
def rules() :
	messagebox.showinfo(
'Règles du jeu :',
'Vous devez trouver le trésor de ce labyrinthe le plus vite possible. Vous perdez de la vitesse petit à petit à cause de la fatigue. Mangez des pommes pour regagner des forces. Utilisez les flèches du clavier pour vous déplacer.\nAttention aux collisions !')

def items():
	messagebox.showinfo(
'Objets :', 
'Pommes rouges : gagner de la vitesse.\nMontre jaune : gagner du temps. \nLaser vert : fait perdre du temps. \nLeviers : ouvrir des portes. \nClef : accès à la sortie. \nPortails : téléportation. \nRonds : vous.\n+ quelques surprises.' )

### Tkinter ###
fen = Tk()
fen.title("A Maze Ingame")
can = Canvas(fen, width=1280, height=720, bg='#FFFAAC')
can.pack(side=TOP, padx=5, pady=5)

# Création des bordures
can.create_rectangle(1, 1, 1280, 1, outline='grey', fill = 'grey', width=5)
can.create_rectangle(1, 720, 1280, 720, outline='grey', fill = 'grey', width = 2)
can.create_rectangle(1, 1, 1, 720, outline='grey', fill = 'grey', width=5)
can.create_rectangle(1280, 1, 1280, 720, outline='grey', fill = 'grey', width = 2)

# Création des obstacles/murs
can.create_rectangle(0, 410, 625, 425, outline ='grey', fill='grey')
can.create_rectangle(885, 410, 1280, 425, outline ='grey', fill='grey' )
can.create_rectangle(445, 0, 460, 670, outline ='grey', fill='grey')
can.create_rectangle(610, 310, 625, 720, outline ='grey', fill='grey')
can.create_rectangle(40, 368, 270, 383, outline ='grey', fill='grey')
can.create_rectangle(985, 250, 1000, 410, outline='grey', fill='grey')
can.create_rectangle(985, 250, 1200, 265, outline='grey', fill='grey')
can.create_rectangle(1185, 60, 1200, 365, outline='grey', fill='grey')
can.create_rectangle(985, 350, 1070, 365, outline='grey', fill='grey')
can.create_rectangle(1110, 350, 1200, 365, outline='grey', fill='grey')
can.create_rectangle(0, 320, 180, 335, outline='grey', fill='grey')
can.create_rectangle(220, 320, 320, 335, outline='grey', fill='grey')
can.create_rectangle(40, 275, 180, 290, outline='grey', fill='grey')
can.create_rectangle(165, 40, 180, 290, outline='grey', fill='grey')
can.create_rectangle(0, 225, 125, 240, outline='grey', fill='grey')
can.create_rectangle(305, 320, 320, 600, outline='grey', fill='grey')
can.create_rectangle(40, 170, 400, 185, outline='grey', fill='grey')
can.create_rectangle(220, 225, 235, 325, outline='grey', fill='grey')
can.create_rectangle(275, 275, 400, 290, outline='grey', fill='grey')
can.create_rectangle(325, 180, 340, 250, outline='grey', fill='grey')
can.create_rectangle(385, 90, 400, 170, outline='grey', fill='grey')
can.create_rectangle(300, 40, 400, 55, outline='grey', fill='grey')
can.create_rectangle(40, 40, 170, 55, outline='grey', fill='grey')
can.create_rectangle(40, 105, 125, 120, outline='grey', fill='grey')
can.create_rectangle(40, 40, 55, 120, outline='grey', fill='grey')
can.create_rectangle(40, 485, 320, 500, outline='grey', fill='grey')
can.create_rectangle(170, 590, 320, 605, outline='grey', fill='grey')
can.create_rectangle(170, 590, 185, 690, outline='grey', fill='grey')
can.create_rectangle(100, 675, 185, 690, outline='grey', fill='grey')
can.create_rectangle(40, 540, 55, 690, outline='grey', fill='grey')
can.create_rectangle(40, 540, 255, 555, outline='grey', fill='grey')
can.create_rectangle(300, 0, 315, 135, outline='grey', fill='grey')
can.create_rectangle(373, 470, 388, 720, outline='grey', fill='grey')
can.create_rectangle(527, 470, 542, 720, outline='grey', fill='grey')
can.create_rectangle(460, 250, 770, 265, outline='grey', fill='grey')
can.create_rectangle(460, 170, 650, 185, outline='grey', fill='grey')
can.create_rectangle(460, 80, 650, 95, outline='grey', fill='grey')
can.create_rectangle(755, 170, 770, 650, outline='grey', fill='grey')
can.create_rectangle(755, 0, 770, 95, outline='grey', fill='grey')
can.create_rectangle(1130, 485, 1145, 720, outline='grey', fill='grey')
can.create_rectangle(1200, 540, 1215, 680, outline='grey', fill='grey')
can.create_rectangle(1130, 485, 1215, 500, outline='grey', fill='grey')
can.create_rectangle(1215, 540, 1280, 555, outline='grey', fill='grey')
can.create_rectangle(885, 0, 900, 350, outline='grey', fill='grey')
can.create_rectangle(885, 555, 1145, 570, outline='grey', fill='grey')
can.create_rectangle(885, 570, 900, 650, outline='grey', fill='grey')


# Création des lasers
can.create_rectangle(760, 95, 765, 170, outline='green', fill='green', tag='laser')
can.create_rectangle(1200, 95, 1280, 100, outline='green', fill='green', tag='laser')
can.create_rectangle(1200, 140, 1280, 145, outline='green', fill='green', tag='laser')
can.create_rectangle(1200, 185, 1280, 190, outline='green', fill='green', tag='laser')
can.create_rectangle(1200, 235, 1280, 240, outline='green', fill='green', tag='laser')
can.create_rectangle(1200, 285, 1280, 280, outline='green', fill='green', tag='laser')
can.create_rectangle(1200, 330, 1280, 335, outline='green', fill='green', tag='laser')
can.create_rectangle(1150, 365, 1155, 410, outline='green', fill='green', tag='laser')

# Création des portes
porte_violet = can.create_rectangle(300, 135, 315, 170, outline='grey', fill='#9033B3', width=3)
porte_violet3 = can.create_rectangle(1215, 485, 1280, 500, outline='grey', fill='#9033B3', width=3, tag='porte_violet3')
porte_marron = can.create_rectangle(0, 540, 40, 555, outline='grey', fill='#BB6533' , width=3, tag="porte_marron" )
porte_marron2 = can.create_rectangle(635, 0, 650, 80, outline='grey', fill='#BB6533', width=3, tag="porte_marron2")
porte_marron3 = can.create_rectangle(1145, 600, 1200, 615, outline='grey', fill='#BB6533', width=3, tag='porte_marron3')
porte_marron4 = can.create_rectangle(770, 635, 885, 650, outline='grey', fill='#BB6533', width=3, tag='porte_marron4')
porte_gris = can.create_rectangle(625, 410, 755, 425, outline='grey', fill='#D5D3D2', width=3)
porte_gris3 = can.create_rectangle(1215, 665, 1280, 680, outline='grey', fill='#D5D3D2', width=3, tag='porte_gris3')
porte_orange = can.create_rectangle(1070, 350, 1110, 365, outline ='grey', fill='#FF7F0D', width=3, tag='porte_orange')

# Création des objets

# Leviers
can.create_rectangle(360, 355, 405, 385, outline='#887B7B', fill="#887B7B")
levier_violet = can.create_rectangle(365, 360, 370, 380, outline='white', fill='purple')
can.create_rectangle(260, 432, 290, 477, outline='#887B7B', fill="#887B7B")
levier_marron = can.create_rectangle(265, 437, 285, 442, outline='white', fill='brown')
can.create_rectangle(480, 23, 510, 63, outline='#887B7B', fill="#887B7B")
levier_gris = can.create_rectangle(485, 28, 505, 33, outline='white', fill='#BAB8B6')
can.create_rectangle(1225, 565, 1270, 595, outline='#887B7B', fill="#887B7B")
levier_orange = can.create_rectangle(1230, 570, 1235, 590, outline='white', fill='orange')
can.create_rectangle(560, 685, 590, 705, outline='#887B7B', fill="#887B7B")
bouton_vert = can.create_rectangle(570, 690, 580, 700, outline='white', fill='#20B33D')

# Pommes
pX = randrange(250, 1055)
pY = randrange (95, 625)
pomme = can.create_oval(pX, pY, pX+10, pY+10, outline='green', fill='red')
pX = randrange(250, 1055)
pY = randrange (95, 625)
pomme2 = can.create_oval(pX, pY, pX+10, pY+10, outline='green', fill='red')
pX = randrange(250, 1055)
pY = randrange (95, 625)
pomme3 =can.create_oval(pX, pY, pX+10, pY+10, outline='green', fill='red')

# Autres
montre = can.create_oval(485, 212, 495, 222, outline='orange', fill='yellow', width=2, tag='montre')
montre_piege = can.create_oval(485, 125, 495, 135, outline='#64DEFF', fill='#64FFE3', width=2, tag='montre_piege')
piege = can.create_oval(70, 77, 80, 87, fill='#6AE082', tag='piege')
clef = can.create_rectangle(1087, 280, 1093, 300, outline="#FCFF33", fill="#FEB121", width=2, tag='clef')


# Création des portails
p_rouge = can.create_oval(215, 59, 245, 89, outline='red', fill='#C4FFF6')
p_vert = can.create_oval(1060, 59, 1090, 89, outline='green', fill='#C4FFF6')
p_bleu = can.create_oval(1060, 632, 1090, 662, outline='blue', fill='#C4FFF6')
p_noir = can.create_oval(215, 632, 245, 662, outline='black', fill='#C4FFF6')	
p_sortie = can.create_oval(510, 320, 560, 360, outline='#FF7878', fill='#B4FFAC', width='2')	


# Création des personnages
perso = can.create_oval(x, y, x+dx, y+dy, outline='black', fill='blue')
perso2 = can.create_oval(a, b, a+dx, b+dy, outline='black', fill='pink')

# Timer
can.create_rectangle(1155, 0, 1280, 30, outline='grey', fill='grey' )
can.create_text(1220, 15, text='Temps restant : %ss' % (tr), tag = 'text', fill="#CA0000")

# Menu du bas
Button(fen, text="Commencer", bg="pink", command=newgame).pack(side=LEFT, padx=5, pady=5)
Button(fen, text='Règles', bg='pink', command=rules).pack(side=LEFT, padx=5, pady=5)
Button(fen, text='Objets', bg='pink', command=items).pack(side=LEFT, padx=5, pady=5)
Label(fen, text='Appuyez sur le bouton Commencer ou sur la touche espace pour lancer le jeu.').pack(side=LEFT, padx =5, pady=5)
fen.bind('<Right>', right)
fen.bind('<Left>', left)
fen.bind('<Up>', up)
fen.bind('<Down>', down)
fen.bind('<space>', space)
fen.mainloop()
