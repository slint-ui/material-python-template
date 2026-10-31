import slint


class MainWindow(slint.loader.slint_project.MainWindow):
    def __init__(self):
        super().__init__()


main_window = MainWindow()
main_window.show()
main_window.run()
