class Resistor:
    __listColors = ["blank", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

    def getColorNumber(self, *color):
        print("el color es -> ", self.__colorToNumber(list(color[0:2])))
    
    def __colorToNumber(self, *color):
        return str(self.__listColors.index(color[0])) + str(self.__listColors.index(color[1]))