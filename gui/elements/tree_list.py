import tkinter as tk
import tkinter.ttk as ttk


class TreeList(tk.Frame):
    def __init__(self, top):
        tk.Frame.__init__(self, top)

        scroll = tk.Scrollbar(self)
        scroll.pack(side='right', fill='y')
        tree = ttk.Treeview(self)
        tree.pack(fill='both', expand=True)

        tree.config(yscrollcommand=scroll.set)
        scroll.config(command=tree.yview)
        self.tree = tree
        self.top = top
        self.set_columns(("test 1", "test 2"))

    def set_columns(self, columns):
        tree = self.tree
        self.top.update_idletasks()

        num_of_col = len(columns)
        tree_width = tree.winfo_width()
        width_unit = tree_width // num_of_col
        half_width = width_unit // 2

        tree.heading('#0', text=columns[0])
        tree.column('#0', minwidth=width_unit, width=width_unit, anchor='center', stretch=1)
        tree['columns'] = columns[1:]
        tree['displaycolumns'] = columns[1:]
        for column in columns[1:]:
            tree.column(column, width=width_unit,
                        minwidth=half_width,
                        anchor='center',
                        stretch=0)
            tree.heading(column, text=column)
