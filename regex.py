import re

text = "My phone number is 9876543210"
result = re.findall(r"\d+", text)

print(result)
print(re.match(r"Hello", "Hello Hasan"))