def hello_name(name):
    return 'Hello ' + name


# print(hello_name('Hamza'))


def make_abba(a, b):
    return a + b + b + a


# print(make_abba('Hi', 'Bye'))


def make_tags(tag, word):
    return '<{y}>{x}</{y}>'.format(y=tag, x=word)


# print(make_tags('i', 'Yay'))


def make_out_word(out, word):
    return out[0:2] + word + out[2:4]


# print(make_out_word('<<>>', 'Yay'))


def extra_end(str):
    length = len(str)
    last_two = str[length - 2: length]
    return last_two + last_two + last_two


#  end = str[-2:]
#  return end + end + end

# print(extra_end('hello'))


def first_two(str):
    return str[0: 2] if len(str) >= 2 else str


# print(first_two(''))

def first_half(str):
    return str[: int(len(str) / 2)]


# print(first_half('Woohoo'))


def without_end(str):
    return str[1: int(len(str) - 1)]


# print(without_end('Hello'))


def combo_Sring(a, b):
    return a + b + a if len(b) > len(a) else b + a + b


# print(combo_Sring('Hello', 'Hi'))


def non_start(a, b):
    return a[1:] + b[1:]


# print(non_start('Hello', 'There'))


def left2(str):
    return str[2:] + str[: 2]


#print(left2('Hello'))
