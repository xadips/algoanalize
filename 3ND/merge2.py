
def merge_sort(A):
    n = len(A)
    if n == 1:
        return A
    else:
        mid = n//2
        return merge2(merge_sort(A[:mid]), merge_sort(A[mid:]))


def merge2(A, B):
    i = 0
    j = 0
    n = len(A)
    m = len(B)
    C = [0] * (m+n)
    for k in range(m+n):
        if i < m:
            if j < n:
                if A[i] < B[j]:
                    print(str(A[i]) + " < " + str(B[j]) + " ? T")
                    C[k] = A[i]
                    i = i + 1
                else:
                    print(str(A[i]) + " < " + str(B[j]) + " ? F")
                    C[k] = A[i]
                    C[k] = B[j]
                    j = j + 1
            else:
                C[k] = A[i]
                i = i + 1
        else:
            C[k] = B[j]
            j = j + 1
    return C


if __name__ == '__main__':
    print(merge_sort([66, 22, 10, 50, 80, 13, 49, 72]))
