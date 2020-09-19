import tkinter as tk
import tkinter.ttk as ttk


class Field:
    def __init__(self, label, cbox):
        self.label = label
        self.cbox = cbox


class CboxTable(tk.Frame):
    field_properties = {"ipadx": 0, "ipady": 0,"padx": 5,
                      "pady": 5, "sticky": "W"}
    label_properties = {"justify": "left", "anchor": "w"}
    cbox_properties = {"width": 12, "state": "readonly"}

    def __init__(self, top, data, *args, **kwargs):
        super().__init__(top, *args, **kwargs)
        self.fields = self.__gen_table(data)

    def get_inserted_values(self):
        return [field.cbox.get() for field in self.fields]

    def get_validated_values(self):
        invalid_fields = []
        values = []
        for field in self.fields:
            val = field.cbox.get()
            if not val:
                invalid_fields.append(field.label.cget("text"))
            values.append(val)
        return values, invalid_fields

    def clean(self):
        for field in self.fields:
            field.cbox.set('')

    def __gen_table(self, data):
        fields = []
        if isinstance(data, (list, tuple)):
            for col_n, column in enumerate(data):
                fields += self.__gen_column(col_n, column)
        else:
            fields = self.__gen_column(0, data)
        return fields

    def __gen_column(self, col_n, column):
        def gen_row():
            label = tk.Label(self, text=field_data[0], **self.label_properties)
            cbox = ttk.Combobox(self, values=field_data[1], **self.cbox_properties)
            return Field(label, cbox)

        col_n = col_n * 2
        fields = []
        for row_n, field_data in enumerate(column.items()):
            row = gen_row()
            row.label.grid(column=col_n, row=row_n, **self.field_properties)
            row.cbox.grid(column=col_n+1, row=row_n, **self.field_properties)
            fields.append(row)
        return fields


if __name__ == "__main__":
    var_1 = {"a": (1, 2, 3), "b": (2, 3), "c": (5, 2)}
    var_2 = {"a": (1, 2, 3), "b": (2, 3), "c": (5, 2)}
    variables = (var_1, var_2)
    root = tk.Tk()
    PrepareImpulseCTable = CboxTable
    PrepareImpulseCTable.cbox_properties.update(width=40)
    cbox_table = PrepareImpulseCTable(root, variables)
    cbox_table.field_properties.update(width=3)
    cbox_table.update()
    cbox_table.pack()
    entries = cbox_table.fields
    entry_1 = cbox_table.fields[0].cbox
    entry_1.set(2)
    cbox_table.clean()
    # print(input_table.get_inserted_values())
    # input_table.point_entries([0, 1, 0])
    # input_table.clear_entries()
    root.mainloop()
