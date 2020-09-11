import tkinter as tk
import tkinter.ttk as ttk


def check_option(func):
    def func_wrapper(self, *args, **kwargs):
        if not self.CHECK_OPTION:
            raise Exception("Check option is disabled in this list.")
        return func(self, *args, **kwargs)
    return func_wrapper


class TreeList(tk.Frame):
    CHECK_OPTION = False

    def __init__(self, top):
        super().__init__(top)
        container = tk.Frame(self)
        scroll = tk.Scrollbar(container)
        tree = ttk.Treeview(container)
        scroll.config(command=tree.yview)
        scroll.pack(side='right', fill='y')
        tree.pack(fill='both', expand=True)
        tree.config(yscrollcommand=scroll.set)
        container.pack(fill="both", expand=1)
        self.tree = tree
        if self.CHECK_OPTION:
            self.checked_img = tk.PhotoImage(file='graphic/checked.gif')
            self.unchecked_img = tk.PhotoImage(file='graphic/unchecked.gif')
            self.chosen_items_ids = []
            tree.bind("<Button-1>", self.__toggle_item)

    def set_data(self, data):
        self.clean_list()
        self.add_to_list(data)

    def add_to_list(self, data):
        for row in data:
            self.tree.insert('', "end", text=row[0], values=row[1:])

    def clean_list(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

    def set_columns(self, columns):
        tree = self.tree
        tree['columns'] = columns[1:]
        tree['displaycolumns'] = columns[1:]

        tree.heading('#0', text=columns[0])
        for num, column in enumerate(columns[1:]):
            tree.heading(num, text=column)

    def set_columns_width(self, tree_width: int, widths):
        widths = [int(width * tree_width) for width in widths]
        self.tree.column('#0', minwidth=widths[0]//2, width=widths[0])
        for num, width in enumerate(widths[1:]):
            self.tree.column(num, width=width,
                             minwidth=width//2,
                             stretch=1)

    @check_option
    def toggle_all(self):
        tree = self.tree
        items = tree.get_children()

        def set_checkout_img(img):
            for item in items:
                tree.item(item, image=img)

        if len(self.chosen_items_ids) != len(items):
            set_checkout_img(self.checked_img)
            self.chosen_items_ids = [i for i in range(0, len(items))]
        else:
            set_checkout_img(self.unchecked_img)
            self.chosen_items_ids = []

    @check_option
    def __toggle_item(self, event):
        row_id = self.tree.identify("item", event.x, event.y)
        if not row_id:
            return
        index = self.tree.index(row_id)
        if index in self.chosen_items_ids:
            self.chosen_items_ids.remove(index)
            self.tree.item(row_id, image=self.unchecked_img)
        else:
            self.chosen_items_ids.append(index)
            self.tree.item(row_id, image=self.checked_img)
