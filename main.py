import sys
import PyQt5.QtWidgets as qw
import serial_ui
import threading


class SerialFrom(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = serial_ui.Ui_serial()
        self.ui.setupUi(self)
        print("主线程ID", threading.current_thread().ident)


if __name__ == "__main__":
    app = qw.QApplication(sys.argv)
    w = SerialFrom()
    w.show()
    sys.exit(app.exec_())
