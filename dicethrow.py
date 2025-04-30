import tkinter as tk
import random
import time
import pygame
from PIL import Image, ImageTk, ImageDraw, ImageFont
from tkinter import messagebox

class DiceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Roller")
        self.throws = 0

        self.sides = 6
        self.previous_results = []

        pygame.mixer.init()
        self.sound_gun = pygame.mixer.Sound("animation/gun_sound.mp3")
        self.sound_gun.set_volume(0.02)
        self.sound_kick = pygame.mixer.Sound("animation/kick_sound.mp3")
        self.sound_kick.set_volume(0.02)

        self.open = False
        self.alive = True
        self.tk_img_click = self.get_tk_imgs(["animation/click.png",
                                              "animation/click_empty.png"])

        self.tk_img_kill_open = self.get_tk_imgs(["animation/kill_open.png"])[0]
        self.tk_imgs_throw = self.get_tk_imgs(["animation/throw1.png",
                                                "animation/throw2.png",
                                                "animation/throw3.png"])
        self.tk_imgs_kick = self.get_tk_imgs(["animation/kick1.png",
                                              "animation/kick2.png"])
        self.tk_img_kill = self.get_tk_imgs(["animation/kill.png"])[0]
        self.tk_img_idle = self.get_tk_imgs(["animation/idle.png"])[0]

        self.create_widgets()

    def create_widgets(self):
        self.label_sides = tk.Label(self.root, text=f"Number of sides: {self.sides}")
        self.label_sides.pack()

        self.btn_throw = tk.Button(self.root, text="Throw Dice", command=self.throw)
        self.btn_throw.pack(pady=10)

        self.root.bind("<Return>", self.throw_with_enter)
        self.root.bind("<Escape>", lambda e: self.root.quit())

        self.btn_previous = tk.Button(self.root, text="Show Previous Results", command=self.show_previous_results)
        self.btn_previous.pack(pady=10)

        self.btn_set_sides = tk.Button(self.root, text="Set Number of Sides", command=self.set_sides)
        self.btn_set_sides.pack(pady=10)

        self.btn_exit = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.btn_exit.pack(pady=10)

        self.image_label = tk.Label(self.root)
        self.show_img(self.tk_img_idle, self.image_label)
        self.image_label.bind("<Button-1>", self.on_image_click)
        self.image_label.pack(pady=10)

        self.label_previous = tk.Label(self.root, text="Previous throws: ")
        self.label_previous.pack()

    def animate(self, tk_imgs: list, label: tk.Label, freq: int):
        for tk_img in tk_imgs:
            self.show_img(tk_img, label)
            time.sleep(freq)

    def show_img(self, tk_img, label: tk.Label):
        label.config(image=tk_img)
        label.image = tk_img
        self.root.update()

    def text_on_image(self, image: str, text: str, size: int, pos: tuple[int]):
        img =  Image.open(image)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("Helvetica", 50)
        draw.text(pos, text=text, font=font, fill='black')
        tk_img = ImageTk.PhotoImage(img)
        return tk_img

    def get_tk_imgs(self, img_names: list[str]):
        tk_imgs = []
        for img_name in img_names:
            img = Image.open(img_name)
            tk_img = ImageTk.PhotoImage(img)
            tk_imgs.append(tk_img)
        return tk_imgs

    def on_image_click(self, event):
        click_x, click_y = event.x, event.y
        print(click_x, click_y)
        if 80 <= click_x <= 200 and 100 <= click_y <= 220 and self.throws > 0:
            self.open = True
            if self.alive:
                self.show_img(self.tk_img_click[0], self.image_label)
            else:
                self.show_img(self.tk_img_click[1], self.image_label)
        elif 295 <= click_x <= 350 and 73 <= click_y <= 193:
            self.throw()

    def throw(self):
        last_five = self.previous_results[-5:]
        last_five.reverse()
        self.label_previous.config(text=f"Previous throws: {', '.join(map(str, last_five))}")

        self.image_label.unbind("<Button-1>")
        self.btn_throw.config(state=tk.DISABLED)  # Block button
        self.root.unbind("<Return>")  # Block Enter key
        if self.throws > 0:
            if(len(self.previous_results) >=3 and \
                self.previous_results[-1]==self.previous_results[-2]) and \
                self.previous_results[-2]==self.previous_results[-3]:
                if(self.open and self.alive):
                    self.show_img(self.tk_img_kill_open, self.image_label)
                    self.sound_gun.play()
                    time.sleep(0.15)
                    self.sound_gun.play()
                    time.sleep(0.15)
                    self.sound_gun.play()
                    time.sleep(0.3)
                    self.alive = False
                else:
                    tk_img_kick1 = self.text_on_image("animation/kick1.png",
                                                        str(self.previous_results[-1]),
                                                        50, (130, 145))
                    tk_img_kick2 = self.tk_imgs_kick[1]
                    self.sound_kick.play()
                    self.animate([tk_img_kick1, tk_img_kick2], self.image_label, 0.1)
            else:
                self.sound_gun.play()
                self.show_img(self.tk_img_kill, self.image_label)
                time.sleep(0.2)

        result = random.randint(1, self.sides)
        self.previous_results.append(result)
        self.throws += 1

        tk_imgs = self.tk_imgs_throw
        tk_img_final = self.text_on_image("animation/final.png", str(result), 50, (130, 145))
        self.tk_img_last_die = tk_img_final
        tk_imgs.append(tk_img_final)

        self.animate(tk_imgs, self.image_label, 0.1)
        self.open = False

        self.image_label.bind("<Button-1>", self.on_image_click)

        tk_imgs.pop()

        time.sleep(0.1)
        self.btn_throw.config(state=tk.NORMAL) # Unblock button
        self.root.bind("<Return>", self.throw_with_enter) # Unblock enter key

    def throw_with_enter(self, event=None):
        """Funkcja wywoływana po naciśnięciu klawisza Enter"""
        self.throw()

    def show_previous_results(self):
        if not self.previous_results:
            messagebox.showinfo("Previous Results", "No previous results to show.")
            return

        result_window = tk.Toplevel(self.root)
        result_window.title("Previous Results")

        tk.Label(result_window, text="Last 50 throws:").pack(pady=10)

        results_str = ""
        for i in range(len(self.previous_results) - 1, -1, -1):
            if i < len(self.previous_results) - 50:
                break
            if i % 5 == 0 and i != len(self.previous_results) - 1:
                results_str += "\n"
            results_str += f"{self.previous_results[i]}   "
        results_str = results_str.strip()

        average = sum(self.previous_results) / len(self.previous_results)
        results_str += f"\n\nAverage: {average:.2f}"
        results_str += f"\nNumber of sides: {self.sides}"
        results_str += f"\nNumber of throws: {len(self.previous_results)}"
        tk.Label(result_window, text=results_str).pack(pady=10)  

        tk.Button(result_window, text="Close", command=result_window.destroy).pack(pady=10)

        result_window.bind("<Escape>", lambda e: result_window.destroy())
        result_window.bind("<Return>", lambda e: result_window.destroy())

    def set_sides(self):
        def update_sides(event=None):
            try:
                sides = int(entry_sides.get())
                if sides > 0:
                    self.sides = sides if sides <= 1000 else 1000
                    self.label_sides.config(text=f"Number of sides: {self.sides}")
                    self.previous_results.clear()
                    set_sides_window.destroy()
                else:
                    messagebox.showerror("Invalid input", "Number of sides must be a positive integer.")
            except ValueError:
                messagebox.showerror("Invalid input", "Please enter a valid integer.")

        set_sides_window = tk.Toplevel(self.root)
        set_sides_window.title("Set Number of Sides")

        tk.Label(set_sides_window, text="Enter number of sides (max 1000):").pack(pady=10)
        # tk.Label(set_sides_window, text="(Note: Numbers over 4 digits may be displayed wrong)").pack(pady=10)
        entry_sides = tk.Entry(set_sides_window)
        entry_sides.pack(pady=10)
        entry_sides.focus()

        tk.Button(set_sides_window, text="Set", command=update_sides).pack(pady=10)
        entry_sides.bind("<Return>", update_sides)

        tk.Button(set_sides_window, text="Cancel", command=set_sides_window.destroy).pack(pady=5)
        entry_sides.bind("<Escape>", lambda e: set_sides_window.destroy())
def main():
    root = tk.Tk()
    app = DiceApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
