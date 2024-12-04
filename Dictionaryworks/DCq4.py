text="ababbccdde"

character_frequancy={char:text.count(char) for char in text}

print(character_frequancy)


# print non recursive elements

for k,v in character_frequancy.items():

    if v==1:
        print(k)

# dictionary comprehension
non_recursive_character={k for char in character_frequancy.items() if v==1}
print(non_recursive_character)


