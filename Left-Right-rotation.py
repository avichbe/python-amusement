a = [1, 2, 3, 4, 5]


def rotateRight(arr, d):

    return arr[-d:] + arr[:-d]
    
def rotateLeft(arr, d):
    return arr[d:] + arr[:d]

print(rotateRight(a, 6))
print(rotateLeft(a,5))

