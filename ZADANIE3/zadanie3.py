import pygame
from random import randint
import os

pygame.init()

CZARNY = (0, 0, 0)
BIALY = (255, 255, 255)
CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)

SZEROKOSC = 700
WYSOKOSC = 500

NAZWA_PLIKU_WYNIK = "highscore.txt"


def wczytaj_najlepszy_wynik():
    if not os.path.exists(NAZWA_PLIKU_WYNIK):
        return 0
    try:
        with open(NAZWA_PLIKU_WYNIK, "r") as f:
            return int(f.read().strip() or 0)
    except (IOError, ValueError):
        return 0


def zapisz_najlepszy_wynik(wynik):
    try:
        with open(NAZWA_PLIKU_WYNIK, "w") as f:
            f.write(str(wynik))
    except IOError:
        pass


class Rakietka(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(CZARNY)
        self.image.set_colorkey(CZARNY)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        if self.rect.x < 0:
            self.rect.x = 0

    def moveRight(self, pixels):
        self.rect.x += pixels
        if self.rect.x > SZEROKOSC - self.rect.width:
            self.rect.x = SZEROKOSC - self.rect.width


class Pilka(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(CZARNY)
        self.image.set_colorkey(CZARNY)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.x = randint(0, SZEROKOSC - self.rect.width)
        self.rect.y = 0
        self.velocity = [randint(-4, 4), randint(4, 8)]

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        if self.rect.x <= 0 or self.rect.x >= SZEROKOSC - self.rect.width:
            self.velocity[0] = -self.velocity[0]

        if self.rect.y <= 0:
            self.velocity[1] = -self.velocity[1]

    def bounce(self):
        self.velocity[1] = -abs(self.velocity[1])
        self.velocity[0] += randint(-2, 2)
        if self.velocity[0] > 8:
            self.velocity[0] = 8
        if self.velocity[0] < -8:
            self.velocity[0] = -8


def gra():
    screen = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))
    pygame.display.set_caption("Jednoosobowy Ping Pong")

    rakietka = Rakietka(BIALY, 80, 10)
    rakietka.rect.x = SZEROKOSC // 2 - rakietka.rect.width // 2
    rakietka.rect.y = WYSOKOSC - 30

    pileczka = Pilka(BIALY, 10, 10)

    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(rakietka)
    all_sprites_list.add(pileczka)

    clock = pygame.time.Clock()

    wynik = 0
    najlepszy = wczytaj_najlepszy_wynik()
    font_maly = pygame.font.Font(None, 36)
    font_go = pygame.font.SysFont("arial black", 90, bold=True)

    kontynuuj = True
    game_over = False

    while kontynuuj:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                kontynuuj = False

        keys = pygame.key.get_pressed()

        if not game_over:
            if keys[pygame.K_LEFT]:
                rakietka.moveLeft(7)
            if keys[pygame.K_RIGHT]:
                rakietka.moveRight(7)

            all_sprites_list.update()

            if pygame.sprite.collide_rect(pileczka, rakietka):
                pileczka.bounce()
                wynik += 1

            if pileczka.rect.y >= WYSOKOSC - pileczka.rect.height:
                game_over = True
                if wynik > najlepszy:
                    najlepszy = wynik
                    zapisz_najlepszy_wynik(najlepszy)

        else:
            if keys[pygame.K_r]:
                wynik = 0
                pileczka.reset()
                game_over = False
            if keys[pygame.K_q]:
                kontynuuj = False

        screen.fill(CZARNY)

        if not game_over:
            all_sprites_list.draw(screen)

            text = font_maly.render(f"Wynik aktualny: {wynik}", True, ZIELONY)
            screen.blit(text, (20, 10))

            text_best = font_maly.render(f"Najlepszy wynik: {najlepszy}", True, BIALY)
            screen.blit(text_best, (20, 40))
        else:
            text_go = font_go.render("GAME OVER", True, CZERWONY)
            screen.blit(text_go, (SZEROKOSC // 2 - text_go.get_width() // 2, 100))

            text_w = font_maly.render(f"Wynik aktualny: {wynik}", True, ZIELONY)
            screen.blit(text_w, (SZEROKOSC // 2 - text_w.get_width() // 2, 250))

            text_nb = font_maly.render(f"Najlepszy wynik: {najlepszy}", True, BIALY)
            screen.blit(text_nb, (SZEROKOSC // 2 - text_nb.get_width() // 2, 290))

            text_instr = font_maly.render("R - nowa gra   Q - wyjście", True, BIALY)
            screen.blit(text_instr, (SZEROKOSC // 2 - text_instr.get_width() // 2, 340))

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    gra()
    pygame.quit()
