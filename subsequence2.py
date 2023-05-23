#  O(n) time | O(1) space

a1 = [5,1,22,25,6,-1,8,10]
a2 = [1,6,-1,10]

def validateSubsequence(array1,array2):
    pointer = 0

    for value in array1:
        if pointer == len(array2):
            break
        if array2[pointer] == value:
            pointer += 1
    return pointer == len(array2)

x = validateSubsequence(a1,a2)

print(x)
