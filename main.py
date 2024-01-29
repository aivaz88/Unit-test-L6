import CalculateAverageOfList


def comparison(vol1, vol2):
    if vol1 > vol2:
        message = "Первый список имеет большее среднее значение"
    elif vol2 > vol1:
        message = "Второй список имеет большее среднее значение"
    else:
        message = "Средние значения равны"
    return message


list1 = CalculateAverageOfList.CalculateAverageOfList([1, 5, 8, 9, 10])
list2 = CalculateAverageOfList.CalculateAverageOfList([5, 5, 7, 10, 6])
print(comparison(list1, list2))
