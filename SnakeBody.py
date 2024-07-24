import pygame

class Segment():
    def __init__(self, x, y, number):
        self.x = x
        self.y = y
        self.number = number
        self.next = None


class SnakeBody():
    def __init__(self, screen):
        self.head = None
        self.direction = None
        self.speed = 5
        self.screen = screen

    
    def grow(self):
        if not self.head:
            new_segment = Segment(self.screen.get_width() / 2, self.screen.get_height() / 2, 0)
            self.head = new_segment
            return
        
        last_segment = self.head
        while last_segment.next:
            last_segment = last_segment.next
        new_segment = Segment(last_segment.x, last_segment.y, last_segment.number + 1)
        last_segment.next = new_segment

    def changeDirection(self, direction):
        self.direction = direction
    
    def move(self):
        coords = (self.head.x, self.head.y)

        last_segment = self.head

        while last_segment.next:
            if (last_segment.x, last_segment.y) == coords:
                if self.direction == "w":
                    last_segment.y -= (self.speed - last_segment.number * 0.5)
                    last_segment = last_segment.next

                elif self.direction == "s":
                    last_segment.y += (self.speed - last_segment.number * 0.5)
                    last_segment = last_segment.next

                elif self.direction == "d":
                    last_segment.x += (self.speed - last_segment.number * 0.5)
                    last_segment = last_segment.next

                elif self.direction == "a":
                    last_segment.x -= (self.speed - last_segment.number * 0.5)
                    last_segment = last_segment.next
            last_segment = last_segment.next
            
    def drawBody(self, screen):
        last_segment = self.head
        while last_segment.next:
            pygame.draw.circle(screen, "red", (last_segment.x, last_segment.y), 40)
            last_segment = last_segment.next