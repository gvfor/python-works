# lambda function for adding two numbers

add=lambda n1,n2:n1+n2
print(add(10,20))


# lambda function for subtracting two numbers

sub=lambda n1,n2:n1-n2
print(sub(10,2))


# lambda function for finding cube of a number

cube=lambda n1:n1**3
print(cube(5))


# lambda function for finding largest string

max_two=lambda str1,str2:str1 if len(str1)>len(str2) else str2

print(max_two("hai","morning"))


# smartsub =>largest number - number
smart_sub=lambda num1,num2:num1-num2 if num1>num2 else num2-num1
print(smart_sub(100,20))


# largest/smallest string by word count 
words=["hello","hai","morning","test","apple"]
def get_length(word):

    return len(word)

print(max(words,key=get_length))


# 2
text="this is a simple programming question to find word with  maximum number of characters"
# ASECENDING ORDER=>

# words=text.split(" ")

# def get_length(w):

#     return len(w)

# print(max(words,key=get_length))

# DESCENDING ORDER=>

# words=text.split(" ")

# def get_length(w):

#     return len(w)

# srt_words=sorted(words,key=get_length,reverse=True)

# print(srt_words)

# MOST FREQUANT WORDS=>

words=text.split(" ")

def get_length(w):

    return words.count(w)

frequent_word=max(words,key=get_length)

print(frequent_word)