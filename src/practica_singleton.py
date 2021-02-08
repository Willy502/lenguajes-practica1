class PracticaSingleton(object):

    __instance = None
    file = None

    def __new__(cls):
        if PracticaSingleton.__instance is None:
            PracticaSingleton.__instance = object.__new__(cls)
        return PracticaSingleton.__instance