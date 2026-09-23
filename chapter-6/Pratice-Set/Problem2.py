sub1 = int(input("Enter your mark in sub1: "))
sub2 = int(input("Enter your mark in sub2: "))
sub3 = int(input("Enter your mark in sub3: "))

percent = (sub1 + sub2 + sub3)/300 * 100

if(sub1 >= 33 and sub2 >= 33 and sub3 >= 33 and percent >= 40):
    print("Student is Pass")
else:
    print("Student is Fail. because student required: ", percent)