def insertionSort1(n, arr):
    # Write your code here
    target = arr[-1]
    i = n-1
    while i > 0 and arr[i-1] > target:
        arr[i] = arr[i-1]
        print(*arr)
        i -= 1
    arr[i] = target
    print(*arr)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)