no_words = int(input("Enter the number of words: "))
lst = []

for i in range(no_words):
    words = input("Enter words here: ")
    lst.append(words)

output = sorted(lst, key=lambda x: x[-2])
print(output)