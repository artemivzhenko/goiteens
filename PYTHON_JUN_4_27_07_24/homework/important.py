import keyboard

def on_key_event(event):
    print(f"Клавиша {event.name} была нажата!")

keyboard.on_press(on_key_event)

print("Программа ожидает нажатия клавиш. Для выхода нажмите ESC.")
keyboard.wait("esc")
