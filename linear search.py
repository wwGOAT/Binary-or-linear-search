def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i  # Element indeksini qaytaradi
    return -1  # Agar element topilmasa, -1 qaytaradi

# Test qilish
arr = [3, 5, 2, 8, 10, 6]
x = int(input("x = "))
result = linear_search(arr, x)
if result != -1:
    print("Element", x, "indeksida", result)
else:
    print("Element topilmadi")
