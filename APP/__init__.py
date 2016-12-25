print('Merry Christmas!!!')

import sys
#
# int main(int argc, char* argv[]) {
#     int n = argc > 1 ? atoi(argv[1]) : 4;
#     for (int j = 1; j <= n; j++) {
#         int s = 1 << j, k = (1 << n) - s, x;
#         for (int y = s - j; y >= 0; y--, putchar('\n')) {
#             for (x = 0; x < y + k; x++) printf("  ");
#             for (x = 0; x + y < s; x++) printf("%c ", '!' ^ y & x);
#             for (x = 1; x + y < s; x++) printf("%c ", '!' ^ y & (s - y - x - 1));
#         }
#     }
# }

def main(*args):
    # """上面的是我尝试尽量用最少代码来画一个抽象一点的圣诞树，因此树干都没有."""
    if args.__len__() > 1:
        n = args[1]
    else:
        n = 4
    for j in range(n):
        s = 1 << j
        k = (1 << n) - s
        x = 0
        for y in range(s - j)[::-1]:
            for x in range(y + k):
                print("  ", end="")
            for x in range(s - y):
                print("%s " % chr(ord('!') ^ y & x), end="")
            for x in range(1, s - y + 1):
                print("%s " % chr(ord('!') ^ y & (s - y - x - 1)), end="")
            print("")


if __name__ == "__main__":
    main(sys.argv)
