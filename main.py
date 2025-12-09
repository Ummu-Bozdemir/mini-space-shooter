import pygame
import sys
import random
import time
import requests

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Space Shooter FINAL")
clock = pygame.time.Clock()
player_img_original = pygame.image.load("spaceship.pod_.1.png")
player_img = pygame.transform.scale(player_img_original, (80, 80))
player_width = 80
player_height = 80

ufo_img_original = pygame.image.load("ufo.png")
ufo_img = pygame.transform.scale(ufo_img_original, (60, 40))
ufo_width = 60
ufo_height = 40

boss_img = pygame.transform.scale(ufo_img_original, (160, 100))
final_boss_img = pygame.transform.scale(ufo_img_original, (240, 150))

player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 120
player_speed = 5
player_name = ""

score = 0

bullets = []
bullet_speed = 10
bullet_offsets = [-20, 0, 20]

ufo_list = []
ufo_speed = 1.2
ufo_spawn_rate = 45
ufo_per_spawn = 1

level = 1
level_start_time = time.time()

boss_active = False
boss_hp = 40
boss_x = WIDTH // 2 - 80
boss_y = -150
boss_speed = 2

final_boss_active = False
final_boss_hp = 120
final_boss_x = WIDTH // 2 - 120
final_boss_y = -200
final_boss_speed = 2

lives = 3
game_over = False

font = pygame.font.SysFont("Arial", 28)
big_font = pygame.font.SysFont("Arial", 64)
small_font = pygame.font.SysFont("Arial", 22)


