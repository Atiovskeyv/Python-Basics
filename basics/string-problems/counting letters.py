text = input('Enter a text:')
text = list(text)

print(text, '\n')


unique_chars = set(text)
if " " in unique_chars:
    unique_chars.remove(' ')

for i in unique_chars:
    print(i, 'Character appears', text.count(i), 'times in the list')
