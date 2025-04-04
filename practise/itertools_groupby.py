from itertools import groupby
from typing import Any, Iterator


words: list[str] = ['Cat', "Cactus", 'Owl', 'Dog', 'Orange', 'Bob', 'Blue', 'Bread']
grouped_words: groupby = groupby(sorted(words), key=lambda s: s[0])

for letter, group in grouped_words:
    print(f'Start with "{letter}": "{list(group)}"')

