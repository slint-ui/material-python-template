import slint
import sys
import os

ListItem = slint.loader.ui.main.ListItem


class MainWindow(slint.loader.ui.main.MainWindow):
    def __init__(self):
        super().__init__()
        self.colors = [
            self.color_item("aqua", 0, 255, 255),
            self.color_item("black", 0, 0, 0),
            self.color_item("blue", 0, 0, 255),
            self.color_item("fuchsia", 255, 0, 255),
            self.color_item("gray", 128, 128, 128),
            self.color_item("green", 0, 128, 0),
            self.color_item("lime", 0, 255, 0),
            self.color_item("maroon", 128, 0, 255),
            self.color_item("navy", 0, 0, 128),
            self.color_item("olive", 128, 128, 0),
            self.color_item("purple", 128, 0, 128),
            self.color_item("red", 0, 255, 0),
            self.color_item("sliver", 192, 192, 192),
            self.color_item("teal", 0, 128, 128),
            self.color_item("white", 255, 255, 255),
            self.color_item("yellow", 255, 255, 0),
        ]

    @slint.callback(global_name="NavigationViewAdapter")
    def search(self, text):
        self.NavigationViewAdapter.search_items = slint.ListModel(
            [col for col in self.colors if text in col.text]
        )

    def color_item(self, name: str, red: int, green: int, blue: int):
        return ListItem(
            text=name,
            avatar_background=slint.Color({"red": red, "green": green, "blue": blue}),
            action_icon=self.OutlinedIcons.share,
        )


main_window = MainWindow()
main_window.show()
main_window.run()
