def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid  # Element indeksini qaytaradi
    return -1  # Agar element topilmasa, -1 qaytaradi

# Test qilish (bu ro'yxatni oldin tartiblang)
arr = [2, 3, 5, 6, 8, 10]
x = int(input("Enter a number: "))
result = binary_search(arr, x)
if result != -1:
    print("Element", x, "indeksida", result)
else:
    print("Element topilmadi")
