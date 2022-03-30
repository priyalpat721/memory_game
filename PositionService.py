class PositionService:
    singleton = None

    def __init__(self):
        self.x = 0
        self.y = 0
        self.visible = True

    # a class method to create a Person object by birth year.
    @classmethod
    def get_instance(cls):
        if PositionService.singleton == None:
            PositionService.singleton = PositionService()
        return PositionService.singleton


# non OO service api

def set_position_x(x):
    instance = PositionService.get_instance()
    instance.x = x


def set_position_y(y):
    instance = PositionService.get_instance()
    instance.y = y


def set_position(x, y):
    instance = PositionService.get_instance()
    instance.x = x
    instance.y = y


def get_position_x():
    instance = PositionService.get_instance()
    return instance.x


def get_position_y():
    instance = PositionService.get_instance()
    return instance.y


def is_visible():
    instance = PositionService.get_instance()
    return instance.visible


def set_visible(visibility):
    instance = PositionService.get_instance()
    instance.visible = visibility
