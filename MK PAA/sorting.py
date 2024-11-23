#Zaky Putra Safandra_F55123011
#Pseudocode Merge Sort
# MERGE-SORT(arr):
#     if length of arr > 1:
#         mid = length of arr // 2
#         left = arr[0:mid]
#         right = arr[mid:]

#         MERGE-SORT(left)
#         MERGE-SORT(right)

#         i = j = k = 0
#         while i < length of left and j < length of right:
#             if left[i] < right[j]:
#                 arr[k] = left[i]
#                 i = i + 1
#             else:
#                 arr[k] = right[j]
#                 j = j + 1
#             k = k + 1

#         while i < length of left:
#             arr[k] = left[i]
#             i = i + 1
#             k = k + 1

#         while j < length of right:
#             arr[k] = right[j]
#             j = j + 1
#             k = k + 1

#Big-O: 𝑂(𝑛log⁡𝑛)
#Penjelasan: Terdapat dua langkah utama: pembagian array (log⁡𝑛) dan penggabungan elemen-elemen (𝑛). Kombinasi ini memberikan kompleksitas 𝑂(𝑛log⁡𝑛).

# Big-Theta: Θ(𝑛log⁡𝑛)
#Penjelasan: Karena algoritma ini selalu membagi dan menggabungkan elemen dengan cara yang sama terlepas dari urutan input, kompleksitas waktu terbaik, rata-rata, dan terburuk adalah sama.

#Pseudocode Bubble Sort
# BUBBLE-SORT(arr):
#     n = length of arr
#     for i from 0 to n-1:
#         for j from 0 to n-i-2:
#             if arr[j] > arr[j+1]:
#                 swap(arr[j], arr[j+1])

#Big-O: 𝑂(𝑛^2)
#Penjelasan: Pada kasus terburuk, setiap elemen harus dibandingkan dengan elemen lainnya.


#Big-Theta: Θ(n^2)
#Penjelasan: Karena bubble sort membandingkan elemen satu per satu tanpa memperhatikan urutan awal, kompleksitas waktu rata-rata dan terburuk tetap (n^2)



#Implementasi Program dalam Python
#Berikut adalah implementasi Python untuk kedua algoritma, dengan pengurutan terhadap array berisi 100 angka acak.
import random
import time

# Merge Sort Implementation
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# Bubble Sort Implementation
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Generate random data
x = random.sample(range(1, 101), 100)  # 100 random integers
arr1 = x[:]
arr2 = x[:]

# Measure time for Merge Sort
start_time = time.time()
merge_sort(arr1)
merge_time = time.time() - start_time

# Measure time for Bubble Sort
start_time = time.time()
bubble_sort(arr2)
bubble_time = time.time() - start_time

print("Original Data: ", x)
print("Sorted with Merge Sort: ", arr1)
print("Sorted with Bubble Sort: ", arr2)
print(f"Merge Sort Time Complexity: {merge_time:.6f} seconds")
print(f"Bubble Sort Time Complexity: {bubble_time:.6f} seconds")