import time
from PyQt5 import QtCore
from writer import Writer

class WritterThread(QtCore.QThread):
    message_signal = QtCore.pyqtSignal(str)
    interface_signal = QtCore.pyqtSignal(str)

    def __init__(self, int_name, ip_address, username, password, model):
        super(WritterThread, self).__init__()
        self.int_name = int_name
        self.ip_address = ip_address
        self.username = username
        self.password = password
        self.model = model
        self.writer = Writer(self.int_name, self.ip_address, self.username, self.password)


    def run(self) -> None:
        # self.writer = Writer(self.int_name, self.ip_address, self.username, self.password)
        self.message_signal.emit("")
        if self.wait_to_connect():
            self.message_signal.emit("Terminal connected. Writing")
            self.writer.start_write(self.model)
            self.message_signal.emit("Writing complete! Connect next terminal and click Start button")


    def wait_to_connect(self):
        if self.writer.interface_status():
            delay = 5
            while delay > 0:
                if self.writer.check_host_connect():
                    return True
                    break
                else:
                    self.message_signal.emit(f"Attempt to connect {delay}")
                    time.sleep(1)
                    delay -= 1
            # self.update_interface_status("Terminal is not available")
            self.message_signal.emit("Terminal is not available")
            return False
        else:
            self.message_signal.emit("Not connected")
            return False








