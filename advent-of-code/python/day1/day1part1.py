from os import getcwd
calorie_count = 0
max_calories = 0
for line in open(getcwd()+"/advent-of-code/python/day1/input.txt", "r"):
    if line != "\n":
        calorie_count += int(line)
    else:
        if calorie_count > max_calories:
            max_calories = calorie_count
        calorie_count = 0
print(max_calories)

