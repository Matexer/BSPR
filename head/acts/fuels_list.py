from tkinter import messagebox as mb
import head.database as db


class FuelsListAct:
    def __init__(self, top):
        self.frame = top.frames[0]

        self.tree_list = self.frame.tree_list
        self.comment_elements = self.frame.comment_elements

        self.tree_list.tree.bind("<<TreeviewSelect>>", self.load_comment)
        self.set_buttons(self.frame)
        self.top = top

    def load_comment(self, event):
        if event.widget.selection():
            fuel = event.widget.selection()[0]
            fuel_id = self.tree_list.tree.index(fuel)
            f_data = self.frame.data[fuel_id]
            add_datetime = f_data.save_date + " " + f_data.save_time
            edit_datetime = f_data.edit_date + " " + f_data.edit_time
            self.fill_comment_section(add_datetime, edit_datetime, f_data.comment)
        else:
            self.fill_comment_section('', '', '')

    def fill_comment_section(self, add_date, edit_date, comment):
        adding_fuel_date, modify_fuel_date, comment_label =\
            self.comment_elements
        adding_fuel_date.config(text=add_date)
        modify_fuel_date.config(text=edit_date)
        comment_label.config(text=comment)

    def set_buttons(self, frame):
        edit_btn = frame.buttons[1]
        delete_btn = frame.buttons[2]

        edit_btn.configure(command=lambda: self.edit_fuel())
        delete_btn.configure(command=lambda: self.delete_fuels())

    def edit_fuel(self):
        names, ids = self.get_selected_fuels()
        edit_frame = self.top.frames[4]
        fuel = db.load_fuel(names[0])
        values = list(fuel.export().values())[:8]
        edit_frame.set_values(values)
        self.top.change_frame(4)

    def delete_fuels(self):
        tree = self.frame.tree_list.tree
        names, ids = self.get_selected_fuels()
        chosen_f_number = len(names)
        title = "Usunięcie paliw"
        message = "Czy chcesz usunąć %i " % chosen_f_number
        if chosen_f_number > 1:
            if chosen_f_number < 5:
                message += "wybrane paliwa z bazy danych?"
            else:
                message += "wybranych paliw z bazy danych?"
        else:
            title = "Usunięcie paliwa"
            message = "Czy chcesz usunąć paliwo %s z bazy danych?" % names[0]

        reply = mb.askyesno(title, message)
        if reply:
            for name, f_id in zip(names, ids):
                tree.selection_remove(f_id)
                db.remove_fuel(name)
                tree.delete(f_id)
                self.frame.data = self.frame.load_data()

    def get_selected_fuels(self):
        tree = self.tree_list.tree
        fuels = tree.selection()
        f_names = [tree.item(fuel)['text'] for fuel in fuels]
        return f_names, fuels
