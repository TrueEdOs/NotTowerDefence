from enum import Enum


class UnitTypes(Enum):
    core = 0
    gun = 1
    wall = 2
    bullet = 3
    enemy = 4


class Constants:
    screen_width = 1200
    screen_height = 600
    fps = 60
    font = "config/Airstream.ttf"
    control_button_text_size = 70
    control_button_width = 100
    control_button_height = 50
    background_image = 'images/background.jpg'
    quit_button_image = 'images/quit_button.png'
    resume_button_image = 'images/resume_button.png'
    pause_menu_width = 2 * screen_width // 5
    pause_menu_height = screen_height // 3
    menu_alpha = 5

    build_menu_width = 350
    build_menu_height = 600

    core_hp = 1500
    core_width = 100
    core_height = 100

    zombie_hp = 10
    zombie_width = 50
    zombie_height = 50
    zombie_speed = 1

