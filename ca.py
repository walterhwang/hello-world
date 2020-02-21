#동굴 코드 짜기. - Py게임 실행불가로 코드만..

import sys
from random import randit
import pygame
from pygame.locals import QUIT, Rect, KEYDOWN, K_SPACE
#locals 사용

pygame.init()
pygame.key.set_repeat(5, 5)
SURFACE = pygame.display.set_mode((800, 600))
FPSCLOCK = pygame.time.Clock()
#타이머

def main():
#메인루틴.
walls = 80
ship_y = 250
velocity = 0
score = 0
slope = 0
sysfont = pygame.font.SysFont(None, 36)
ship_image = pygame.image.load("ship.png")
bang_image = pygame.image.load("bang.png")
holes = []
for xpos in range(walls):
    holes.append(Rect(xpos * 10, 100, 10, 400))
game_over = false

while True:
  is_space_down = false
  for event in pygame.event.get():
    if event.type == QUIT:
       pygame.quit()
       sys.exit()
elif event.type == KEYDOWN:
   if event.key == K_SPACE:
      is_space_down = True

#여기서부터 게임내 캐릭터 이동.
   if not game_over:
      score += 10
      velocity += -3 if is_space_down else 3
      ship_y += velocity

#여기서 부터 동굴 불러오기(스크롤).
      edge = holes[-1].copy()
      test = edge.move(0, slope)
      if test.top <= 0 or test.bottom >= 600:
         slope = randint(1, 6) * (-1 if slope > 0 else 1)
         edge.inflate_ip(0, -20)
      edge.move_ip(10, slope)
      holes.append(edge)
      del holes[0]
      holes = [x.move(-10, 0) for x in holes]

#운석과 충돌시.

      if holes[0].top > ship_y + 80:
         game_over = True

#그리기

   SURFACE.fill((0, 255, 0))
   for hole in holes:
      pygame.draw.rect(SURFACE, 0, 0, 0, hole)
   SURFACE.blit(ship_image, (0, ship_y))
   score_image = sysfont.render("score is {}"format(score), True, (0, 0, 225))
   SURFACE.blit(score_image, (600,20))

   if game_over:
      SURFACE.blit(bang_image, (0, ship_y-40))

   pygame.display.update()
   FPSCLOCK.tick(15)

if __name__== '__main__':
   main()
