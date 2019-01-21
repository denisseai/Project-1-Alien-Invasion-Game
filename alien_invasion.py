import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
  #Initialize pygame, settings and create a screen object
  pygame.init()
  ai_settings = Settings()
  screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
  pygame.display.set_caption("Alien Invasion")

  #Make a ship, a grouop of bullets, and a group of aliens
  ship = Ship(ai_settings, screen)
  bullets = Group()
  aliens = Group()

  #Create a fleet of aliens
  gf.create_fleet(ai_settings, screen, aliens)

  #Start the main loop for the game
  while True:
      gf.check_events(ai_settings, screen, ship, bullets)
      ship.update()
      gf.update_bullets(bullets)
      gf.update_screen(ai_settings, screen, ship, aliens, bullets)

      #Get rid of bullets that have disappeared
      for bullet in bullets.copy():
          if bullet.rect.bottom < 0:
              bullets.remove(bullet)
      print(len(bullets))

      gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
