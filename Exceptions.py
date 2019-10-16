class CustomError(Exception):
    """Base Class For Custom Exceptions"""

    def __init__(self, data=""):
        self.data = data


class RabbitMustBeDied(CustomError):
    """Raised when rabbit health is going to be negative"""
    pass


class NoMoreRabbit(CustomError):
    """Raised when there are no more rabbits in a field"""
    pass


class NoMoreCarrot(CustomError):
    """Raised when there are no more rabbits in a field"""
    pass


class NoMoreRooms(CustomError):
    """Raised when there are no more empty rooms in a field"""
    pass
