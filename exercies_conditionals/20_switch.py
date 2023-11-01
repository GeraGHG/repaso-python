
nums_words = ["zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
nums = [i for i in range(0, 10)]
dict_switch = dict(zip(nums, nums_words))
def switch_it(num):
    return dict_switch[num]

print(switch_it(5))
print(switch_it(1))