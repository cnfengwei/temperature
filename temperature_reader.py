from pymodbus.client import ModbusSerialClient

class TemperatureReader:
    def __init__(self, port='/dev/ttyUSB0', baudrate=9600, timeout=0.5):
        self.serial_port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.client = ModbusSerialClient(port=port, baudrate=baudrate, timeout=timeout)

    def connect(self):
        return self.client.connect()

    def read_temperature(self):
        temperature_register = self.client.read_holding_registers(2, 2, unit=1)
        if temperature_register.registers:
            temperatures = []
            for value in temperature_register.registers:
                if value > 32767:
                    value = value - 65536  # 进行符号位扩展
                temperatures.append(value / 10)
            return temperatures
        else:
            return None

    def close(self):
        self.client.close()