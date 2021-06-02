# OOP


class Robot:
    FORWARD = 1
    BACKWARD = 2
    LEFT = 3
    RIGHT = 4
    UP = 5
    DOWN = 6
    MAX_SPEED = 15

    serial_number = 0

    def __init__(self, model, current_speed=0):
        print('__init__:', model, current_speed)
        self.model = model
        self.current_speed = current_speed
        self.serial_number = f'{self.model} - SN: {Robot.serial_number}'
        self.driver = ...  # main software of the robot
        Robot.serial_number += 1

    def move(self, speed, direction):
        self.driver

    def move_forward(self, speed):
        print(self.model, self.serial_number, 'Moving forward with current speed')
        self.move(speed, self.FORWARD)

    def move_backward(self, speed):
        print(self.model, self.serial_number, 'Moving backward with current speed')
        self.move(speed, self.BACKWARD)

    def move_left(self):
        print(self.model)
        self.move(self.LEFT)

    def move_right(self):
        print(self.model)
        self.move(self.RIGHT)


class SpotMini(Robot):
    def __init__(self, model, current_speed, current_weight):
        super().__init__(model, current_speed)
        self.current_weight = current_weight

    def move_forward(self, speed):
        print(self.model, self.serial_number, 'Moving forward with current speed')
        if self.current_weight > 25:
            self.current_speed = 0
            print('Error: Max weight limit exceeded')
        self.move(speed, self.FORWARD)


class Atlas(Robot):
    def __init__(self, model, current_speed, step=0.5, run=2):
        super().__init__(model, current_speed)
        self.step = step
        self.run = run

    def move_step(self, speed):
        print(self.model, 'Moving forward stepping')
        speed += self.step
        self.move(speed, self.FORWARD)

    def move_run(self, speed):
        print(self.model, 'Moving forward running')
        speed += self.run
        self.move(speed, self.FORWARD)

    def move_up(self, speed):
        print(self.model, 'Moving UP')
        self.move(speed, self.UP)

    def move_down(self, speed):
        print(self.model, 'Moving DOWN')
        self.move(speed, self.DOWN)


class Handle(Robot):
    def __init__(self, model, current_speed, battery_life):
        super().__init__(model, current_speed)
        self.battery_life = battery_life

    def move_limit(self):
        print(self.model)
        if self.battery_life <= 30:
            print('LOW BATTERY! Come back HOME!')

    def move_forward(self, speed):
        print(self.model, self.serial_number, 'Moving forward with current speed')
        if self.current_speed > Robot.MAX_SPEED:
            print('ATTENTION! You are moving too fast, SLOW DOWN!')


r = Handle('Test_Handle', 20, 31)
r.move_forward(20)

r2 = Atlas('Test_Atlas', 10)
r2.move_step(1)

r3 = SpotMini('Test_Spot_Mini', 10, 30)
r3.move_forward(10)


