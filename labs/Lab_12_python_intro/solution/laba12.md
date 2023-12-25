### Задание 1

```python
    def count_ways(n, m):
        dp = [[0 for _ in range(m+2)] for _ in range(n+2)]
        dp[2][2] = 1

        for i in range(2, n+2):
        for j in range(2, m+2):
        dp[i][j] += dp[i-2][j-1] + dp[i-1][j-2]

        return dp[n+1][m+1]

        n, m = map(int, input().split())
    print(count_ways(n, m))
```
### Задание 2

```python
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
```

### Задание 3
```python
    def histogram(text):
    count = {}
    for char in text:
    if char not in (' ', '\n'):
    count[char] = count.get(char, 0) + 1

    max_count = max(count.values())

    histogram = []
    for i in range(max_count, 0, -1):
    row = ''
    for char in sorted(count.keys()):
    if count[char] >= i:
    row += '#'
    else:
    row += ' '
    histogram.append(row)

    histogram.append(''.join(sorted(count.keys())))

    return '\n'.join(histogram)

    encrypted_text = input()
    print(histogram(encrypted_text))
```
