students = {
    "Aman": [85, 78, 92],
    "Riya": [88, 90, 79],
    "Karan": [70, 65, 60],
    "Sneha": [95, 92, 96]
}

averages = {}

for name, marks in students.items():
    avg = sum(marks) / len(marks)
    averages[name] = avg

topper = max(averages, key=averages.get)

print("Averages:", averages)
print("Topper:", topper)

pass_count = sum(1 for avg in averages.values() if avg >= 40)
fail_count = len(averages) - pass_count

print("Pass:", pass_count)
print("Fail:", fail_count)

import matplotlib.pyplot as plt

names = list(averages.keys())
scores = list(averages.values())

plt.bar(names, scores)
plt.title("Student Average Scores")
plt.xlabel("Students")
plt.ylabel("Average Marks")

plt.show()