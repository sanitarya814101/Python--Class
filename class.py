class Car(object):
    def __init__(self, model, color, company, speed):
        self.model = model
        self.color = color
        self.company = company
        self.speed = speed

    def start(self):
        print('Started')

    def stop(self):
        print("Stopped")


audi = Car('a6', 'black', 'audi', '60km/s')
print(audi.color)
audi.start()
