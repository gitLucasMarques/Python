import random

nums = []
for i in range (0,20):
    nums.append(random.randint(0,20))
    
target = random.randint(0, 20)

print(nums)
print("\n",target)

def twoSum(nums, target):

    tuple_nums = tuple(nums)

    for i in tuple_nums:
        prime = i
        pos_prime = tuple_nums.index(prime)
        second = target - i

        if(second == prime):
            listTwo = nums
            del listTwo[pos_prime]
            verific = listTwo.count(second)

            if(verific != 0):
                pos_second = listTwo.index(second)
                return print("\nOutput: [",pos_prime,",",pos_second + 1,"]\n")

            else:
                pos_prime = -1
                pos_second = -1

        else:
            verific = tuple_nums.count(second)
            
            if(verific != 0):
                pos_second = tuple_nums.index(second)
                return print("\nOutput: [",pos_prime,",",pos_second,"]\n")

            else:
                pos_prime = -1
                pos_second = -1
    
    if(pos_prime == -1 and pos_second == -1):
        print("\nPar não encontrado na lista dada.\n")

resultado = twoSum(nums, target)
resultado