from PyQt5 import QtCore


class TestTread(QtCore.QThread):
    test_sygnal = QtCore.pyqtSignal(str)

    def __init__(self, int_name):
        QtCore.QThread.__init__(self)
        self.running = False
        self.int_name = int_name
        # self.test_sygnal = QtCore.pyqtSignal(str)

    def run(self):
        self.running = True
        while self.running:
            # проверка состояния сетевого нтерфейса
            int_file = '/sys/class/net/' + self.int_name + '/operstate'
            with open(int_file) as f:
                int_status = f.readline().rstrip()


