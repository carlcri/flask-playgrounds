class Truck:
    def __init__(self, model=None) -> None:
        self._model = model
    
    def get_model(self):
        print('returns model')
        return self._model
    
    def set_model(self, model):
        self._model = model

    model = property(fget=get_model,
                     fset=set_model,
                     doc='manages model')

    