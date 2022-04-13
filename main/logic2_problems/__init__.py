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
