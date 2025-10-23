

class BAPInstance:
    def __init__(self, data):
        self.data = data




class BAPEnvironment:
    def __init__(self, instance=None):
        if instance is None:
            instance = self.get_random_instance()
        self.instance = instance


    def reset(self, instance=None):
        if instance is None:
            instance = self.get_random_instance()
        self.instance = instance
        
        