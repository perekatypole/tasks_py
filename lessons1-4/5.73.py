import math

def pole_angle():
    wall_distance = 3
    pole_length = 4.5
    pole_height = 0
    angle = 0
    while pole_height < pole_length:
        pole_height += 0.2
        distance = math.sqrt(wall_distance ** 2 + pole_height ** 2)
        angle = math.degrees(math.atan(pole_height / wall_distance))
        print("Distance from wall:", round(distance, 2), "meters")
        print("Angle with floor:", round(angle, 2), "degrees")