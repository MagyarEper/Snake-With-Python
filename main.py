# Example file showing a circle moving on screen
import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0


class Snake():
    def __init__(self):
        self.bodyLength = 4
        self.coordinates = [[0,0]]
        self.direction = None
        self.speed = 30
        self.score = 0
 

    def move(self):
        x,y = self.coordinates[0]
        if self.direction == "w":
            y -= self.speed
        elif self.direction == "s":
            y += self.speed
        elif self.direction == "a":
            x -= self.speed
        elif self.direction == "d":
            x += self.speed
        
        self.coordinates.insert(0,(x,y))
        for x,y in self.coordinates:
            pygame.draw.rect(screen, 'black', [x,y, 30, 30])

        if len(self.coordinates) > self.bodyLength:
            self.coordinates.pop()

    def eat(self):
        self.bodyLength += 1
        self.score += 1
        self.speed += 1

class Food():
    def __init__(self):
        self.x = random.randint(0, ((1280 // 30) - 1) * 30)
        self.y = random.randint(0, ((720 // 30) - 1) * 30)
        
    def generate(self):
        pygame.draw.rect(screen,'yellow', [self.x, self.y, 30, 30])

    def relocate(self):
        self.x = random.randint(0, 1280)
        self.y = random.randint(0, 720)

snake = Snake()
food = Food()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and snake.direction != "s":
        snake.direction = "w"
    if keys[pygame.K_s] and snake.direction != "w":
        snake.direction = "s"
    if keys[pygame.K_a] and snake.direction != "d":
        snake.direction = "a"
    if keys[pygame.K_d] and snake.direction != "a":
        snake.direction = "d"
    screen.fill("gray")
    snake.move()

    print(snake.coordinates[0][0], snake.coordinates[0][1])


    if snake.coordinates[0][0] < food.x + 30 and snake.coordinates[0][0] + 40 > food.x and snake.coordinates[0][1] < food.y + 30 and snake.coordinates[0][1] + 30 > food.y:
        snake.eat()
        food.relocate()
        print("kowabunga")

    food.generate()

    # flip() the display to put your work on screen
    pygame.display.flip()


    dt = clock.tick(10)

pygame.quit()