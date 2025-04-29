def countSwaps(a,n):
    move = True
    count = 0
    while move:
        move = False
        for i in range(n-1):
            if a[i]>a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                count += 1 
                move = True
    # Write your code here
    print(f"Array is sorted in {count} swaps.")
    print (f"First Element: {a[0]}" )
    print (f"Last Element: {a[-1]}")
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a,n)