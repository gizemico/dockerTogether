class Device:
    device_number = int
    device_ip = str
    device_port = str
    device_password = str
    device_username = str
    def __init__(
        self, device_number, device_ip, device_port, device_username, device_password
    ):

        self.device_number = device_number
        self.device_ip = device_ip
        self.device_port = device_port
        self.device_username = device_username
        self.device_password = device_password

