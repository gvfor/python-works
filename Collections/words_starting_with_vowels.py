text=["apple","iphone","orange","potatto"]

vowels_words=[w  for w in text if w[0] in ['a','e','i','o','u']]

print(vowels_words)

consonant_words=[w  for w in text if w[0] not in ['a','e','i','o','u']]

print(consonant_words)

long=max([len(w) for w in text])

longest_words=[w for w in text if len(w)==long]

print(longest_words)