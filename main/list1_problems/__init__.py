def first_last6(nums):
    return nums[0] == 6 or nums[len(nums) - 1] == 6


# print(first_last6([1, 2, 4, 6]))

def same_first_last(nums):
    return len(nums) > 1 and nums[0] == nums[-1]


# print(same_first_last([1,2,3, 1]))

def make_pi():
    return [3, 1, 4]


# print(make_pi())

def common_end(a, b):
    return a[0] == b[0] or a[-1] == b[-1]


# print(common_end([1,2,3], [675.3, 3]))


def sum3(nums):
    return nums[0] + nums[1] + nums[2]


# print(sum3([1,2,3]))

def rotate_left3(nums):
    return [nums[1], nums[2], nums[0]]


# print(rotate_left3([1,2,3]))


def reverse3(nums):
    return [nums[2], nums[1], nums[0]]


# print(reverse3([1,2,3]))

def max_end3(nums):
    return [nums[0], nums[0], nums[0]] if nums[0] > nums[2] else [nums[2], nums[2], nums[2]]


# print(max_end3([1,2,3]))


def middle_Waysum2(nums):
    if len(nums) == 0:
        return 0
    return nums[0] + nums[1] if len(nums) >= 2 else nums[0]


#print(sum2([]))


def middle_Way(a, b):
    return [a[1], b[1]]


#print(middle_Way([1,2,3], [4,5,6]))



def make_ends(nums):
    return [nums[0], nums[-1]] if len(nums) > 1 else [nums[0], nums[0]]

#print(make_ends([1]))


def has23(nums):
    return 2 in nums or 3 in nums

print(has23([1]))