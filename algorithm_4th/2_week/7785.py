import sys

workPeople = set()
for _ in range(int(input())):
    name, status = sys.stdin.readline().rstrip().split()
    if status == 'enter':
        workPeople.add(name)
    else:
        if name in workPeople:
            workPeople.remove(name)

for i in sorted(workPeople, reverse=True):
    print(i)
