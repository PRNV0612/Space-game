import pygame
import random
pygame.init()


surface=pygame.display.set_mode((900,600))
gameRun=True
pygame.display.set_caption("guardians of the galaxy")
icon=pygame.image.load("galaxy.png")
pygame.display.set_icon(icon)


playerPic=pygame.image.load("player.png")
back=pygame.image.load("back.jpg")
playerX=64
playerY=300
playerVX=3

#numA is number of asteroids
numA=3
astImg=[]
astImgX=[]
astImgY=[]
astV=[]

astV.append(random.randint(1,4))
astImg.append(pygame.image.load("ast.png"))
astImgX.append(random.randint(600,836))
astImgY.append(random.randint(300,550))

for i in range(numA):

	astV.append(random.randint(1,4))
	astImg.append(pygame.image.load("ast.png"))
	astImgX.append(random.randint(200,836))
	astImgY.append(random.randint(200,550))

bulletImg=pygame.image.load("bullet.png")
bulletX=70
bulletY=300
bulletV=0
bulletVY=10
bulletState="ready"

def ast(x,y,i):
	surface.blit(astImg[i],(x,y))

def player(x,y):
	surface.blit(playerPic,(x,y))

def bullet(x,y,):
	global bulletState
	bulletState="fire"
	surface.blit(bulletImg,(x+16,y+10))





while gameRun:

	surface.fill((0,0,255))
	surface.blit(back,(0,0))
	for event in pygame.event.get():
		if (event.type==pygame.QUIT):
			gameRun=False
		keys=pygame.key.get_pressed()
	if keys[pygame.K_SPACE] and playerX> 0 and bulletState=="ready":
		bulletState="fire"
		bulletY=playerY
	if keys[pygame.K_UP] and playerY>0:
		playerY-=playerVX
	if keys[pygame.K_DOWN] and playerY<536:
		playerY+=playerVX

	for i in range(numA):

		if(astImgX[i]<-200):
			astImgX[i]=900
			astImgY[i]=random.randint(0,500)
 
		if (((astImgX[i]-playerX)**2)+(astImgY[i]-playerY)**2)**0.5<69:
			astImgX[i]=random.randint(200,836)
			astImgY[i]=random.randint(200,550)
			quit()

		if (((bulletX-astImgX[i])**2+(bulletY-astImgY[i])**2)**0.5) <=45:
			bulletState=="ready"
			astImgX[i]=900
			astImgY[i]=random.randint(0,500)

					
		else:
			astImgX[i]-=astV[i]
	
	if(bulletX>=900):
		bulletX=70
		bulletState="ready"

	if(bulletState=="fire"):
		bullet(bulletX,bulletY)
		bulletX+=bulletVY

	for i in range(numA):
		ast(astImgX[i],astImgY[i],i)
 
	player(playerX,playerY)

	pygame.display.update()


pygame.quit()
quit()