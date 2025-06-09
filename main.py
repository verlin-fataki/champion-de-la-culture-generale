import pygame
import sys

# Initialisation de pygame
pygame.init()

# Definir le dimension de la fenetre 
WIDTH = 1000
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Champions de la Culture Générale") 

# Definir les couleurs(RGB)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0, 0)
GREY = (200, 200, 200)
BLUE = (100, 149, 237)
GREEN = (0, 128, 0)

# Chargement de l'image du fond
fond = pygame.image.load("assets/Champion.png").convert()
fond = pygame.transform.scale(fond, (WIDTH, HEIGHT))

# Definir la police pour le texte
police = pygame.font.Font("assets/White Paper.otf", 50)

# Transition du fond d'ecran
def fond_trasition(fond_one, fond_two, duration=1000):
	clock = pygame.time.Clock()
	for alpha in range(0, 256, 10):
		screen.blit(fond_one, (0, 0))
		fondu = fond_two.copy()
		fondu.set_alpha(alpha)
		screen.blit(fondu, (0, 0))
		pygame.display.flip()
		clock.tick(60)

# Animation de l'introduction
def animation():
	for alpha in range(0, 256, 5):
		screen.blit(fond, (0, 0))
		surface = pygame.Surface((WIDTH, HEIGHT))
		surface.set_alpha(255 - alpha)
		surface.fill(WHITE)
		screen.blit(surface, (0, 0))
		pygame.display.flip()
		pygame.time.delay(30)


# Bouton START
class Bouton:
	def __init__(self, x, y, width, height, texte):
		self.rect = pygame.Rect(x, y, width, height)
		self.texte = texte

	def showing(self):
		#pygame.draw.rect(screen, GREY, self.rect)
		#pygame.draw.rect(screen, BLACK, self.rect, 2)
		texte_render = police.render(self.texte, True, WHITE)
		texte_rect = texte_render.get_rect(center = self.rect.center)
		screen.blit(texte_render, texte_rect)

	def click(self, pos):
		return self.rect.collidepoint(pos)

# Menu principal
def main_Menu():
	#fond_menu = pygame.image.load("assets/fond.png").convert()
	#fond_menu = pygame.transform.scale(fond_menu, (WIDTH, HEIGHT))

	# Les trois(3) boutons alignes horizontalement
	boutons = [
		Bouton(100, 400, 200, 50, "JOUER"),
		Bouton(400, 400, 200, 50, "VOIR SCORES"),
		Bouton(700, 400, 200, 50, "QUITTER")
	]

	in_menu = True
	while in_menu:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			elif event.type == pygame.MOUSEBUTTONDOWN:
				if boutons[0].click(event.pos):
					print("Jouer")
					in_menu = False

				elif boutons[1].click(event.pos):
					print("Voir scores")
				elif boutons[2].click(event.pos):
					pygame.quit()
					sys.exit()

		screen.blit(fond, (0, 0))
		title = police.render("Menu principal", True, BLACK)
		screen.blit(title, (WIDTH//2 - title.get_width() // 2, 100))

		for bouton in boutons:
			bouton.showing()

		pygame.display.flip()
	


# Creer une boucle principale
def main_loop():

	startBouton = Bouton(WIDTH // 2 -80, 460,200, 50, "COMMENCONS")
	animation()

	running = True

	while running:
		# Gérer les événements clavier / souris
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

			elif event.type == pygame.MOUSEBUTTONDOWN:
				if startBouton.click(event.pos):
					fond_menu = pygame.image.load("assets/fond.png").convert()
					fond_menu = pygame.transform.scale(fond_menu, (WIDTH, HEIGHT))
					fond_trasition(fond, fond_menu)
					main_Menu()
					running = False


		# Afficher un fond 
		screen.blit(fond, (0,  0))

		# Affichage de notre texte de bienvenue et le boutton
		texte_welcome = police.render("Bienvenue dans le jeu !", True, WHITE)
		texte_rect = texte_welcome.get_rect(center=(WIDTH // 2, 400))
		screen.blit(texte_welcome, texte_rect)
		startBouton.showing()

		# Mettre en jour laffichage
		pygame.display.flip()

	pygame.quit()
	sys.exit()

# Lancement de la boucle
if __name__ == "__main__":

	main_loop()

