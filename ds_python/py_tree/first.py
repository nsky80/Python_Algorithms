#
# def max_len(a, b, c):
#     if a == b:
#         return a + b + 2 * c
#     elif b > a:
#         return (2*a + 1) + 2 * c
#     else:
#         return 2 * b + 1 + 2 * c
#
#
#
# if __name__ == "__main__":
#     print(max_len(*map(int, input().rstrip().split())))

"""
4 5 1 1 2
1 3 5 7
1 2 3 9 10"""


def nearest(data, b):

    z = 0
    nb = len(b)
    while z < nb and data > b[z]:
        z += 1
    return z


def find_flight(n, m, ta, tb, k, a, b):
    if n <= k or m <= k:
        return -1
    a = list(map(lambda y: y + ta, a))

    while k > 0:
        i = 0
        j = 0
        ax1 = nearest(a[i], b)
        ax2 = nearest(a[i+1], b)

        ac = a[i+1] + b[ax2]    # Cancel ai
        if ax1 == ax2 and ax2 < m - 1:
            ax2 += 1
        bc = a[i] + b[ax1 + 1]    # cancel bj
        if bc > ac:
            b = b[ax2 + 1:]
        else:
            a = a[i + 1:]
            b = b[ax2:]
        k -= 1
    if len(b) > 0:
        return b[0] + tb
    else:
        return -1



if __name__ == "__main__":
    n, m, ta, tb, k = map(int, input().rstrip().split())
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    print(find_flight(n, m, ta, tb, k, a, b))
