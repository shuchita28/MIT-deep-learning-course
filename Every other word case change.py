# Create a word list from the string stored in 'text'
word_list = text.split()

# Make every other word lowercased; otherwise - uppercased
for i in range(len(word_list)):
    if (i + 1) % 2 == 0:
        word_list[i] = word_list[i].upper()
    else:
        word_list[i] = word_list[i].lower()

print(word_list)

# Join the words back and form a new string
new_text = ' '.join(word_list)
print(new_text)
