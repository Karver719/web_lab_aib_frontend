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