def get_avr(list1):
    sum = 0
    if len(list1) > 1:
        for i in list1:
            sum = sum + i
        avr = sum / len(list1)
        return avr
    else:
        return -1
