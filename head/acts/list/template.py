from abc import ABCMeta, abstractmethod


class ListActTemplate(metaclass=ABCMeta):
    def __init__(self, top, list_frame):
        self.frame = list_frame

        self.tree_list = self.frame.tree_list
        self.comment_elements = self.frame.comment_elements

        self.tree_list.tree.bind("<<TreeviewSelect>>", self.load_comment)
        self.set_buttons(list_frame)
        self.top = top

    def load_comment(self, event):
        selected = event.widget.selection()
        if selected:
            item = selected[0]
            item_id = self.tree_list.tree.index(item)
            item_data = self.frame.data[item_id]
            add_datetime = item_data.save_date + " " + item_data.save_time
            edit_datetime = item_data.edit_date + " " + item_data.edit_time
            self.fill_comment_section(add_datetime, edit_datetime, item_data.comment)
        else:
            self.fill_comment_section('', '', '')

    def fill_comment_section(self, add_date, edit_date, comment):
        adding_date, modify_date, comment_label =\
            self.comment_elements
        adding_date.config(text=add_date)
        modify_date.config(text=edit_date)
        comment_label.config(text=comment)

    @abstractmethod
    def set_buttons(self, frame):
        pass
