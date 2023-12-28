def to_characters_histogram(text: str):
    chars = {}
    for char in filter(lambda char: not char.isspace(), text):
        chars.update({char : chars.get(char, 0) + 1})
    sorted_columns = sorted(chars.items())
    max_height = max(chars.values())
    sorted_text_columsn = "\n".join("".join(["#" if height <= column[1] else " " for column in sorted_columns]) for height in range(max_height, 0, -1))
    return sorted_text_columsn + "\n" + "".join([column[0] for column in sorted_columns])

if __name__ == '__main__':
    text = input()
    print(to_characters_histogram(text))