def get_player_name():
    global player_name
    input_text = ""
    asking = True

    while asking:
        screen.fill((0, 0, 0))

        title = big_font.render("Enter Your Name:", True, (255, 255, 255))
        screen.blit(title, (WIDTH//2 - title.get_width()//2, HEIGHT//2 - 100))

        name_surf = font.render(input_text, True, (150, 200, 255))
        screen.blit(name_surf, (WIDTH//2 - name_surf.get_width()//2, HEIGHT//2))

        pygame.display.update()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN and len(input_text) > 0:
                    player_name = input_text
                    asking = False
                elif e.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    if len(input_text) < 12:
                        input_text += e.unicode


def send_score():

    try:
        requests.post(
            "https://bozdemirummu.app.n8n.cloud/webhook/47973814-e6dd-4f5d-adf4-1a08ea90b26a",
            json={"player_name": player_name, "score": score}
        )
    except Exception as e:
        print("Could not send score:", e)


def fire_bullets():
    for off in bullet_offsets:
        bullets.append([player_x + player_width//2 + off, player_y])


def spawn_ufos(count):
    for _ in range(count):
        x = random.randint(0, WIDTH - ufo_width)
        y = -random.randint(40, 200)
        ufo_list.append([x, y])


def reset_game():
    global lives, ufo_list, bullets, boss_active, boss_hp
    global final_boss_active, final_boss_hp
    global level, level_start_time, ufo_per_spawn
    global boss_x, boss_y, final_boss_x, final_boss_y
    global score
    global game_over

    lives = 3
    ufo_list.clear()
    bullets.clear()

    boss_active = False
    boss_hp = 40
    boss_x = WIDTH // 2 - 80
    boss_y = -150

    final_boss_active = False
    final_boss_hp = 120
    final_boss_x = WIDTH // 2 - 120
    final_boss_y = -200

    level = 1
    score = 0
    ufo_per_spawn = 1
    level_start_time = time.time()
    game_over = False


def update_spawn_by_level(lv):
    if lv == 1: return 1
    elif lv == 2: return 1
    elif lv == 3: return 2
    elif lv == 4: return 2
    elif lv == 5: return 1
    elif lv == 6: return 1
    elif lv == 7: return 1
    else: return 0

get_player_name()
spawn_ufos(1)


while True:

    if level >= 9:
        screen.fill((0, 0, 0))

        win_text = big_font.render("YOU WIN!", True, (50, 255, 50))
        screen.blit(win_text, (WIDTH//2 - win_text.get_width()//2, HEIGHT//2 - 100))

        retry_rect = pygame.Rect(WIDTH//2 - 80, HEIGHT//2, 160, 40)
        pygame.draw.rect(screen, (50, 50, 200), retry_rect)

        retry_txt = small_font.render("PLAY AGAIN", True, (255,255,255))
        screen.blit(retry_txt, (WIDTH//2 - retry_txt.get_width()//2, HEIGHT//2 + 5))

        pygame.display.update()

        send_score()

        waiting = True
        while waiting:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit(); sys.exit()
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if retry_rect.collidepoint(e.pos):
                        reset_game()
                        waiting = False
        continue

    if game_over:
        screen.fill((0, 0, 0))

        go_text = big_font.render("GAME OVER", True, (255, 60, 60))
        screen.blit(go_text, (WIDTH//2 - go_text.get_width()//2, HEIGHT//2 - 120))

        retry_rect = pygame.Rect(WIDTH//2 - 70, HEIGHT//2, 140, 40)
        pygame.draw.rect(screen, (50, 50, 200), retry_rect)

        retry_txt = small_font.render("RETRY", True, (255,255,255))
        screen.blit(retry_txt, (WIDTH//2 - retry_txt.get_width()//2, HEIGHT//2 + 5))

        pygame.display.update()

        send_score()

        waiting = True
        while waiting:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit(); sys.exit()
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if retry_rect.collidepoint(e.pos):
                        reset_game()
                        waiting = False
        continue

    if time.time() - level_start_time > 10:
        level += 1
        level_start_time = time.time()
        ufo_per_spawn = update_spawn_by_level(level)

        if level == 5 and not boss_active:
            boss_active = True
            boss_hp = 40
            boss_y = -150

        if level == 8 and not final_boss_active:
            final_boss_active = True
            final_boss_hp = 120
            final_boss_y = -200

    if not boss_active and not final_boss_active:
        if ufo_per_spawn > 0:
            if random.randint(1, ufo_spawn_rate) == 1:
                spawn_ufos(ufo_per_spawn)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            fire_bullets()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    for b in bullets[:]:
        b[1] -= bullet_speed
        if b[1] < -20:
            bullets.remove(b)

    for u in ufo_list[:]:
        u[1] += ufo_speed

        if u[1] > HEIGHT:
            ufo_list.remove(u)
            lives -= 1
            if lives <= 0:
                game_over = True
            continue

        for b in bullets[:]:
            if u[0] <= b[0] <= u[0] + ufo_width and u[1] <= b[1] <= u[1] + ufo_height:
                bullets.remove(b)
                ufo_list.remove(u)
                score += 50
                break

        if (player_x < u[0] + ufo_width and
            player_x + player_width > u[0] and
            player_y < u[1] + ufo_height and
            player_y + player_height > u[1]):
            ufo_list.remove(u)
            lives -= 1
            if lives <= 0:
                game_over = True
            continue

    if boss_active:
        if boss_y < 60:
            boss_y += boss_speed
        else:
            boss_x += boss_speed
            if boss_x <= 0 or boss_x >= WIDTH - 160:
                boss_speed *= -1

        for b in bullets[:]:
            if boss_x <= b[0] <= boss_x + 160 and boss_y <= b[1] <= boss_y + 100:
                bullets.remove(b)
                boss_hp -= 1
                if boss_hp <= 0:
                    boss_active = False
                    score += 100
                break

    if final_boss_active:
        if final_boss_y < 50:
            final_boss_y += 2
        else:
            final_boss_x += final_boss_speed
            if final_boss_x <= 0 or final_boss_x >= WIDTH - 240:
                final_boss_speed *= -1

        for b in bullets[:]:
            if final_boss_x <= b[0] <= final_boss_x + 240 and final_boss_y <= b[1] <= final_boss_y + 150:
                bullets.remove(b)
                final_boss_hp -= 1
                if final_boss_hp <= 0:
                    final_boss_active = False
                    score += 200
                    level = 9
                break

    screen.fill((0, 0, 0))

    for u in ufo_list:
        screen.blit(ufo_img, (u[0], u[1]))

    if boss_active:
        screen.blit(boss_img, (boss_x, boss_y))
        screen.blit(font.render(f"BOSS HP: {boss_hp}", True, (255,100,100)), (WIDTH-200, 10))

    if final_boss_active:
        screen.blit(final_boss_img, (final_boss_x, final_boss_y))
        screen.blit(font.render(f"FINAL BOSS HP: {final_boss_hp}", True, (255,100,100)), (WIDTH-260, 50))

    for b in bullets:
        pygame.draw.rect(screen, (255,0,0), (b[0], b[1], 6, 12))

    screen.blit(player_img, (player_x, player_y))

    screen.blit(font.render(f"LEVEL: {level}", True, (255,255,255)), (10, 40))
    screen.blit(font.render(f"LIVES: {lives}", True, (255,255,255)), (10, 10))
    screen.blit(font.render(f"SCORE: {score}", True, (255,255,0)), (10, 70))

    pygame.display.update()
    clock.tick(60)

