from PyQt5 import QtCore

class InterfaceStatusThread(QtCore.QThread):
    interface_signal = QtCore.pyqtSignal(str)
    changed_signal = QtCore.pyqtSignal(bool)

    def __init__(self, int_name):
        super().__init__()
        self.int_name = int_name
        self.running = False
        self.int_change = "down"

    def run(self) -> None:
        self.running = True
        while self.running:
            # проверка состояния сетевого интерфейса
            int_file = '/sys/class/net/' + self.int_name + '/operstate'
            # int_file = '/sys/class/net/enp3s0/operstate'
            with open(int_file) as f:
                int_status = f.readline().rstrip()
                self.interface_signal.emit(int_status)
                if self.int_change != int_status:
                    self.changed_signal.emit(True)
                    self.int_change == int_status
                else:
                    self.changed_signal.emit(False)

