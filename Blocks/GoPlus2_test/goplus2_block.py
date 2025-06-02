
"""
file     GoPlus2
time     2025-06-02
author   
email   
license  MIT License
"""



class GoPlus2:
    """
    note: ''
    details:
        color: '#d2760f'
        link: ''
        image: ''
        category: Custom
    example: ''
    """




    def __init__(self):
        """
        label:
            en: '%1 init'
        """
        pass

    def move_motor(self, motor: str = '"1"', speed: int = 0):
        """
        label:
            en: method %1 Motor %2 Speed %3
        params:
            motor:
                name: motor
                type: str
                default: '"1"'
            speed:
                name: speed
                type: int
                default: '0'
                field: number
        """
        pass

    def servo_pwm(self, motor: str = '"1"', micros: int = 0):
        """
        label:
            en: method %1 Motor %2 PWM (µs) (500-2500 µs) 1500 µs és STOP %3
        params:
            motor:
                name: motor
                type: str
                default: '"1"'
            micros:
                name: micros
                type: int
                default: '0'
                field: number
        """
        pass


