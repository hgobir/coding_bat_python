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

#def rotate_left3(nums):
#    return nums[1:2] + nums[0]

#print(rotate_left3([1,2,3]))
