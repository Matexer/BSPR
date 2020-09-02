import tkinter as tk


class Field:
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
        self.inputs = self.__gen_table(data)

    def __gen_table(self, data):
        inputs = []
        if self.__is_nested(data):
            for col_n, column in enumerate(data):
                inputs += self.__gen_column(col_n, column)
        else:
            inputs = self.__gen_column(0, data)
        return inputs

    @staticmethod
    def __is_nested(data):
        if isinstance(data[0], (list, tuple)):
            return True

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
        label = tk.Label(self, justify="left", anchor="w")
        label.configure(text=text_label)
        entry = tk.Entry(self, width=12)
        row = Field(label, entry)
        return row

    def get_inserted_values(self):
        """
        :return: list of values. From first column down (down, right)
        """
        values = []
        for row in self.inputs:
            value = row.entry.get()
            values.append(value)
        return values

    def point_entries(self, numbers):
        """
        :param numbers: list = [0 1 0 0]
        Second entry in self.insert get red bg. Rest white.
        """
        for val_n, number in enumerate(numbers):
            if number == 0:
                self.inputs[val_n].entry.configure(background="white")
            else:
                self.inputs[val_n].entry.configure(background="red")

    def clear_entries(self):
        for imp in self.inputs:
            imp.entry.delete('0', 'end')
        numbers = [0] * (len(self.inputs))
        self.point_entries(numbers)


if __name__ == "__main__":
    variables = ("atttttttttttt", "b", "c")
    properties = {"ipadx": 0,
                  "ipady": 0,
                  "padx": 5,
                  "pady": 5,
                  "sticky": "W"}

    root = tk.Tk()
    input_table = InputTable(root, variables, ipadx=3)
    input_table.pack()
    entries = input_table.inputs
    entry_1 = input_table.inputs[0].entry
    entry_1.insert(0, "eeeg")
    print(input_table.get_inserted_values())
    input_table.point_entries([0, 1, 0])
    input_table.clear_entries()
    root.mainloop()
