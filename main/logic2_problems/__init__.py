# need to think and code for failures/ edge cases first!!!
# my solution that didnt solve all edge cases follows then coding bat solution after


# def make_bricks(small, big, goal):
#     small_tuple = (small, 1)
#     big_tuple = (big, 5)
#     total_big = big * 5
#
#     # print(f'modulo of number of small bricks [{small}] is {goal % small}')
#     # print(f'modulo of number of big bricks [{big}] is {goal % big}')
#     # print(f'modulo of total big bricks [{total_big}] is {goal % total_big}')
#
#     print(f'{goal % 5}')
#
#     multiple_of_five = goal % 5 == 0
#
#     # print(multiple_of_five)
#
#     if multiple_of_five and total_big >= goal:
#         return True
#
#     # near_multiple_of_five = goal % 5 == 1
#     #
#     # if near_multiple_of_five:
#     #     return small >= 1
#     #     coefficient = goal / 5
#     #     if coefficient <= big:
#
#     nearly = total_big - goal == 1
#
#     print(f'{nearly}')
#
#     if nearly:
#         return False
#
#     if total_big >= goal:
#         return total_big % goal == 0 or (total_big % goal) <= small or (goal - small) % 5 == 0
#     else:
#         return (total_big + small) == goal or (total_big + small) > goal


# coding bat solution
def make_bricks(small, big, goal):
    if goal > big * 5 + small:
        return False

    if goal % 5 > small:
        return False

    return True


# print(make_bricks(3, 1, 8)) # True
# print(make_bricks(3, 1, 9) # False
# print(make_bricks(3, 2, 10)) # True
# print(make_bricks(3, 2, 9))  # True


def lone_sum(a, b, c):
    if a != b and b != c and c != a:
        return a + b + c
    elif a == b and a != c:
        return c
    elif a == c and a != b:
        return b
    elif b == c and c != a:
        return a
    else:
        return 0


# print(lone_sum(3,2,3))
# print(lone_sum(3,3,3))

# coding bat solution

# def lone_sum(a, b, c):
#   sum = 0
#   if a != b and a != c: sum += a
#   if b != a and b != c: sum += b
#   if c != a and c != b: sum += c
#
#   return sum


def lucky_sum(a, b, c):
    sum = 0

    if a != 13:
        sum += a
    else:
        return sum

    if b != 13:
        sum += b
    else:
        return sum

    if c != 13:
        sum += c
    else:
        return sum

    return sum


# print(lucky_sum(1, 13, 3))
# print(lucky_sum(13, 2, 3))


def no_teen_sum(a, b, c):
    new_a = fix_teen(a)
    new_b = fix_teen(b)
    new_c = fix_teen(c)
    return new_a + new_b + new_c


def fix_teen(n):
    # if 13 <= n < 15 and 17 <= n < 20:
    if 13 <= n < 15:
        return 0
    else:
        return 0 if 17 <= n < 20 else n


# print(no_teen_sum(1,2,3))
# print(no_teen_sum(2,13,1))
# print(no_teen_sum(2,1,14))


# print(3 % 10)
def round_sum(a, b, c):
    new_a = round10(a)
    new_b = round10(b)
    new_c = round10(c)
    return new_a + new_b + new_c


def round10(num):
    remainder = num % 10
    new_num = num - remainder if remainder < 5 else num + (10 - remainder)
    return new_num


# print(round_sum(16, 17, 18))

# coding bat solutions below!
# def round_sum(a, b, c):
#     return round10(a) + round10(b) + round10(c)
#
#
# def round10(num):
#     mod = num % 10
#     num -= mod
#     if mod >= 5: num += 10
#     return num


def close_far(a, b, c):
    if (abs(a - b) <= 1 and abs(a - c) >= 2) or (abs(a - c) <= 1 and abs(a - b) >= 2):
        return abs(b - c) >= 2
    return False


# print(close_far(1,2,10))
# print(close_far(1,2,3))
# print(close_far(4,1,3))
# print(close_far(10,10,8))


def make_chocolate(small, big, goal):
    total_big = big * 5

    if total_big + small == goal:
        return small

    if 0 <= (goal - total_big) <= small:
        total_left = goal - total_big
        print(total_left)
        return total_left - small

    return -1


# print(make_chocolate(4, 1, 9))
# print(make_chocolate(4, 1, 10))
print(make_chocolate(4, 1, 7))
