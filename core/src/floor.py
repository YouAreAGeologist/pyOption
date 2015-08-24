class Floor:
    def __init__(self, floorlets):
        self.__floorlets = floorlets

    def get_value(self):
        sum = 0
        for floorlet in self.__floorlets:
            sum += floorlet.get_value()
        return sum
