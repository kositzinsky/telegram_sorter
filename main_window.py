import tkinter as tk
from tkinter import filedialog
from tkinter import ttk


class MainWindow:
    directory = None

    root = tk.Tk()
    root.title("Мини-приложение")
    root.geometry("400x300")

    def __init__(self):
        self.directory = None

        self.choose_dir_btn = ttk.Button(
            self.root, text="Выбрать папку", command=self.select_dir
        )
        self.choose_dir_btn.place(relx=0.35, rely=0.9, anchor="c", width=100, height=40)

        self.sort_files_btn = ttk.Button(self.root, text="Сортировать", command=...)
        self.sort_files_btn.place(relx=0.65, rely=0.9, anchor="c", width=100, height=40)

        self.dir_label = ttk.Label(
            self.root, text=f"Выбранная папка: {self.show_dir()}"
        )
        self.dir_label.place(relx=0.05, rely=0.7)

        self.var1 = tk.IntVar()
        self.cb1 = ttk.Checkbutton(self.root, text="Опция 1", variable=self.var1)
        self.cb1.pack()

    def select_dir(self):
        self.directory = filedialog.askdirectory()
        self.dir_label.config(text=f"Выбранная папка: {self.directory}")

    def show_dir(self):
        return self.directory

    def main_window_run(self):
        self.root.mainloop()


if __name__ == "__main__":
    main = MainWindow()
    print(main.directory)
    main.main_window_run()
