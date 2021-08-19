import pygame
import mixer 
import button
import random
#menginisialisasi pygame
pygame.init()

#timernya
#waktu = pygame.time.Clock()
#waktukini = 0
#buttontime = 0
#membuat screen baru berbentuk potrait
screen = pygame.display.set_mode((400,600))
screensize = (400,600)
screen.fill((202,228,241))
pygame.display.set_caption('Game Prevention Covid')

#Sound
pygame.mixer.music.load("bgm.wav")
pygame.mixer.music.play(-1)
boxSound = pygame.mixer.Sound("box.wav")


#Load asset
font = pygame.font.Font('BaksoSapi.otf', 32)
fontGO = pygame.font.Font('BaksoSapi.otf', 20)
masker_img = pygame.image.load('masker.png').convert_alpha()
vitamin_img = pygame.image.load('vitamin.png').convert_alpha()
handsanitizer_img = pygame.image.load('handsanitizer.png').convert_alpha()
termogun_img = pygame.image.load('termogun.png').convert_alpha()
makanansehat_img = pygame.image.load('makanansehat.png').convert_alpha()
tisu_img = pygame.image.load('tisu.png').convert_alpha()
bawahImg = pygame.image.load('gray.png').convert_alpha()
bg = pygame.image.load('pink.png').convert_alpha()
konsumen1 = pygame.image.load('orang 1.png').convert_alpha()
konsumen2 = pygame.image.load('orang 2.png').convert_alpha()
konsumen3 = pygame.image.load('orang 3.png').convert_alpha()
konsumen4 = pygame.image.load('orang 4.png').convert_alpha()
bgstart = pygame.image.load('bgstart.png').convert_alpha()
startbut = pygame.image.load('start.png').convert_alpha()
backbut = pygame.image.load('back.png').convert_alpha()
#variable
completeMisi=0
skor=0
timer = 5000
start = True
highscore = 0

main = False
gover = False

