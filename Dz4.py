class Computer:
    def __init__(self, model, processor, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model
        self.processor = processor
        self.memory = 128

    def upgrade_memory(self, additional_memory):
        self.memory += additional_memory
        print(f"Memory upgraded to {self.memory} GB")


class Display:
    def __init__(self, screen_size, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.screen_size = screen_size
        self.resolution = "4K"

    def change_resolution(self, new_resolution):
        self.resolution = new_resolution
        print(f"Resolution changed to {self.resolution}")


class SmartPhone(Display, Computer):
    def __init__(self, model, processor, screen_size, battery_life):
        super().__init__(model=model, processor=processor, screen_size=screen_size)
        self.battery_life = battery_life

    def print_info(self):
        print(f"Model: {self.model}")
        print(f"Processor: {self.processor}")
        print(f"Memory: {self.memory} GB")
        print(f"Screen Size: {self.screen_size} inches")
        print(f"Resolution: {self.resolution}")
        print(f"Battery Life: {self.battery_life} hours")

    def charge_battery(self, hours):
        self.battery_life += hours
        print(f"Battery charged. New battery life: {self.battery_life} hours")


# Создание объекта смартфона
iphone = SmartPhone(model="POCO", processor="Snapdragon 888", screen_size=6.5, battery_life=20)
iphone.print_info()
iphone.upgrade_memory(64)
iphone.change_resolution("1080p")
iphone.charge_battery(5)
