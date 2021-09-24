import random
import time
import arcade



class Player(arcade.AnimatedWalkingSprite):
    def __init__(self):
        super().__init__()
        self.width = 30
        self.height = 30
        self.change_x = 100
        self.change_y = 400
        self.speed = 4
        
        self.stand_left_textures = [arcade.load_texture(':resources:images/animated_characters/female_adventurer/femaleAdventurer_walk0.png')]
        self.walk_left_textures = [arcade.load_texture(':resources:images/animated_characters/female_adventurer/femaleAdventurer_walk0.png'),
                                   arcade.load_texture(':resources:images/animated_characters/female_adventurer/femaleAdventurer_walk1.png'),
                                   arcade.load_texture(':resources:images/animated_characters/female_adventurer/femaleAdventurer_walk2.png'),
                                   arcade.load_texture(':resources:images/animated_characters/female_adventurer/femaleAdventurer_walk3.png'),
                                   arcade.load_texture(':resources:images/animated_characters/female_adventurer/femaleAdventurer_walk4.png'),
                                   arcade.load_texture(':resources:images/animated_characters/female_adventurer/femaleAdventurer_walk5.png'),
                                   arcade.load_texture(':resources:images/animated_characters/female_adventurer/femaleAdventurer_walk6.png'),
                                   arcade.load_texture(':resources:images/animated_characters/female_adventurer/femaleAdventurer_walk7.png')]
        
        self.stand_right_textures= [arcade.load_texture(':resources:images/animated_characters/female_adventurer/femaleAdventurer_walk0.png', mirrored = True),]  
        self.walk_right_textures = [arcade.load_texture(':resources:images/animated_characters/female_adventurer/femaleAdventurer_walk0.png', mirrored = True),
                                   arcade.load_texture(':resources:images/animated_characters/female_adventurer/femaleAdventurer_walk1.png', mirrored = True),
                                   arcade.load_texture(':resources:images/animated_characters/female_adventurer/femaleAdventurer_walk2.png', mirrored = True),
                                   arcade.load_texture(':resources:images/animated_characters/female_adventurer/femaleAdventurer_walk3.png', mirrored = True),
                                   arcade.load_texture(':resources:images/animated_characters/female_adventurer/femaleAdventurer_walk4.png', mirrored = True),
                                   arcade.load_texture(':resources:images/animated_characters/female_adventurer/femaleAdventurer_walk5.png',mirrored = True),
                                   arcade.load_texture(':resources:images/animated_characters/female_adventurer/femaleAdventurer_walk6.png',mirrored = True),
                                   arcade.load_texture(':resources:images/animated_characters/female_adventurer/femaleAdventurer_walk7.png',mirrored = True)]
            
        
         
        
class Lamia(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture(':resources:images/animated_characters/zombie/zombie_walk3.png')
        self.width = 60
        self.height = 60
        self.change_x = random.choice([-1, 1])
        self.change_y = 400
        self.speed = 4
        

        
        
        
class Ground(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__() 
        self.texture = arcade.load_texture(':resources:images/tiles/planetHalf_mid.png')
        self.center_x = x
        self.center_y = y
        self.width = 120
        self.height = 120
        



class Box(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__() 
        self.texture = arcade.load_texture(':resources:images/tiles/sandHalf_left.png')
        self.center_y = y
        self.center_x = x 
        
        self.width = 120
        self.height = 120              
        
class MyGame(arcade.Window):
    def __init__(self):
        self.w = 700
        self.h = 600
        self.gravity = 0.2
        super().__init__(self.w, self.h, "NightLamia")
        self.background_image = arcade.load_texture('art.png')
        self.t1 = time.time()
        self.me = Player()
        self.lamia_list = arcade.SpriteList()
        self.ground_list = arcade.SpriteList()
        
        for i in range(0, 1000, 120):
            ground = Ground(i, 50)
            self.ground_list.append(ground)
            
        for i in range(400, 800, 120):
            ground = Ground(i, 300)
        self.ground_list.append(ground)
            
        for i in range(100, 400, 120):
            ground = Ground(i, 500)
            self.ground_list.append(ground)
            
            
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, 600, 500, self.background_image)
        self.me.draw()
        
        for ground in self.ground_list:
            ground.draw()
            
        for lamia in self.lamia_list:
            lamia.draw()
            
        
        self.my_physics_engine = arcade.PhysicsEnginePlatformer(self.me, self.ground_list, gravity_constant=self.gravity)
        self.lamia_physics_engine_list = []
        
        
        
    def on_update(self, delta_time):
        self.t2 = time.time()
        if self.t2 - self.t1 > 5:
            new_lamia = Lamia()
            self.lamia_list.append(new_lamia)
            self.lamia_physics_engine_list.append(arcade.physics_engines(new_lamia, self.ground_list, gravity_constant = self.gravity))
            self.t1 = time.time()
            self.my_physics_engine.update()
            
            for lamia in self.lamia_list:
                lamia.update()
    
            self.me.update_animation()
            
            
    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.me.change_x = -1*self.me.speed
            
        elif key == arcade.key.RIGHT:
            self.me.change_y = 1*self.me.speed
        elif key == arcade.key.UP:
            if self.my_physics_engine.can_jump():
                self.me.change_y = 10
                
    def  on_key_press(self, key, modifiers):
        self.me.change_x = 0
        

game = MyGame()
arcade.run()