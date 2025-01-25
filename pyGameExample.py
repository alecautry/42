import pygame
import random

# this class is a container for 
# our game state and all the sprites
class Game:
    def __init__(self, font):
        self.font = font
        # currently we have 2 states: RUNNING and SELECT_POSITION
        self.state = 'RUNNING'

        # a sprite group for all sprites (+ UI)
        self.sprites = pygame.sprite.Group()

        # a sprite group for all game objects (- UI)
        self.actors = pygame.sprite.Group()
        self.callback = None

    def update(self, events, dt):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:

                # if we're in SELECT_POSITION, a mouse click will
                # change the game state back to RUNNING
                # we pass the mouse position to the callback
                # so the action actually happens
                if self.state == 'SELECT_POSITION' and self.callback:
                    self.callback(event.pos)
                    self.state = 'RUNNING'

        # just update the sprites
        self.sprites.update(events, dt)

    def draw(self, screen):
        # usually, the background is black, but to give the player 
        # a visual clue that they have to do something, let's change
        # it to grey when we're in the SELECT_POSITION mode
        screen.fill(pygame.Color('black' if self.state == 'RUNNING' else 'grey'))

        # just draw all the sprites
        self.sprites.draw(screen)

        # just some info text for the player
        if self.state == 'SELECT_POSITION':
            screen.blit(self.font.render('Select a position', True, pygame.Color('black')), (150, 400))

    # a button can call this function when the action that should be invoked
    # needs a position that the player has to choose
    def select_position(self, callback):
        self.state = 'SELECT_POSITION'
        self.callback = callback

# just a little square guy that walks around the screen
# nothing special happens here
class WalkingRect(pygame.sprite.Sprite):
    def __init__(self, pos, color, game):
        super().__init__(game.sprites, game.actors)
        self.image = pygame.Surface((32, 32))
        self.image.fill(pygame.Color(color))
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.Vector2(pos)
        self.direction = pygame.Vector2(random.choice([-1,0,1]), random.choice([-1,1])).normalize()

    def update(self, events, dt):
        self.pos += self.direction * dt/10
        self.rect.center = self.pos
        if random.randint(0, 100) < 10:
            self.direction = pygame.Vector2(random.choice([-1,0,1]), random.choice([-1,1])).normalize()

# the actuall Button class
# it takes an action that is invoked when the player clicks it
class Button(pygame.sprite.Sprite):
    def __init__(self, pos, color, text, game, action):
        super().__init__(game.sprites)
        self.color = color
        self.action = action
        self.game = game
        self.text = text
        self.image = pygame.Surface((150, 40))
        self.rect = self.image.get_rect(topleft=pos)
        self.fill_surf(self.color)

    def fill_surf(self, color):
        self.image.fill(pygame.Color(color))
        self.image.blit(self.game.font.render(self.text, True, pygame.Color('White')), (10, 10))

    def update(self, events, dt):

        # the player can only use the button when the game is in the RUNNING state
        if self.game.state != 'RUNNING':
            self.fill_surf('darkgrey')
            return

        self.fill_surf(self.color)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    # if the player clicked the button, the action is invoked
                    self.action(self.game)

def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    screen_rect = screen.get_rect()
    font = pygame.font.SysFont(None, 26)
    clock = pygame.time.Clock()

    game = Game(font)

    # the action for the green button
    # when invoked, as the game for the player
    # to select a position, and spawn a green
    # guy at that position
    def green_action(game_obj):
        def create_green(pos):
            WalkingRect(pos, 'green', game_obj)
        game_obj.select_position(create_green)

    # the same but spawn a red guy instead
    def red_action(game_obj):
        def create_red(pos):
            WalkingRect(pos, 'darkred', game_obj)
        game_obj.select_position(create_red)

    Button((10, 10), 'green', 'CREATE GREEN', game, green_action)
    Button((10, 50), 'darkred', 'CREATE RED', game, red_action)

    # a button to kill all guys
    # just to show how generic our buttons are
    Button((10, 90), 'red', 'KILL', game, lambda game_obj: [x.kill() for x in game_obj.actors])

    # classic boring main loop
    # just updates and draws the game
    dt = 0
    while True:
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                return

        game.update(events, dt)
        game.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)

if __name__ == '__main__':
    main()