#  O(n) time | O(1) space

a1 = [5,1,22,25,6,-1,8,10]
a2 = [1,6,-1,10]

def validateSubsequence(array1,array2):
    pointer2 = 0
    pointer1 = 0

    while pointer2 < len(array2) and pointer1 < len(array1):
        if array2[pointer2] == array1[pointer1]:
            pointer2 += 1
        pointer1 += 1
    return pointer2 == len(array2)

x = validateSubsequence(a1,a2)

print(x)
