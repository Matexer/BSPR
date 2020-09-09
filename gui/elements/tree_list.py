import tkinter as tk
import tkinter.ttk as ttk


class TreeList(tk.Frame):
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

    def set_columns_width(self, tree_width, widths):
        widths = [int(width * tree_width) for width in widths]
        self.tree.column('#0', minwidth=widths[0]//2, width=widths[0])
        for num, width in enumerate(widths[1:]):
            self.tree.column(num, width=width,
                             minwidth=width//2,
                             stretch=1)
