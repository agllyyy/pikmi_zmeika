import tkinter as tk
from tkinter import messagebox
from tkinter import Canvas

# Глобальные настройки (можно передавать в игру позже)
settings = {
    "speed": "Средне"  # Варианты: "Медленно", "Средне", "Быстро"
}

# ---------- ФУНКЦИИ РЕЖИМОВ ----------
def play_with_friend():
    messagebox.showinfo("Режим", f"Игра с другом\nСкорость: {settings['speed']}")

def play_vs_computer():
    messagebox.showinfo("Режим", f"Игра против компьютера\nСкорость: {settings['speed']}")

def quit_app():
    if messagebox.askokcancel("Выход"):
        root.destroy()

# ---------- ОКНО НАСТРОЕК ----------
def open_settings():
    settings_window = tk.Toplevel(root)
    settings_window.title("Настройки")
    settings_window.geometry("300x200")
    settings_window.resizable(False, False)
    settings_window.grab_set()  # Блокирует основное окно
    settings_window.configure(bg="#CE83A2")
    tk.Label(settings_window, bg="#CE83A2", text="Скорость игры:", font=("Candara", 12)).pack(pady=10)

    speed_var = tk.StringVar(value=settings["speed"])

    speeds = ["Медленно", "Средне", "Быстро"]
    for speed in speeds:
        tk.Radiobutton(
            settings_window,
            text=speed,
            variable=speed_var,
            value=speed,
            bg="#CE83A2",
            font=("Candara", 11)
            
        ).pack(anchor="w", padx=50)

    def save_and_close():
        settings["speed"] = speed_var.get()
        settings_window.destroy()

    tk.Button(
        settings_window,
        text="Сохранить",
        font=("Candara", 12),
        bg="#43C047",
        fg="white",
        command=save_and_close
    ).pack(pady=15)

# ---------- ГЛАВНОЕ МЕНЮ ----------
root = tk.Tk()
root.title("Змейка — Меню")
root.geometry("400x400")
root.resizable(False, False)
font=('Candara', 16, 'bold')
root.configure(bg="#FFE5EA")

# Создаем Canvas для текста с обводкой
canvas = Canvas(root, width=400, height=60, bg="#FFE5EA", highlightthickness=0)
canvas.pack(pady=1)

# Текст с обводкой "Игра змейка на двоих"
text = "Игра змейка\nна двоих"
x, y = 200, 30  # Центр Canvas

# Рисуем обводку (черные копии текста со смещением)
for dx, dy in [(-1,-1), (-1,1), (1,-1), (1,1)]:
    canvas.create_text(x+dx, y+dy, text=text, 
                     font=("Arial Black", 22, "bold"),
                     fill="#E381B1",  # Цвет обводки
                     anchor="center")

# Рисуем основной текст (белый поверх обводки)
canvas.create_text(x, y, text=text,
                  font=("Arial Black", 22, "bold"),
                  fill="#E381B1",  # Цвет основного текста
                  anchor="center")

# Обычный текст без обводки
tk.Label(root, fg="#5F0322", bg="#CE83A2", text="Выберите режим", font=("Candara", 14)).pack(pady=0)

# Кнопки
tk.Button(root, text="С другом", font=("Candara", 12), width=25, height=2,
          command=play_with_friend, bg="#E381B1", fg="white").pack(pady=8)

tk.Button(root, text="Против компьютера", font=("Candara", 12), width=25, height=2,
          command=play_vs_computer, bg="#E381B1", fg="white").pack(pady=8)

tk.Button(root, text="Настройки", font=("Candara", 12), width=25, height=2,
          command=open_settings, bg="#E381B1", fg="white").pack(pady=8)

tk.Button(root, text="Выход", font=("Candara", 12), width=25, height=2,
          command=quit_app, bg="#E381B1", fg="white").pack(pady=8)

# Запуск
if __name__ == "__main__":
    root.mainloop()