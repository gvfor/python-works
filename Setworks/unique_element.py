arr=[10,10,10,20,30,40,50]

st=set()


for num in arr:

    st.add(num)

# print(st)


st1={10,20,30,40}

st2={10,20,40,50}

intersection_elements=st1.intersection(st2)

# print(intersection_elements)

union_set=st1.union(st2)

# print(union_set)

difference_set=st1.difference(st2)

# print(difference_set)

st1.remove(40)

# print(st1)


text="this is a test to remove duplicate words this test is simple"

text2="this simple test remove duplicate words"

words=text.split(" ")

# print(set(words))

