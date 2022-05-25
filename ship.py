import pygame


class Ship():

    def __init__(self, ai_seetings, screen):
        # 初始化飞船并设置其初始位置
        self.screen = screen
        self.ai_seetings = ai_seetings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每搜新飞船放在屏幕底部中央
        # 将飞船中心的x坐标设置为屏幕矩形的中心x坐标
        # 将飞船下边缘坐标设置为屏幕矩形的下边缘
        self.rect.centerx = self.screen_rect.centerx
        # 这里能看出来,self.rect=self.image.get_rect()是将类给赋值到这个属性上去了。
        # 所以这里是又在给self.rect这个类设置属性
        self.rect.bottom = self.screen_rect.bottom
        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """在指定的位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_seetings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_seetings.ship_speed_factor

        self.rect.centerx = self.center

    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx
