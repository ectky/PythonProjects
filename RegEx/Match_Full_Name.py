import re

text = input()
pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

matches = re.findall(pattern, text)

for match in matches:
    print(match)
