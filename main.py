import json


class ModelProto:
    def __init__(self, initial_values):
        self._initial_values = initial_values.copy()
        self._properties = initial_values.copy()

    def __setattr__(self, name, value):
        if hasattr(self, '_properties') and name in self._properties and self._properties[name] != value:
            self._properties[name] = value
        super().__setattr__(name, value)

    def generateDelta(self):
        delta = {}
        for key, value in self._properties.items():
            if value != self._initial_values.get(key):
                delta[key] = value
        return json.dumps(delta)  # Serialize the delta as JSON


class ModelA(ModelProto):
    def __init__(self, initial_values):
        super().__init__(initial_values)
        self.propertyA = initial_values.get('propertyA')
        self.propertyB = initial_values.get('propertyB')
        self.propertyC = initial_values.get('propertyC')


initial_values = {
    'propertyA': 'initial value 1',
    'propertyB': 'initial value 2',
    'propertyC': 42
}

if __name__ == '__main__':

    modelInstance = ModelA(initial_values)

    # Modify properties
    modelInstance.propertyA = 'new value 1'
    modelInstance.propertyC = 100

    # Generate Delta event as a JSON string
    delta = modelInstance.generateDelta()
    print(delta)
