import re

string = ""
text = input()

while text != 'end':
    string += text
    text = input()

pattern = r"<a href=\"(.+)\">(.+)</a>"

match = re.search(pattern, string)
while match != None:
    newString = "[URL href={0}>{1}[/URL]".format(match.group(1), match.group(2))
    string = string.replace(match.group(0), newString)
    match = re.search(pattern, string)

print(string)
