products= [“Pride and Prejudice”, “To Kill a Mockingbird”, “The Great Gatsby”,\
“One Hundred Years of Solitude”, “Pride and Prejudice”, “In Cold Blood”, “Wide Sargasso Sea”,\
“One Hundred Years of Solitude”, “Brave New World”,  “The Great Gatsby”, “Brave New World”,\
“I Capture The Castle”, “Brave New World”, “The Great Gatsby”, “The Great Gatsby”,\
“One Hundred Years of Solitude”, “Pride and Prejudice”]
found = set()
found_again = set()
for a in products:
    if a in found_again:
        continue
    if a in found:
        found.remove(a)
        found_again.add(a)
    else:
        found.add(a)
print(list(found))