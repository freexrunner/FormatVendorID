import os
import telnetlib
import subprocess
import time
# import getpass


def to_bytes(line):
    return f"{line}\r".encode("ascii")


commands_snr = ['gccli sys vendor HWTC', 'gccli sys vendorid HWTC', 'gccli sys save']
commands_bo = ['flash set PON_VENDOR_ID HWTC', 'flash set GPON_SN HWTC00123456']
commands_bo_test = ['show version', 'show version']
commands_snr_test = ['gccli sys show', 'gccli sys version', 'gccli sys vendorid']



class Writer:
    def __init__(self, int_name, ip_address, username, password):
        self.int_name = int_name
        self.ip_address = ip_address
        self.username = username
        self.password = password

    def start_write(self, terminal_model):
        # отправка команд по Telnet
        with telnetlib.Telnet(self.ip_address) as telnet:
            # time.sleep(1)
            telnet.read_until(b"Username", timeout=1)
            telnet.write(to_bytes(self.username))
            # time.sleep(1)
            telnet.read_until(b"Password", timeout=1)
            telnet.write(to_bytes(self.password))
            # time.sleep(1)
            if terminal_model == 0:
                for command in commands_snr_test:
                    telnet.write(to_bytes(command))
                    time.sleep(1)
                telnet.close()
            elif terminal_model == 1:
                for command in commands_bo_test:
                    telnet.write(to_bytes(command))
                    time.sleep(1)
                telnet.close()
            else:
                telnet.close()
        telnet.close()
        # pass

    def interface_status(self):
        # проверка состояния сетевого интерфейса
        int_file = '/sys/class/net/' + self.int_name + '/operstate'
        # int_file = '/sys/class/net/enp3s0/operstate'
        with open(int_file) as f:
            int_status = f.readline().rstrip()
        if int_status == 'up':
            return True
        elif int_status == 'down':
            return False

    def check_host_connect(self):
        # проверка доступности терминала
        response = os.system("ping -c 1 " + self.ip_address)
        if response == 0:
            return True
        else:
            return False
