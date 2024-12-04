signal=input("enter signal").lower()

if signal=="yellow":
    print("wait")
    
elif signal=="green":
    print("go")

elif signal=="red":
    print("stop")

else:
    print("invalid signal")