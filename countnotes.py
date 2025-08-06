Amount=int(input("Enter The Amount For Withdrawal:"))
note_1=Amount//100
note_2=(Amount%100)//50
note_3=((Amount%100)%50)//10

print("Notes of 100Rs:", note_1)
print("Notes of 50Rs:", note_2)
print("Notes of 10Rs:", note_3)
