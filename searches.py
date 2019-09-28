def bsearch_helper(arr, key, low, high):
    if low > high:
        return False
    mid = (low + high)//2
    if arr[mid] == key:
        return True
    elif arr[mid] < key:
        return bsearch_helper(arr, key, mid + 1, high)
    else:
        return bsearch_helper(arr, key, low, mid - 1)
    return False

def bsearch(arr, key):
    return bsearch_helper(arr, key, 0, len(arr) - 1)

def lsearch(arr, key):
    return len(list(filter(lambda x: x == key, arr))) > 0

if __name__ == '__main__':
    arr = [8, 3, 9, 2, 6, 5, 1, 7, 4]
    #print (bsearch(sorted(arr), 5))
    print (lsearch(arr, 10))
