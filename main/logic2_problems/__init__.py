# small = 1 inch, big = 5 inches
def make_bricks(small, big, goal):
    small_tuple = (small, 1)
    big_tuple = (big, 5)
    total_big = big * 5

    # print(f'modulo of number of small bricks [{small}] is {goal % small}')
    # print(f'modulo of number of big bricks [{big}] is {goal % big}')
    # print(f'modulo of total big bricks [{total_big}] is {goal % total_big}')
    print(f'{total_big % goal}')

    if total_big >= goal:
        return True if total_big % goal == 0 else (total_big % goal) <= small
    else:
        return (total_big + small) == goal or (total_big + small) > goal


# print(make_bricks(3, 1, 8)) # True
# print(make_bricks(3, 1, 9) # False
# print(make_bricks(3, 2, 10)) # True
print(make_bricks(3, 2, 9)) # True
