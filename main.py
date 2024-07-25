import pygame
import random


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
gameSpeed = 10
score = 0


class Snake():
    def __init__(self):
        self.bodyLength = 4
        self.coordinates = [[640,360]]
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
            pygame.draw.rect(screen, (0, 0, 0), [x,y, 30, 30])

        if len(self.coordinates) > self.bodyLength:
            self.coordinates.pop()

    def eat(self):
        self.bodyLength += 1
        self.score += 1

    def gameOver(self):
        print("Game Over")
        self.bodyLength = 0
        self.speed = 0

class Food():
    def __init__(self):
        self.x = random.randint(0, ((1280 // 30) - 1) * 30)
        self.y = random.randint(0, ((720 // 30) - 1) * 30)
        
    def generate(self):
        pygame.draw.rect(screen,(0, 0, 0), [self.x, self.y, 30, 30])

    def relocate(self):
        self.x = random.randint(0, ((1280 // 30) - 1) * 30)
        self.y = random.randint(0, ((720 // 30) - 1) * 30)

def display_text(screen, text, font_size, color, x_offset=screen.get_width() / 2, y_offset=screen.get_height() / 2,):

    font = pygame.font.SysFont(None, font_size)

    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()

    text_rect.midtop = (x_offset, y_offset)
    
    screen.blit(text_surface, text_rect)

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
    screen.fill((99, 181, 5))
    snake.move()



    if snake.coordinates[0][0] < food.x + 30 and snake.coordinates[0][0] + 40 > food.x and snake.coordinates[0][1] < food.y + 30 and snake.coordinates[0][1] + 30 > food.y:
        snake.eat()
        food.relocate()
        gameSpeed += 1
        score += 1

    if snake.coordinates[0][0] < 0 or snake.coordinates[0][0] > 1280 or snake.coordinates[0][1] < 0  or snake.coordinates[0][1] > 720:
        snake.gameOver()
        display_text(screen, f"Game Over! Your score was: {score}", 60, (0, 0, 0))

    for segment in snake.coordinates[1:]:
        if snake.direction and snake.coordinates[0] == segment:
            snake.gameOver()
            display_text(screen, f"Game Over! Your score was: {score}", 60, (0, 0, 0))


    food.generate()

    
    display_text(screen, f"Score: {score}", 40, (0, 0, 0), screen.get_width() / 2, 10)
    pygame.display.flip()


    dt = clock.tick(gameSpeed)

pygame.quit()