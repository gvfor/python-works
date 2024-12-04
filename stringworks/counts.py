
text="pneumonoultramicroscopicsilicovolcanoconiosis"

v_count=0

c_count=0

vowels_count=("a","e","i","o","u")


for ch in text:

    if ch in vowels_count:

        v_count=v_count+1

    else:
        c_count+=1



print("vowel count=",v_count)

print("consonant count=",c_count)

    


    