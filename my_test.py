# # import sys
# # import pygame
# #
# # from setting import Settings
# # from ship import Ship
# #
# #
# # ai_settings=Settings()
# # screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
# #
# # #显示一些Ship类中属性rect的类型。结果显示，它的类型是类
# # ship=Ship(screen)
# # print(type(ship.rect))
class test():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def printa(self):
        print(self.a)

    def printb(self):
        print(self.b)
#
#
# class test_test():
#
#     def __init__(self):
#         self.t = test(4,5)
#         self.t.a=100
#
#     def print_a(self):
#         print(self.t.a)
#
#
# tt = test_test()
# tt.print_a()

# bullets=[11,-7,0,3,-45,-33,-21,-49,-5,2]
# for bullet in bullets:
#     if bullet<= 0:
#         bullets.remove(bullet)
#
# print(bullets)

def var(test):
    test.a+=1
    test.b+=1

t=test(9,9)
var(t)

print(t.a)
print(t.b)