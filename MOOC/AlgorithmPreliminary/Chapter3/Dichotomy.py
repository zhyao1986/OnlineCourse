
def Dichotomy(arr, x):
    high = len(arr) - 1
    low = 0
    while low <= high:
        mid = (low + high)//2
        if x == arr[mid]:
            return mid
        elif x < arr[mid]:
            high = mid - 1
            
            low = mid + 1
        print(f"low = {low}, high = {high}")

if __name__ == '__main__':
    arr = [2, 4, 6, 11, 12, 17, 28, 36, 39, 41]
    x = 45
    Dichotomy(arr, x)