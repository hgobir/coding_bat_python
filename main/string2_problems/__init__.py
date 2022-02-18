def double_char(str):
    new_str = ''
    for i in str:
        new_str += (i + i)
    return new_str


# print(double_char('The'))


# codingbat solution
# def double_char(str):
#   result = ""
#   for i in range(len(str)):
#     result += str[i] + str[i]
#   return result

def count_hi(str):
    if len(str) < 2:
        return 0
    else:
        count = 0
        for i in range(len(str)):
            potential_str = str[i] + str[i + 1]
            #        print(f'this is what potential_str is [{potential_str}]')
            if potential_str == 'hi':
                count += 1
                # i += 1
            if i == len(str) - 2:
                break

    return count


# print(count_hi('abc hi ho'))
# print(count_hi('ABChi hi'))
# print(count_hi('h'))
# print(count_hi('hi'))

# codingbat soliution

# def count_hi(str):
#   sum = 0
#   ## Loop to length-1 and access index i and i+1
#   ## in the loop.
#   for i in range(len(str)-1):
#     if str[i:i+2] == 'hi':
#       sum = sum + 1
#   return sum

def cat_dog(str):
    cat_count, dog_count = 0, 0
    for i in range(len(str) - 2):
        if str[i: i + 3] == 'cat':
            cat_count += 1
        elif str[i: i + 3] == 'dog':
            dog_count += 1

    return cat_count == dog_count


# print(cat_dog('1cat1cadodog'))

def count_code(str):
    count = 0
    for i in range(len(str) - 3):
        if str[i: i + 2] == 'co' and str[i + 3: i + 4] == 'e':
            count += 1
    return count


# print(count_code('cozexxcope'))

def end_other(a, b):
    # print(a[len(a) - 1: len(a)])
    # print(b[len(b) - 1: len(b)])
    # return a[len(a) - 1: len(a)].lower() == b[len(b) - 1: len(b)].lower()
    # return a.endswith(b[len(b) - 1: len(b)])
    a = a.lower()
    b = b.lower()

    print(f'first we are checking if a string [{a}] ends with b string [{b}] to which the answer is {a.endswith(b)}')
    print(f'next we are checking if b string [{b}] ends with a string [{a}] to which the answer is {b.endswith(a)}')
    return b.endswith(a) or a.endswith(b)


print(end_other('yz', '12xz'))
