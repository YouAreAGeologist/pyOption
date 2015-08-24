class Cap:
    def __init__(self, caplets):
        self.__caplets = caplets

    def get_value(self):
        sum = 0
        for caplet in self.__caplets:
            sum += caplet.get_value()
        return sum
