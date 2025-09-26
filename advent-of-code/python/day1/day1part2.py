from os import getcwd
calorie_count = 0
top_three = [0,0,0]
for line in open(getcwd()+"/advent-of-code/python/day1/input.txt", "r"):
    if line != "\n":
        calorie_count += int(line)
    else:
        top_three = top_three + [calorie_count]
        top_three.sort(reverse=True)
        top_three.pop()
        calorie_count = 0

print(top_three)
print(sum(top_three))

