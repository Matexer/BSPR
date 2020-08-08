import tkinter as tk
from gui.elements import *
from gui.configure import TL_BG


class AddFuelFrame(tk.Frame):
    def __init__(self, top):
        tk.Frame.__init__(self, top)
        self.create_head_section()
        self.create_body_section()
        self.top = top

    def create_head_section(self):
        title = self.create_title("DODAWANIE NOWEGO PALIWA")
        name_container, self.name_entry = self.create_name_container()

        title.pack(side="top", fill="x")
        name_container.pack(side="top", anchor="w", padx=5, pady=20)

    def create_body_section(self):
        inputs_subtitle = self.create_subtitle("DANE OD PRODUCENTA")
        inputs_container, self.inputs_table = self.create_inputs_container()
        comment_subtitle = self.create_subtitle("KOMENTARZ")
        comment_container, self.comment = self.create_comment_container()
        btns_container, self.buttons, self.message = self.create_buttons_container()

        inputs_subtitle.pack(side="top", fill="x")
        inputs_container.pack(side="top", anchor="w", padx=5)
        comment_subtitle.pack(side="top", fill="x")
        comment_container.pack(side="top", anchor="w", padx=5)
        btns_container.pack(side="bottom", fill="x")

    def create_title(self, text):
        title = TitleLabel(self)
        title.configure(text=text)
        return title

    def create_name_container(self):
        name_container = tk.Frame(self)
        label = tk.Label(name_container)
        label.configure(text="Nazwa paliwa",
                        font="bold")
        entry = tk.Entry(name_container)
        entry.configure(width=30)
        label.grid()
        entry.grid(row=0, column=1, padx=7)
        return name_container, entry

    def create_subtitle(self, text):
        subtitle = SubtitleLabel(self)
        subtitle.configure(text=text)
        return subtitle

    def create_inputs_container(self):
        inputs_container = tk.Frame(self)
        variables = (("Średnica zewnętrzna\nładunku paliwa [mm]",
                      "Średnica wewnętrzna\nładunku paliwa [mm]"),

                      ("Długość ładunku\npaliwa [mm]",
                      "Masa paliwa [g]"),

                     ("Siła paliwa [MJ/kg]",
                      "Wykładnik adiabaty gazowych\nproduktów spalania"))
        table = InputTable(inputs_container, variables)
        table.pack()
        return inputs_container, table

    def create_comment_container(self, width=100, height=8):
        comment_container = tk.Frame(self)
        comment = tk.Text(comment_container)
        comment.configure(width=width,
                          height=height)
        comment.pack(pady=5)
        return comment_container, comment

    def create_buttons_container(self):
        btns_container = tk.Frame(self)
        btns_container.configure(bg=TL_BG)

        save_btn = SaveButton(btns_container)
        clear_btn = ClearButton(btns_container)
        cancel_btn = CancelButton(btns_container)

        message_label = MessageLabel(btns_container)
        message_label.configure(bg=TL_BG)

        config = {"padx": 5, "pady": 5, "ipadx": 2, "ipady": 2}
        save_btn.pack(side="right", **config)
        cancel_btn.pack(side="left", **config)
        clear_btn.pack(side="left", **config)

        clear_btn.configure(command=lambda: self.clear_entries())
        cancel_btn.configure(command=lambda: self.cancel())
        return btns_container, (save_btn, clear_btn, cancel_btn), message_label

    def get_inserted_values(self):
        name = [self.name_entry.get()]
        inputs = self.inputs_table.get_inserted_values()
        comment = [self.comment.get('1.0', 'end')]
        return name + inputs + comment

    def point_entries(self, numbers):
        name_num = numbers[0]
        inputs_num = numbers[1:-1]
        if name_num == 0:
            self.name_entry.configure(background="white")
        else:
            self.name_entry.configure(background="red")
        self.inputs_table.point_entries(inputs_num)

    def clear_entries(self):
        self.name_entry.delete('0', 'end')
        self.name_entry.configure(background="white")
        self.inputs_table.clear_entries()
        self.comment.delete("1.0", 'end')
        self.hide_message()

    def cancel(self):
        self.clear_entries()
        self.top.change_frame(0)

    def show_message(self, text, color="red"):
        self.message.set_text(text)
        self.message.set_color(color)
        self.message.pack(side="right", expand=1)

    def hide_message(self):
        self.message.pack_forget()
