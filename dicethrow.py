import tkinter as tk
import random
import time
from PIL import Image, ImageTk, ImageDraw, ImageFont
from tkinter import messagebox

class DiceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Roller")

        self.sides = 6
        self.previous_results = []

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

        self.result_label = tk.Label(self.root, text="Result: ", font=("Helvetica", 16))
        self.result_label.pack(pady=20)

        self.image_label = tk.Label(self.root)
        self.image_label.pack(pady=10)


    def throw(self):
        self.btn_throw.config(state=tk.DISABLED)  # Block button
        self.root.unbind("<Return>")  # Block Enter key
        self.result_label.config(text=f"Result:") 


        images = [Image.open("rzut1.png"), 
                  Image.open("rzut2.png"),
                  Image.open("rzut3.png"),
                  Image.open("rzut4.png")]
        for i in range(len(images) - 1):
            tk_image = ImageTk.PhotoImage(images[i])
            self.image_label.config(image=tk_image)
            self.image_label.image = tk_image
            self.root.update()
            time.sleep(0.2)
        result = random.randint(1, self.sides)

        final_image =  images[len(images) - 1]
        draw = ImageDraw.Draw(final_image)
        font = ImageFont.truetype("Helvetica", 50) 
        text = str(result)
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        width, height = final_image.size
        position = (width // 2 - text_width // 2 - 40, height // 2 - text_height // 2 + 30)
        draw.text(position, text, font=font, fill="black")
        final_tk_image = ImageTk.PhotoImage(final_image)
        self.image_label.config(image=final_tk_image)
        self.image_label.image = final_tk_image

        self.result_label.config(text=f"Result: {result}")
        self.previous_results.append(result)
        self.btn_throw.config(state=tk.NORMAL)

        self.root.bind("<Return>", self.throw_with_enter)

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
                    self.sides = sides
                    self.label_sides.config(text=f"Number of sides: {self.sides}")
                    self.previous_results.clear()
                    set_sides_window.destroy()
                else:
                    messagebox.showerror("Invalid input", "Number of sides must be a positive integer.")
            except ValueError:
                messagebox.showerror("Invalid input", "Please enter a valid integer.")

        set_sides_window = tk.Toplevel(self.root)
        set_sides_window.title("Set Number of Sides")

        tk.Label(set_sides_window, text="Enter number of sides:").pack(pady=10)
        # tk.Label(set_sides_window, text="(Note: Numbers over 4 digits may be displayed wrong)").pack(pady=10)
        entry_sides = tk.Entry(set_sides_window)
        entry_sides.pack(pady=10)
        entry_sides.focus()

        entry_sides.bind("<Return>", update_sides)
        entry_sides.bind("<Escape>", lambda e: set_sides_window.destroy())


        tk.Button(set_sides_window, text="Set", command=update_sides).pack(pady=10)
        tk.Button(set_sides_window, text="Cancel", command=set_sides_window.destroy).pack(pady=5)

def main():
    root = tk.Tk()
    app = DiceApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
