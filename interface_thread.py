from PyQt5 import QtCore


class InterfaceStatusThread(QtCore.QThread):
    interface_signal = QtCore.pyqtSignal(str)

    def __init__(self, int_name):
        super().__init__()
        self.int_name = int_name
        self.interface_running = False
        # self.int_change = 'down'

    def run(self) -> None:
        self.interface_running = True
        while self.interface_running:
            # проверка состояния сетевого интерфейса
            int_file = '/sys/class/net/' + self.int_name + '/operstate'
            # int_file = '/sys/class/net/enp3s0/operstate'
            with open(int_file) as f:
                int_status = f.readline().rstrip()
                self.interface_signal.emit(int_status)

