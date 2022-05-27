import telnetlib


def to_bytes(line):
    return f"{line}\n".encode("utf-8")


commands_snr = ['gccli sys vendor HWTC', 'gccli sys vendorid HWTC', 'gccli sys save']
commands_bo = ['flash set PON_VENDOR_ID HWTC', 'flash set GPON_SN HWTC00123456']


class Writer:
    def __init__(self, int_name, ip_address, username, password):
        self.int_name = int_name
        self.ip_address = ip_address
        self.username = username
        self.password = password

    def start_write(self, terminal_model):
        # self.interface_status()
        # self.check_host_connect()
        with telnetlib.Telnet(self.ip_address) as telnet:
            telnet.write(to_bytes(self.username))
            telnet.write(to_bytes(self.password))
            if terminal_model == 0:
                for command in commands_snr:
                    telnet.write(to_bytes(command))
            elif terminal_model == 1:
                for command in commands_bo:
                    telnet.write(to_bytes(command))
            else:
                telnet.close()
            telnet.close()
        # pass

    def interface_status(self):
        pass

    def check_host_connect(self):
        pass
