arr=[1,22,33,45,6,7,8,9]


search_element=int(input("enter number"))

arr.sort()

low=0

upp=len(arr)-1

is_present=False

while(low<=upp):

    mid=(low+upp)//2

    if search_element==arr[mid]:

        is_present=True

        break

    elif search_element<arr[mid]:

        upper=mid-1

    elif search_element>arr[mid]:

        low=mid+1

print(is_present)
