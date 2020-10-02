from gui.elements import TreeList
from .templates import ListFrameTemplate
import head.database as db


class FuelsListFrame(ListFrameTemplate):
    def __init__(self, top):
        super().__init__(top)

    def get_id_by_name(self, name):
        tree = self.tree_list.tree
        items = tree.get_children()
        for item_id in items:
            if tree.item(item_id)['text'] == name:
                return item_id

    def create_head_section(self, top):
        title = self.create_title(self, "LISTA PALIW")
        btns_container, self.buttons =\
            self.create_btns_container(self)
        self.buttons[0].config(
            command=lambda: self.top.change_frame(1))

        title.pack(side="top", fill="x")
        btns_container.pack(side="top")

    def create_body_section(self, top):
        self.tree_list = TreeList(self)
        comment_container, self.comment_elements =\
            self.create_comment_container(self)

        self.tree_list.pack(fill="both", expand=1)
        comment_container.pack(side="bottom", fill="x")

        columns = {"Nazwa": 0.3,
                   "Siła [MJ/kg]": 0.15,
                   "k": 0.07,
                   "Masa [g]": 0.12,
                   "Długość [mm]": 0.12,
                   "Śr. zew. [mm]": 0.12,
                   "Śr. wew. [mm]": 0.12}

        self.set_list(top, self.tree_list, columns)
        self.data = self.load_data()
        self.fill_list(self.tree_list.tree, self.data)

    @staticmethod
    def load_data():
        fuels = db.get_fuels_list()
        data = []
        for fuel_name in fuels:
            fuel = db.load_fuel(fuel_name)
            data.append(fuel)
        return data

    @staticmethod
    def fill_list(tree, data):
        for fuel in data:
            tree.insert(
                '', 'end',
                text=fuel.name, values=(fuel.strength,
                                        fuel.k,
                                        fuel.mass,
                                        fuel.length,
                                        fuel.outer_diameter,
                                        fuel.inner_diameter))

    def reload_list(self):
        tree = self.tree_list.tree
        items = tree.get_children()
        for item in items:
            tree.delete(item)
        self.data = self.load_data()
        self.fill_list(tree, self.data)
