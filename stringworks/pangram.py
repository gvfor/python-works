text="the quick brown fox jumps over the lazy dog"

alpha="abcdefghijklmnopqrstuvwxyz"

is_pangram=True


for ch in alpha:

    if ch not in text:

        is_pangram=False

        break

print(is_pangram)

