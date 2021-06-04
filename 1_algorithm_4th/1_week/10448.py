t = [n * (n + 1) // 2 for n in range(46)]


def isSamgaksuSum(target):
    # 브루트포스 알고리즘 이용!
    for idx1 in range(1, 46):
        for idx2 in range(1, 46):
            for idx3 in range(1, 46):
                if t[idx1] + t[idx2] + t[idx3] == target:
                    return 1
    return 0


for _ in range(int(input())):
    print(isSamgaksuSum(int(input())))
