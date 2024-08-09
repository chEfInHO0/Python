import pygame
import random
from consts import WIDTH, HEIGHT, COIN_COLOR, OBSTACLE_COLOR, PLATFORM_COLOR, PLATFORM_HEIGHT,PLAYER_COLOR,XP_BAR_COLOR,XP_COLOR
# Inicialização do Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
####################  PLAYER  #############################

class Player(pygame.sprite.Sprite):
    def __init__(self, platform):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect()
        self.current_platform = platform
        self.rect.x = self.current_platform.rect.left + 16
        self.rect.y = self.current_platform.rect.top - self.rect.height
        self.can_move = True
        self.speed = 5
        self.max_spawn_time = 3000
        self.min_spawn_time = 1000
        self.last_object_time = 0
        self.level = 1
        self.xp = 0
        self.gold = 0
        self.current_level = 1

        # Power-ups
        self.xp_boost_level = 0
        self.gold_boost_level = 0
        self.shield_level = 0
        self.speed_boost = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.can_move:
            self.move_to_platform(self.current_platform, "up")
            self.can_move = False
        elif keys[pygame.K_DOWN] and self.can_move:
            self.move_to_platform(self.current_platform, "down")
            self.can_move = False
        elif not keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
            self.can_move = True            

    def move_to_platform(self, current_platform, direction):
        if direction == "up" and current_platform != platform_1:
            self.current_platform = self.get_upper_platform(current_platform)
        elif direction == "down" and current_platform != platform_3:
            self.current_platform = self.get_lower_platform(current_platform)
        
        self.rect.x = self.current_platform.rect.left + 16
        self.rect.y = self.current_platform.rect.top - self.rect.height

    def get_upper_platform(self, current_platform):
        if current_platform == platform_2:
            return platform_1
        elif current_platform == platform_3:
            return platform_2

    def get_lower_platform(self, current_platform):
        if current_platform == platform_1:
            return platform_2
        elif current_platform == platform_2:
            return platform_3

############################################################################

def game_over(screen, score, player):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    game_over_text = font.render("Game Over", True, (255, 255, 255))
    score_text = font.render(f"Score: {score.value}", True, (255, 255, 255))
    gold_text = font.render(f"Gold: {player.gold}", True, COIN_COLOR)
    level_text = font.render(f"Level: {player.level}", True, XP_COLOR)
    restart_text = font.render("Press R to Restart", True, (255, 255, 255))
    game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
    score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    gold_rect = gold_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    level_rect = level_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))
    screen.blit(game_over_text, game_over_rect)
    screen.blit(score_text, score_rect)
    screen.blit(gold_text, gold_rect)
    screen.blit(level_text, level_rect)
    screen.blit(restart_text, restart_rect)
    pygame.display.flip()


# Dentro da função para renderizar o texto do nível:
def draw_level_text(screen, player):
    font = pygame.font.Font(None, 36)
    level_text = font.render(f"Level: {player.level}", True, XP_COLOR)
    gold_text = font.render(f"Gold: {player.gold}", True, COIN_COLOR)
    text_rect = level_text.get_rect()
    text_rect.centerx = WIDTH // 2
    text_rect.bottom = xp_bar.rect.top - 10

    gold_rect = gold_text.get_rect()
    gold_rect.centerx = WIDTH // 2
    gold_rect.bottom = text_rect.top - 10

    screen.blit(level_text, text_rect)
    screen.blit(gold_text, gold_rect)



