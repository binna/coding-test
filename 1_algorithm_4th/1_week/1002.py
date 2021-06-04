# n = int(input())
#
# for i in range(n):
#     x1, y1, r1, x2, y2, r2 = map(int, input().split())
#     distance = ((x1-x2)**2 + (y1-y2)**2) ** 0.5
#     data = [r1, r2, distance]
#     m = max(data)
#     data.remove(m)
#
#     if distance == 0 and r1 == r2:                  # 두 원이 일치하는 경우
#         print(-1)
#     elif distance == r1 + r2 or m == sum(data):     # 두 원이 한 점에서 만나는 경우(외접, 내접)
#         print(1)
#     elif sum(data) < m:                             # 두 원이 만나지 않는 경우
#         print(0)
#     else:                                           # 두 원이 두 점에서 만나는 경우
#         print(2)

n = int(input())

for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = ((x1-x2)**2 + (y1-y2)**2) ** 0.5
    R = [r1, r2, distance]
    m = max(R)
    R.remove(m)
    print(-1 if (distance == 0 and r1 == r2) else 1 if (distance == r1+r2 or m == sum(R)) else 0 if (m > sum(R)) else 2)
