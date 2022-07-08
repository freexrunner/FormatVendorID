import time
from PyQt5 import QtCore
from writer import Writer
from interface_thread import InterfaceStatusThread


class WritterThread(QtCore.QThread):
    message_signal = QtCore.pyqtSignal(str)
    # interface_signal = QtCore.pyqtSignal(str)

    def __init__(self, int_name, ip_address, username, password, model):
        super(WritterThread, self).__init__()
        self.int_name = int_name
        self.ip_address = ip_address
        self.username = username
        self.password = password
        self.model = model
        self.on_changed = None
        self.interface_thread = None
        self.interface_status = None
        self.write_running = False
        self.step = 0
        self.writer = Writer(self.int_name, self.ip_address, self.username, self.password)

        # self.interface_thread = InterfaceStatusThread(self.int_name)
        # self.interface_thread.interface_signal.connect(self.check_status)
        # self.interface_thread.changed_signal.connect(self.check_change)
        # self.interface_thread.start()

    def run(self) -> None:

        # self.interface_thread = InterfaceStatusThread(self.int_name)
        # self.interface_thread.interface_signal.connect(self.check_status)
        # self.interface_thread.changed_signal.connect(self.check_change)
        # self.interface_thread.start()

        self.single_write()

    def single_write(self):
        # одиночный телнет сеанс
        self.message_signal.emit("")
        self.message_signal.emit("Подлючите терминал")
        if self.wait_to_connect():
            self.message_signal.emit("Терминал подключен. Выполняется настройка.")
            self.writer.start_write(self.model)
            self.message_signal.emit("Настройка завершена. Подключите следующий терминал.")

    def wait_to_connect(self):
        if self.writer.interface_status():
            # if self.interface_status == 'up':
            delay = 5
            while delay > 0:
                if self.writer.check_host_connect():
                    return True
                    break
                else:
                    self.message_signal.emit(f"Попытка подключения {delay}")
                    time.sleep(1)
                    delay -= 1
            self.message_signal.emit("Терминал недоступен")
            return False
        else:
            self.message_signal.emit("Нет подключения к сетевому интерфейсу")

    def check_status(self, status):
        # self.interface_status = status
        self.interface_signal.emit(status)

    def check_change(self, signal):
        self.on_changed = signal

    def start_process(self):
        pass
