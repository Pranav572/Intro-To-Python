medical=input("Did You Have A Medical Cause Y or N:")
atten=int(input("Enter Your Attendance:"))

if medical=="Y":
    print("You Are Allowed")
else:
    if atten>=75:
        print("You Are Allowed")

    else:
        print("You Are Not Allowed")
