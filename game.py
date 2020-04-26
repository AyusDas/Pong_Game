import os
import random

os.environ["RAYLIB_BIN_PATH"] = "project_env/Lib/site-packages/raylibpy" #path to the binary

from raylibpy import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Mygame:

    def __init__(self):

        # Initialize Players 
        self.player1 = Rectangle(400.0, 1.0,70,20)
        self.player1_score = 0
        self.player2 = Rectangle(400.0, 580.0,70,20)
        self.player2_score = 0
        
        # Iinitialize Ball
        self.ball_center = Vector2(400.0, 200.0)
        self.ball_radius = 13.0
        self.ball_dx = 3
        self.ball_dy = 3


    def draw(self):

        player1_output = f"Player Blue : {self.player1_score}"
        player2_output = f"Player Gray : {self.player2_score}"
        draw_rectangle_rec(self.player1, BLUE)
        draw_rectangle_rec(self.player2, GRAY)
        draw_circle_v(self.ball_center, self.ball_radius, RED)
        draw_text(player1_output, 100, 300, 20, BLACK)
        draw_text(player2_output, 600, 300, 20, BLACK)

    def update(self):

        # Update Players
        if self.player1.x <= SCREEN_WIDTH - 70 :
            if is_key_down(KEY_RIGHT):
                self.player1.x += 3
        
        if self.player1.x >= 1 :
            if is_key_down(KEY_LEFT):
                self.player1.x -= 3
        
        if self.player2.x <= SCREEN_WIDTH - 70 :
            if is_key_down(KEY_D):
                self.player2.x += 3
        
        if self.player2.x >= 1 :
            if is_key_down(KEY_A):
                self.player2.x -= 3
        
        # Update Ball
        self.ball_center.x += self.ball_dx
        self.ball_center.y += self.ball_dy

        if self.ball_center.x >= 13:
            self.ball_dx *= -1

        if self.ball_center.x <= SCREEN_WIDTH - 13:
            self.ball_dx *= -1
        
        # Checking For Collisions
        if check_collision_circle_rec(self.ball_center, self.ball_radius, self.player1) or check_collision_circle_rec(self.ball_center, self.ball_radius, self.player2):
            self.ball_dy *= -1
        
        # Update Score and Ball
        if self.ball_center.y < 1:
            self.player2_score += 1
            self.ball_center.x = 400
            self.ball_center.y = 300
            self.ball_dx *= 1
            self.ball_dy *= -1
        
        if self.ball_center.y > SCREEN_HEIGHT:
            self.player1_score += 1
            self.ball_center.x = 400
            self.ball_center.y = 300
            self.ball_dx *= 1
            self.ball_dy *= -1
        
        
def main():

    game = Mygame()
    set_target_fps(60)
    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "game")

    while not window_should_close():

        game.update()

        begin_drawing()
        clear_background(RAYWHITE)

        game.draw()
        draw_fps(400,300)
        

        end_drawing()
    close_window()

if __name__ == "__main__":
    main()

