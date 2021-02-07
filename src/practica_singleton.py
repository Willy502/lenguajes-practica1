class PracticaSingleton:

    __instance = None
    file = None
    lists = {}

    def __init__(self):
        if PracticaSingleton.__instance is None:
            PracticaSingleton.__instance = self
        else:
            raise Exception("Singleton already exists")

    @staticmethod
    def get_instance():
        if not PracticaSingleton.__instance:
            PracticaSingleton()
        return PracticaSingleton.__instance