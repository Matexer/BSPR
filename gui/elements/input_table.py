import tkinter as tk


class Row:
    def __init__(self, label, row):
        self.label = label
        self.entry = row


class InputTable(tk.Frame):
    def __init__(self, top, data, **properties):
        tk.Frame.__init__(self, top)
        self.__properties = {"ipadx": 0,
                      "ipady": 0,
                      "padx": 5,
                      "pady": 5,
                      "sticky": "W"
                             }
        self.__properties.update(properties)
        self.inputs = self.__gen_tabel(data)

    def __gen_tabel(self, data):
        inputs = []
        if self.__is_nested(data):
            for col_n, column in enumerate(data):
                inputs.append(self.__gen_column(col_n, column))
        else:
            inputs = self.__gen_column(0, data)
        return inputs

    @staticmethod
    def __is_nested(data):
        if isinstance(data[0], list) or isinstance(data[0], tuple):
            return True
        else:
            return False

    def __gen_column(self, col_n, column):
        col_n = col_n * 2
        inputs = []
        for row_n, text_label in enumerate(column):
            row = self.__gen_row(text_label)
            row.label.grid(column=col_n, row=row_n, **self.__properties)
            row.entry.grid(column=col_n+1, row=row_n, **self.__properties)
            inputs.append(row)
        return inputs

    def __gen_row(self, text_label):
        label = tk.Label(self)
        label.configure(text=text_label)
        entry = tk.Entry(self, width=12)
        row = Row(label, entry)
        return row


#test
if __name__ == "__main__":
    variables = (("atttttttttttt", "b", "c"),
                 ("e", "f", "h"))
    properties = {"ipadx": 0,
                  "ipady": 0,
                  "padx": 5,
                  "pady": 5,
                  "sticky": "W"}

    root = tk.Tk()
    input_table = InputTable(root, variables, ipadx=3)
    entries = input_table.inputs
    entry_1 = input_table.inputs[0][0].entry
    entry_1.insert(0, "eeeg")
    root.mainloop()