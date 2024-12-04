words=["hello","hai","hello","this","is","this","is","hello"]

words_frequancy={w:words.count(w) for w in words}
print(words_frequancy)

recursive_characters=[k for k,v in words_frequancy.items() if v>1]
print(recursive_characters)