##############################################################################
class Platform(pygame.sprite.Sprite):
    def __init__(self, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((WIDTH, PLATFORM_HEIGHT))
        self.image.fill(PLATFORM_COLOR)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.centery = y

    def update(self):
        pass
##############################################################################

class ShopCard(pygame.sprite.Sprite):
    def __init__(self, power_up_name, level, price, color, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.power_up_name = power_up_name
        self.level = level
        self.price = price
        self.color = color
        self.image = pygame.Surface((100, 100))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

    def draw(self, screen):
        font = pygame.font.Font(None, 24)
        text = font.render(f"{self.power_up_name} - Level {self.level}", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.centerx = self.rect.centerx
        text_rect.centery = self.rect.centery + 60

        price_text = font.render(f"Price: {self.price}", True, (255, 255, 255))
        price_rect = price_text.get_rect()
        price_rect.centerx = self.rect.centerx
        price_rect.centery = self.rect.centery + 80

        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)
        screen.blit(self.image, self.rect)
        screen.blit(text, text_rect)
        screen.blit(price_text, price_rect)


# Classe do objeto em movimento
class MovingObject(pygame.sprite.Sprite):
    def __init__(self, platform, color, size, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.y = platform.rect.y - self.rect.height
        self.speed = speed
        self.platform = platform

    def update(self):
        self.rect.x -= self.speed

# Classe do obstáculo
class Obstacle(MovingObject):
    def __init__(self, platform, size, speed):
        super().__init__(platform, OBSTACLE_COLOR, size, speed)

# Classe Coin
class Coin(MovingObject):
    def __init__(self, platform, size, speed):
        super().__init__(platform, COIN_COLOR, size, speed)

    def update(self):
        self.rect.x -= player.speed
        if self.rect.right < 0:
            self.kill()

# Classe XP
class XP(MovingObject):
    def __init__(self, platform, size, speed):
        super().__init__(platform, XP_COLOR, size, speed)

    def update(self):
        self.rect.x -= player.speed
        if self.rect.right < 0:
            self.kill()


# Classe do score
class Score:
    def __init__(self):
        self.value = 0
        self.high_score = 0
        self.font = pygame.font.Font(None, 36)
        self.text = self.font.render("Score: 0", True, (255, 255, 255))
        self.text_rect = self.text.get_rect()
        self.text_rect.topleft = (10, 10)

    def add_point(self):
        self.value += 1
        if self.value > self.high_score:
            self.high_score = self.value
        self.text = self.font.render(f"Score: {self.value}", True, (255, 255, 255))

    def draw(self, screen):
        screen.blit(self.text, self.text_rect)

    def reset(self):
        self.value = 0
        self.text = self.font.render("Score: 0", True, (255, 255, 255))

# Classe da barra de XP
class XPBar(pygame.sprite.Sprite):
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        self.player = player
        self.image = pygame.Surface((WIDTH, 10))
        self.image.fill(XP_BAR_COLOR)
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.bottom = HEIGHT

    def update(self):
        xp_percentage = self.player.xp / self.player.level * 10
        bar_width = int((xp_percentage / 100) * WIDTH)
        self.image = pygame.Surface((bar_width, 10))
        self.image.fill(XP_BAR_COLOR)
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.bottom = HEIGHT


# Inicialização do jogo
platform_1 = Platform(HEIGHT // 2 - 100)
platform_2 = Platform(HEIGHT // 2)
platform_3 = Platform(HEIGHT // 2 + 100)
player = Player(platform_2)
moving_objects = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(platform_1, platform_2, platform_3, player)
score = Score()
xp_bar = XPBar(player)
all_sprites.add(xp_bar)
shop_cards = []
in_shop = False

def render_shop():
    screen.fill((0, 0, 0))  # Preenche a tela com preto
    font = pygame.font.Font(None, 36)
    title_text = font.render("Power-up Shop", True, (255, 255, 255))
    gold_text = font.render(f"Gold: {player.gold}", True, COIN_COLOR)
    title_rect = title_text.get_rect()
    gold_rect = gold_text.get_rect()
    title_rect.centerx = WIDTH // 2
    title_rect.centery = HEIGHT // 2 - 150
    gold_rect.centerx = WIDTH // 2
    gold_rect.centery = HEIGHT // 2 - 100
    screen.blit(title_text, title_rect)
    screen.blit(gold_text, gold_rect)

    # Renderiza os cards dos power-ups
    for card in shop_cards:
        card.draw(screen=screen)
    pygame.display.flip()
def card_position_calc(cards):
    card_width = 150
    card_spacing = 50

    screen_width = pygame.display.get_surface().get_width()

    # Calcula o espaço horizontal total ocupado pelas quatro cartas e o espaçamento entre elas
    total_width = (card_width * cards) + (card_spacing * (cards-1))
    x_start = (screen_width - 13*total_width/16) // 2

    # Calcula a posição X de cada carta
    positions_x = [x_start + (card_width + card_spacing) * i for i in range(cards)]

    # Retorna uma lista de tuplas contendo as posições X e Y de cada carta
    return [(x, HEIGHT // 2) for x in positions_x]

def generate_shop_cards(player):
    shop_cards.clear()
    # Define as posições para renderizar os cards
    card_positions = card_position_calc(4)

    # Cria os cards para cada power-up e adiciona à lista de shop_cards
    xp_boost_card = ShopCard("XP Boost", player.xp_boost_level, 10 * (player.xp_boost_level + 1),
                             (255, 0, 0), *card_positions[0])
    gold_boost_card = ShopCard("Gold Boost", player.gold_boost_level, 10 * (player.gold_boost_level + 1),
                               (0, 255, 0), *card_positions[1])
    shield_card = ShopCard("Shield", player.shield_level, 50 * (player.shield_level + 1),
                           (0, 0, 255), *card_positions[2])
    speed_card = ShopCard("Speed", player.speed, 5,
                           (0, 255, 255), *card_positions[3])

    shop_cards.append(xp_boost_card)
    shop_cards.append(gold_boost_card)
    shop_cards.append(shield_card)
    shop_cards.append(speed_card)

# Função para reiniciar o jogo
def reset_game():
    score.reset()
    player.speed = 5
    player.min_spawn_time = 1000
    player.max_spawn_time = 3000
    player.last_object_time = 0
    player.level = 1
    player.xp = 0
    player.gold = 0
    player.gold_boost_level = 0
    player.xp_boost_level = 0
    player.shield_level = 0
    player.rect.x = platform_2.rect.left + 16
    player.rect.y = platform_2.rect.top - player.rect.height
    xp_bar.image = pygame.Surface((0, 10))
    xp_bar.image.fill(XP_BAR_COLOR)
    xp_bar.rect = xp_bar.image.get_rect()
    xp_bar.rect.left = 0
    xp_bar.rect.bottom = HEIGHT

    for obj in moving_objects:
        obj.kill()

# Loop principal do jogo
running = True
game_over_screen = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            # Verifica se algum card foi clicado
            for card in shop_cards:
                if card.rect.collidepoint(mouse_pos):
                    # Realiza a compra do power-up
                    if card.power_up_name == "XP Boost" and player.gold > card.price:
                        player.xp_boost_level += 1
                    elif card.power_up_name == "Gold Boost" and player.gold > card.price:
                        player.gold_boost_level += 1
                    elif card.power_up_name == "Shield" and player.gold > card.price:
                        player.shield_level += 1
                    elif card.power_up_name == "Speed" and player.gold > card.price:
                        player.speed += 1
                        player.min_spawn_time -= 10
                        player.max_spawn_time -= 20
                        for obj in moving_objects:
                            obj.speed = player.speed

                    if player.gold > card.price:
                        player.gold -= card.price  # Subtrai o preço do ouro do jogador
                        # Fecha a loja e continua o jogo
                        in_shop = False
                        generate_shop_cards(player)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and in_shop:
                in_shop = not in_shop
            elif event.key == pygame.K_r and game_over_screen:
                reset_game()
                game_over_screen = False

    if not game_over_screen and not in_shop:
        current_time = pygame.time.get_ticks()
        if current_time - player.last_object_time > random.randint(player.min_spawn_time, player.max_spawn_time):
            if random.random() < 0.5:
                moving_object = Obstacle(random.choice([platform_1, platform_2, platform_3]), (player.rect.width, player.rect.height), player.speed)
                moving_objects.add(moving_object)
                all_sprites.add(moving_object)
                player.last_object_time = current_time
            else:
                object_type = random.choices(["coin", "xp"], weights=[0.30, 0.20])[0]
                if object_type == "coin":
                    moving_object = Coin(random.choice([platform_1, platform_2, platform_3]), (20, 20), player.speed)
                elif object_type == "xp":
                    moving_object = XP(random.choice([platform_1, platform_2, platform_3]), (20, 20), player.speed)
                moving_objects.add(moving_object)
                all_sprites.add(moving_object)
                player.last_object_time = current_time

        # Verifica colisão entre o jogador e os obstáculos
        collisions = pygame.sprite.spritecollide(player, moving_objects, True)
        for collision in collisions:
            if isinstance(collision, Obstacle):
                if player.shield_level <= 0:
                    game_over_screen = True
                    game_over(screen, score, player)
                    break
                else:
                    player.shield_level -= 1
            elif isinstance(collision, Coin):
                player.gold += 1 + player.gold_boost_level
            elif isinstance(collision, XP):
                player.xp += 1 + player.xp_boost_level
                if player.xp >= player.level * 10:
                    player.xp = 0
                    player.level += 1
                    player.speed += player.level
                    player.min_spawn_time -= player.level*10
                    player.max_spawn_time -= player.level*10
                    for obj in moving_objects:
                            obj.speed = player.speed
                    in_shop = True
        # Atualizações
        all_sprites.update()

        # Verifica se os objetos saíram da tela
        for obj in moving_objects:
            if obj.rect.right < 0 or obj.rect.y < 0:
                if isinstance(obj, Obstacle):
                    score.add_point()
                obj.kill()

        # Renderização
        screen.fill((0, 0, 0))  # Preenche a tela com preto
        all_sprites.draw(screen)  # Desenha os sprites na tela
        score.draw(screen)  # Desenha o score na tela
        draw_level_text(screen, player)
    elif in_shop:
        generate_shop_cards(player)
        render_shop()
    else:
        # Tela de Game Over
        game_over(screen, score, player)

    pygame.display.flip()
    clock.tick(60)


#################################

pygame.quit()
