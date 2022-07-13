import time
from PyQt5 import QtCore
from writer import Writer
# from interface_thread import InterfaceStatusThread


class WriterThread(QtCore.QThread):
    message_signal = QtCore.pyqtSignal(str)
    interface_signal = QtCore.pyqtSignal(str)

    def __init__(self, int_name, ip_address, username, password, model):
        super(WriterThread, self).__init__()
        # self.int_state = "down"
        self.int_name = int_name
        self.ip_address = ip_address
        self.username = username
        self.password = password
        self.model = model
        # self.on_changed = None
        # self.interface_thread = None
        # self.interface_status = None
        self.write_running = True
        self.writer = Writer(self.int_name, self.ip_address, self.username, self.password)

    def run(self) -> None:
        self.single_write()

    def single_write(self):
        # одиночный телнет сеанс
        self.message_signal.emit("")
        # self.message_signal.emit("Подлючите терминал")
        if self.wait_to_connect():
            self.message_signal.emit("Терминал подключен. Выполняется настройка.")
            self.writer.start_write(self.model)
            self.message_signal.emit("Настройка завершена. Подключите следующий терминал.")
        self.write_running = False

    def wait_to_connect(self):
        if self.writer.interface_status():
            delay = 30
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

