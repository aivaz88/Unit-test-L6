class CalculateAverageOfList:

    def __init__(self, new_list):
        self.new_list = new_list
        if not isinstance(new_list, list):
            raise TypeError("Вы ввели не список числе.")
        elif not new_list:
            self.average = 0
        else:
            self.average = sum(self.new_list) / len(self.new_list)

    def __gt__(self, other):
        return self.average > other.average
