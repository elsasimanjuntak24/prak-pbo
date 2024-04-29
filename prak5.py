import pygame
import random

# Inheritance: Snake class inherits from pygame.sprite.Sprite
class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size = 20
        self.segments = [(200, 200)]
        self.dx = self.size
        self.dy = 0

    # Encapsulation: Methods to handle movement and drawing are encapsulated within the Snake class
    def move(self):
        x, y = self.segments[0]
        x += self.dx
        y += self.dy
        self.segments = [(x, y)] + self.segments[:-1]

    def grow(self):
        x, y = self.segments[-1]
        self.segments.append((x, y))

    def draw(self, surface):
        for segment in self.segments:
            pygame.draw.rect(surface, (0, 255, 0), (segment[0], segment[1], self.size, self.size))

    def check_collision(self):
        if self.segments[0] in self.segments[1:]:
            return True
        return False

# Polymorphism: Food class can be considered as a subclass of Snake, though not explicitly
class Food:
    def __init__(self):
        self.size = 20
        self.position = (random.randint(0, 39) * self.size, random.randint(0, 29) * self.size)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), (*self.position, self.size, self.size))

# Abstraction: Game class abstracts the main game logic
class Game:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.game_over = False

        pygame.init()
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Snake Game')

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.snake.dy != self.snake.size:
                    self.snake.dx = 0
                    self.snake.dy = -self.snake.size
                elif event.key == pygame.K_DOWN and self.snake.dy != -self.snake.size:
                    self.snake.dx = 0
                    self.snake.dy = self.snake.size
                elif event.key == pygame.K_LEFT and self.snake.dx != self.snake.size:
                    self.snake.dx = -self.snake.size
                    self.snake.dy = 0
                elif event.key == pygame.K_RIGHT and self.snake.dx != -self.snake.size:
                    self.snake.dx = self.snake.size
                    self.snake.dy = 0

    def check_collision(self):
        if (self.snake.segments[0][0] < 0 or self.snake.segments[0][0] >= self.width or
            self.snake.segments[0][1] < 0 or self.snake.segments[0][1] >= self.height or
            self.snake.check_collision()):
            self.game_over = True

    def check_eat(self):
        if self.snake.segments[0] == self.food.position:
            self.snake.grow()
            self.score += 1
            self.food.position = (random.randint(0, 39) * self.food.size, random.randint(0, 29) * self.food.size)

    def run(self):
        while not self.game_over:
            self.surface.fill((0, 0, 0))

            self.handle_events()

            self.snake.move()
            self.check_collision()
            self.check_eat()

            self.snake.draw(self.surface)
            self.food.draw(self.surface)

            pygame.display.update()
            self.clock.tick(10)

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()