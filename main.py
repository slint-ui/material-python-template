import slint
from pathlib import Path

ui = slint.load_file(
    Path(__file__).parent / "ui" / "main.slint",
    library_paths={
        "material": Path(__file__).parent / "material-1.0" / "material.slint"
    },
)


class MainWindow(ui.MainWindow):
    def __init__(self):
        super().__init__()


main_window = MainWindow()
main_window.show()
main_window.run()
