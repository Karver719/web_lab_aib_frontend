n = int(input())
sequence = list(map(int, input().split()))

medians_sum = 0
sorted_sequence = []

for i in range(n):
    sorted_sequence.append(sequence[i])
    sorted_sequence.sort()

if i % 2 == 0:
    median_index = i // 2
else:
    median_index = (i + 1) // 2 - 1

median = sorted_sequence[median_index]
medians_sum += median

print(medians_sum)