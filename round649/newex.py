import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = [1000000] * n
    p = 0
    st = []
    for i, x in enumerate(a):
        #print(b)

        st.append(i)
        if p < x:
            while st and p < x:
                b[st.pop()] = p
                p += 1

    print(' '.join(map(str, b)))
main()

