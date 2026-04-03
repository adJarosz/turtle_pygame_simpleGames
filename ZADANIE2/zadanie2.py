import pygame, sys
from pathlib import Path

pygame.init()


def resource(name: str):
    return str(Path(__file__).parent / name)


def main():
    clock = pygame.time.Clock()

    pygame.display.set_caption("piłka i grawitacja")
    icon = pygame.image.load(resource("favicon.ico"))
    pygame.display.set_icon(icon)

    try:
        pygame.mixer.music.load(resource("music.mp3"))
        pygame.mixer.music.play(-1)
    except Exception:
        pass

    size = width, height = 800, 800
    screen = pygame.display.set_mode(size)

    speed = [2.0, 2.0]
    accel = [0.1, 0.1]

    key_impulse = 0.2

    image = pygame.image.load(resource("moon.jpg"))
    image = pygame.transform.scale(image, size)
    surf_center = (
        (width - image.get_width()) / 2,
        (height - image.get_height()) / 2,
    )

    screen.blit(image, surf_center)
    ball = pygame.image.load(resource("ball.gif"))
    ball = pygame.transform.scale(ball,(ball.get_width() // 2, ball.get_height() // 2))

    ballrect = ball.get_rect(center=(width / 2, height / 2))
    pygame.display.flip()

    while True:
        clock.tick(60)
        pygame.time.delay(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            sys.exit()

        if keys[pygame.K_LEFT]:
            speed[0] -= key_impulse
        if keys[pygame.K_RIGHT]:
            speed[0] += key_impulse
        if keys[pygame.K_UP]:
            speed[1] -= key_impulse
        if keys[pygame.K_DOWN]:
            speed[1] += key_impulse

        speed[1] += accel[1]

        ballrect = ballrect.move(speed)


        if ballrect.left <= 0:
            ballrect.left = 0
            speed[0] = -speed[0]
        elif ballrect.right >= width:
            ballrect.right = width
            speed[0] = -speed[0]

        if ballrect.top <= 0:
            ballrect.top = 0
            speed[1] = -speed[1]
        elif ballrect.bottom >= height:
            ballrect.bottom = height
            speed[1] = -speed[1]

        screen.blit(image, surf_center)
        screen.blit(ball, ballrect)
        pygame.display.flip()


if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()
