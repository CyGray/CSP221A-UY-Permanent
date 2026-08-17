import abc


class InsufficientBatteryError(Exception):
    def __init__(self, name, required, available):
        self.name = name
        self.required = required
        self.available = available
        super().__init__(
            f"{name} needs {required}% battery for this task but only has {available}%."
        )


class Robot(abc.ABC):
    manufacturer = "Sarap Technologies Co. Ltd."
    population = 0

    def __init__(self, name, battery=100):
        self.name = name
        self.battery = battery
        Robot.population += 1

    @property
    def battery(self):
        return self._battery

    @battery.setter
    def battery(self, value):
        self._battery = max(0, min(100, value))

    def use_battery(self, amount):
        if amount > self.battery:
            raise InsufficientBatteryError(self.name, amount, self.battery)
        self.battery -= amount

    @abc.abstractmethod
    def perform_task(self, **kwargs):
        pass

    def __str__(self):
        return f"{self.name} ({self.battery}% battery)"

    def __repr__(self):
        return f"{type(self).__name__}(name={self.name!r}, battery={self.battery!r})"


class SaltedNutRobot(Robot):
    def __init__(self, name, battery=100, salt_capacity=5):
        super().__init__(name, battery)
        self.salt_capacity = salt_capacity

    def perform_task(self, **kwargs):
        self.use_battery(10)
        return f"{self.name} salted the nuts."


class CoatedNutRobot(Robot):
    def __init__(self, name, battery=100, coating_capacity=100):
        super().__init__(name, battery)
        self.coating_capacity = coating_capacity

    def perform_task(self, **kwargs):
        self.use_battery(15)
        return f"{self.name} coated the nuts."


def fleet_report(robots):
    for robot in robots:
        print(str(robot))
