import timeit

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


class Test_cube(Entity):
    def __init__(self):
        super().__init__(
            model="cube",
            color=color.white,
            texture="white_cube",
            # rotation=Vec3(45, 45, 45)
        )


class Test_button(Button):
    def __init__(self):
        super().__init__(
            model="cube",
            texture="brick",
            color=color.blue
        )


def update():
    # Move Entity
    if held_keys["w"]:
        test_square.y += 0.1
    if held_keys["a"]:
        test_square.x -= 0.1
    if held_keys["s"]:
        test_square.y -= 0.1
    if held_keys["d"]:
        test_square.x += 0.1

    # Rotate Entity
    if held_keys["r"]:
        test_cube.rotation_x += 3
        test_cube.rotation_y -= 1


app = Ursina()

# Square Entity
test_square = Entity(model="cube", color=color.blue, scale=(1, 1), position=(3, 2))

# Texture Entity
"""sans_texture = load_texture("assets/Sans.png")
sans = Entity(model="cube", texture=sans_texture)"""

test_cube = Test_button()

app.run()
