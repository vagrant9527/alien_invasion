class Settings():
    """存储《外星人》入侵的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
        self.ship_limit=3
        # 子弹设置
        self.bullet_speed_factor = 0.1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        # 外星人设置
        self.alien_speed_factor = 1
        #指定外星人撞到边缘时向下移动的速度
        self.fleet_drop_speed = 100
        # fleet_direction为1表示向右移动，为-1表示向左移动
        self.fleet_direction = 1