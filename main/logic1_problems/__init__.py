def cigar_party(cigars, is_weekend):
    if 40 <= cigars <= 60:
        print("cigars are in correct range - always return true")
        return True
    elif cigars < 40:
        return False

    if is_weekend:
        print("its the weekend so doesnt matter how many cigars - always return true")
        return True
    else:
        return False


# def cigar_party(cigars, is_weekend):
#   if is_weekend:
#     return (cigars >= 40)
#   else:
#     return (cigars >= 40 and cigars <= 60)


# print(cigar_party(30, False))
# print(cigar_party(50, False))
# print(cigar_party(70, True))
# print(cigar_party(30, True))

def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    elif you >= 8 or date >= 8:
        return 2
    else:
        return 1


# print(date_fashion(5, 10))
# print(date_fashion(5, 2))
# print(date_fashion(5, 5))


def squirrel_play(temp, is_summer):
    if is_summer:
        return 60 <= temp <= 100
    else:
        return 60 <= temp <= 90


# print(squirrel_play(70, False))
# print(squirrel_play(95, False))
# print(squirrel_play(95, True))

def caught_speeding(speed, is_birthday):
    if (speed > 85 and is_birthday) or (speed > 80 and not is_birthday):
        return 2
    elif (65 < speed <= 85 and is_birthday) or (60 < speed <= 80 and not is_birthday):
        return 1
    else:
        return 0


# print(caught_speeding(60, False))
# print(caught_speeding(65, False))
# print(caught_speeding(65, True))


def sorta_sum(a, b):
    return (a + b) if not 10 <= (a + b) <= 19 else 20


# print(sorta_sum(3, 4))
# print(sorta_sum(9, 4))
# print(sorta_sum(10, 11))


def alarm_clock(day, vacation):
    if not vacation:
        return '10:00' if day == 0 or day == 6 else '7:00'
    else:
        return 'off' if day == 0 or day == 6 else '10:00'

#print(alarm_clock(1, False))
#print(alarm_clock(5, False))
#print(alarm_clock(0, False))

#print(alarm_clock(6, True))

def love6(a, b):
    return a == 6 or b == 6 or a + b == 6 or a - b == 6 or b - a == 6

#print(love6(-7, 1))

def in1to10(n, outside_mode):
    return (not outside_mode and 1 <= n <= 10) or (outside_mode and not 1 < n < 10)


#print(in1to10(1, True))


def near_ten(num):
    return (num % 10) <= 2 or 8 <= (num % 10) <= 9

#print(near_ten(12))
#print(near_ten(18))
#print(near_ten(158))
#print(near_ten(19))





