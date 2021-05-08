n = int(input())
cnt = 0
series = 666
while True:
    if '666' in str(series):
        cnt += 1
    if cnt == n:
        print(series)
        break
    series += 1
