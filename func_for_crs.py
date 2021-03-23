import pygame as pg
from random import choices
import math


class Figure():
    def __init__(self, current_size, key_press):
        self.current_size = current_size
        self.key_press = key_press
        self.quantity_of_top = 10

    def drawing(self, screen):
        if self.key_press == "rect":
            x, y = pg.mouse.get_pos()


            x -= self.current_size
            y -= self.current_size


            pg.draw.rect(screen, (choices(range(255), k=3)), (x, y, self.current_size * 2, self.current_size * 2))
        

        elif self.key_press == "circle":
            pg.draw.circle(screen, (choices(range(255), k=3)), pg.mouse.get_pos(), self.current_size)


        elif self.key_press == "star":
            step = math.pi / (self.quantity_of_top)
            angle = 0


            x, y = pg.mouse.get_pos()
            right_points, left_points = [], []


            i = 0
            while angle <= math.pi:
                if i % 2 == 0:
                    step_x, step_y = round(self.current_size * math.sin(angle)), round(self.current_size * math.cos(angle))


                    right_points.append([x + step_x, y - step_y])
                    left_points.insert(0, [x - step_x, y - step_y])


                else:
                    step_x, step_y = round(self.current_size / 2 * math.sin(angle)), round(self.current_size / 2 * math.cos(angle))


                    right_points.append([x + step_x, y - step_y])
                    left_points.insert(0, [x - step_x, y - step_y])


                i += 1
                angle += step


            del left_points[-1]
            if angle == math.pi:
                del right_points[-1]


            points = right_points + left_points


            pg.draw.polygon(screen, (choices(range(255), k=3)), points)




    def analizing(self, screen, keys):
        if keys[pg.K_q]:
            self.key_press = "rect"
            screen.fill((255, 255, 255))
            self.current_size = 3


        elif keys[pg.K_w]:
            self.key_press = "circle"
            screen.fill((255, 255, 255))
            self.current_size = 3


        elif keys[pg.K_s]:
            self.key_press = "star"
            screen.fill((255, 255, 255))
            self.current_size = 3


        elif keys[pg.K_SPACE]:
            screen.fill((255, 255, 255))
            self.current_size = 3