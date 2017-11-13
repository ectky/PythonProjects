import re

pattern = r"(\+359([ -])2\2\d{3}\2\d{4}\b)"
text = input()

matches = re.findall(pattern, text)
for match in matches:
    print(match[0])
