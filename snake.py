import pygame
import snakeObj
import random

pygame.init()
pygame.font.init()

winX, winY = 450, 450
window = pygame.display.set_mode((winX, winY))
pygame.display.set_caption("Snek")

font = pygame.font.Font("freesansbold.ttf", 20)
text = font.render("Move to start", True, (0, 0, 255))
textRect = text.get_rect()
textRect.center = (winX // 2, winY // 3)
	
def generatePos(direction, gridX, gridY): # 0 = x, 1 = y
	openX, openY = [], []
	for i in range(len(gridX)):
		if gridX[i]:
			openX.append(i)
		if gridY[i]:
			openY.append(i)
	newPos = random.choice(openY) * height
	if direction == 0:
		newPos = random.choice(openX) * width
	return newPos

def mainMenu():
	window.fill((0, 0, 0))
	window.blit(text, textRect)
	pygame.draw.rect(window, (255, 0, 0), (x, y, width, height))
	pygame.display.update()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
		keys = pygame.key.get_pressed()
		if any(keys):
			break;

def paused():
	text = font.render("Press Space to Resume", True, (0, 0, 255))
	textRect.center = (winX // 2, winY // 3)
	window.fill((0, 0, 0))
	window.blit(text, textRect)
	pygame.draw.rect(window, (255, 0, 0), (x, y, width, height))
	for each in head.body:
		pygame.draw.rect(window, (255, 0, 0), (each[0], each[1], width, height))
	pygame.draw.rect(window, (255, 208, 0), (itemX, itemY, width, height))
	pygame.display.update()

	pygame.time.delay(100)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE]:
			break;

#rect stuff
x = 0
y = 0
width = 15
height = 15
speed = 15
head = snakeObj.Snake([x, y], width, height)

#direction movement
up, down, left, right = 0, 0, 0, speed

#item generation
gridX, gridY = [True] * (winX // width), [True] * (winY // height)
itemX, itemY = generatePos(0, gridX, gridY), generatePos(1, gridX, gridY)

alive = True
mainMenu()
while alive:
	pygame.time.delay(80)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

	keys = pygame.key.get_pressed()

	if keys[pygame.K_UP]:
		up, down, left, right = 0, 0, 0, 0
		up = -speed
	if keys[pygame.K_LEFT]:
		up, down, left, right = 0, 0, 0, 0
		left = -speed
	if keys[pygame.K_DOWN]:
		up, down, left, right = 0, 0, 0, 0
		down = speed
	if keys[pygame.K_RIGHT]:
		up, down, left, right = 0, 0, 0, 0
		right = speed
	if keys[pygame.K_p]:
		paused()

	#movement & boundaries
	x = (x + left + right) % winX
	y = (y + up + down) % winY

	#current direction
	currDirection = -1
	if left + right == 0 and up + down < 0:
		currDirection = 0
	elif left + right == 0 and up + down > 0:
		currDirection = 1
	elif up + down == 0 and left + right < 0:
		currDirection = 2
	elif up + down == 0 and left + right > 0:
		currDirection = 3

	#snake current tiles
	gridX, gridY = [True] * (winX // width), [True] * (winY // height)
	bodyLength = head.length() - 1
	snakeX, snakeY = [x // width], [y // height]
	gridX[x // width] = False
	gridY[y // height] = False
	for i in range(bodyLength):
		snakeX.append(head.body[i][0] // width)
		snakeY.append(head.body[i][1] // height)
		gridX[head.body[i][0] // width] = False
		gridY[head.body[i][1] // height] = False

	# body collision
	for i in range(bodyLength):
		if abs(x - head.body[i][0]) < width and abs(y - head.body[i][1]) < height:
			alive = False

	if not alive:
		break;

	head.updatePos(x, y)

	# item collision
	if abs(x-itemX) < width and abs(y-itemY) < height:
		head.grow(currDirection, winX, winY)
		itemX, itemY = generatePos(0, gridX, gridY), generatePos(1, gridX, gridY)


	window.fill((0, 0, 0))

	#item
	pygame.draw.rect(window, (255, 208, 0), (itemX, itemY, width, height))

	#snake draw
	pygame.draw.rect(window, (255, 0, 0), (x, y, width, height))
	for each in head.body:
		pygame.draw.rect(window, (255, 0, 0), (each[0], each[1], width, height))
	pygame.display.update()

# death
text = font.render("You lose :(", True, (0, 0, 255))
textRect.center = (winX // 3, winY // 3)
window.fill((0, 0, 0))
window.blit(text, textRect)
pygame.draw.rect(window, (255, 0, 0), (x, y, width, height))
for each in head.body:
	pygame.draw.rect(window, (255, 0, 0), (each[0], each[1], width, height))
pygame.draw.rect(window, (255, 208, 0), (itemX, itemY, width, height))
pygame.display.update()

pygame.quit()

