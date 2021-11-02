import keyboard

data = {
    'x_ang': 0,
    'y_ang': 0,
    'z_ang': 0
}

while True:
    if keyboard.is_pressed('w'):
        data['x_ang'] += 0.1
    if keyboard.is_pressed('s'):
        data['x_ang'] -= 0.1

    if keyboard.is_pressed('d'):
        data['y_ang'] -= 0.1
    if keyboard.is_pressed('a'):
        data['y_ang'] += 0.1

    if keyboard.is_pressed('z'):
        data['z_ang'] -= 0.1
    if keyboard.is_pressed('x'):
        data['z_ang'] += 0.1

    print(data)