#class button
class Button():
	def __init__(self, x,y,image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				boxSound.play()
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action

def show_score(x, y):
    score = font.render("Score : "+str(skor), True, (38, 28, 44))
    screen.blit(score, (x, y))

def show_go(x, y):
    score = font.render("Score : "+str(skor), True, (38, 28, 44))
    hiscore = font.render("High Score : "+str(highscore), True, (38, 28, 44))
    screen.blit(score, (x, y))
    screen.blit(hiscore, (x, y+70))

masker_button = Button(50,370, masker_img, 0.2)	
vitamin_button = Button(160,370, vitamin_img, 0.2)	
handsanitizer_button = Button(270,370, handsanitizer_img, 0.2)	
termogun_button = Button(50,480, termogun_img, 0.2)	
makanansehat_button = Button(160,480, makanansehat_img, 0.2)	
start_button = Button(160,480, startbut, 0.3)
back_button = Button(160,480, backbut, 0.3)	
tisu_button = Button(270,480, tisu_img, 0.2)	
sizeMisi = (70,70)
sizePlayer = (240, 300)

misi1 = random.randrange(0,6)

misi2 = random.randrange(0,6)
noorang = random.randrange(0,4)
	#kondisi tampilkan misi
running = True
while running:
	#waktukini = pygame.time.get_ticks()
	#screen.fill((202,228,241))
	if start==True:
		screen.blit(pygame.transform.scale(bgstart, screensize), (0, 0))
		if start_button.draw(screen):
			start=False
			gover=False
			main = True
								
	if main ==True and start==False:
		screen.blit(bg, (0, 0))
		if noorang==0:
			screen.blit(pygame.transform.scale(konsumen1, sizePlayer), (130, 100))
		elif noorang==1:
			screen.blit(pygame.transform.scale(konsumen2, sizePlayer), (130, 100))
		elif noorang==2:
			screen.blit(pygame.transform.scale(konsumen3, sizePlayer), (130, 100))
		elif noorang==3:
			screen.blit(pygame.transform.scale(konsumen4, sizePlayer), (130, 100))

		screen.blit(bawahImg, (0, 350))

		if misi1 == 0:
			screen.blit(pygame.transform.scale(masker_img, sizeMisi), (50, 100))
		elif misi1 == 1:
			screen.blit(pygame.transform.scale(vitamin_img, sizeMisi), (50, 100))
		elif misi1 == 2:
			screen.blit(pygame.transform.scale(handsanitizer_img, sizeMisi), (50, 100))
		elif misi1 == 3:
			screen.blit(pygame.transform.scale(termogun_img, sizeMisi), (50, 100))
		elif misi1 == 4:
			screen.blit(pygame.transform.scale(makanansehat_img, sizeMisi), (50, 100))
		elif misi1 == 5:
			screen.blit(pygame.transform.scale(tisu_img, sizeMisi), (50, 100))

		if misi2 == 0:
			screen.blit(pygame.transform.scale(masker_img, sizeMisi), (50, 180))
		elif misi2 == 1:
			screen.blit(pygame.transform.scale(vitamin_img, sizeMisi), (50, 180))
		elif misi2 == 2:
			screen.blit(pygame.transform.scale(handsanitizer_img, sizeMisi), (50, 180))
		elif misi2 == 3:
			screen.blit(pygame.transform.scale(termogun_img, sizeMisi), (50, 180))
		elif misi2 == 4:
			screen.blit(pygame.transform.scale(makanansehat_img, sizeMisi), (50, 180))
		elif misi2 == 5:
			screen.blit(pygame.transform.scale(tisu_img, sizeMisi), (50, 180))

		if masker_button.draw(screen):
			if misi1==0:
				screen.blit(pygame.transform.scale(bg, sizeMisi), (50, 100))
				misi1 = 6
				completeMisi +=1

			elif misi2==0:
				screen.blit(pygame.transform.scale(bg, sizeMisi), (50, 180))
				misi2 = 6
				completeMisi +=1
			else :
				main=False
				gover=True


		elif vitamin_button.draw(screen):
			if misi1==1:
				screen.blit(pygame.transform.scale(bg, sizeMisi), (50, 100))
				misi1 = 6
				completeMisi +=1

			elif misi2==1:
				screen.blit(pygame.transform.scale(bg, sizeMisi), (50, 180))
				misi2 = 6
				completeMisi +=1
			else :
				main=False
				gover=True
		elif handsanitizer_button.draw(screen):
			if misi1==2:
				screen.blit(pygame.transform.scale(bg, sizeMisi), (50, 100))
				misi1 = 6
				completeMisi +=1

			elif misi2==2:
				screen.blit(pygame.transform.scale(bg, sizeMisi), (50, 180))
				misi2 = 6
				completeMisi +=1
			else :
				main=False
				gover=True

		elif termogun_button.draw(screen):
			if misi1==3:
				screen.blit(pygame.transform.scale(bg, sizeMisi), (50, 100))
				misi1 = 6
				completeMisi +=1

			elif misi2==3:
				screen.blit(pygame.transform.scale(bg, sizeMisi), (50, 180))
				misi2 = 6
				completeMisi +=1
			else :
				main=False
				gover=True

		elif makanansehat_button.draw(screen):
			if misi1==4:
				screen.blit(pygame.transform.scale(bg, sizeMisi), (50, 100))
				misi1 = 6
				completeMisi +=1

			elif misi2==4:
				screen.blit(pygame.transform.scale(bg, sizeMisi), (50, 180))
				misi2 = 6
				completeMisi +=1
			else :
				main=False
				gover=True

		elif tisu_button.draw(screen):
			if misi1==5:
				screen.blit(pygame.transform.scale(bg, sizeMisi), (50, 100))
				misi1 = 6
				completeMisi +=1

			elif misi2==5:
				screen.blit(pygame.transform.scale(bg, sizeMisi), (50, 180))
				misi2 = 6
				completeMisi +=1
			else :
				main=False
				gover=True

		if completeMisi==2:
			skor+=1
			completeMisi=0
			noorang = random.randrange(0,4)
			misi1 = random.randrange(0,6)
			misi2 = random.randrange(0,6)

		show_score(10, 10)
	
	if gover==True and start==False:
		if skor>highscore:
			highscore=skor				

		screen.blit(bawahImg, (0, 0))
		show_go(100,150)

		if back_button.draw(screen):
			skor=0
			start=True
			main=False
			gover=False
			completeMisi=0
			misi1 = random.randrange(0,6)
			misi2 = random.randrange(0,6)
			screen.blit(pygame.transform.scale(bg, sizeMisi), (50, 100))
			screen.blit(pygame.transform.scale(bg, sizeMisi), (50, 180))
		

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			skor=0
			start=True
			main=False
			gover=False
			completeMisi=0

	
	#waktu.tick(1)
	pygame.display.update()
