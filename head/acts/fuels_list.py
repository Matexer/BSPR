from tkinter import messagebox as mb
import head.database as db


class FuelsListAct:
    def __init__(self, top):
        self.frame = top.frames[0]
        self.set_buttons(self.frame)
        self.top = top

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
                db.remove_fuel(name)
                tree.delete(f_id)

    def get_selected_fuels(self):
        tree = self.frame.tree_list.tree
        fuels = tree.selection()
        f_names = []
        for fuel in fuels:
            f_names.append(tree.item(fuel)['text'])

        return f_names, fuels
