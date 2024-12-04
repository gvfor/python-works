text="abaabbc"

text.split()

def get_length(w):

    return text.count(w)

frequent_word=max(text,key=get_length)

print(frequent_word)
