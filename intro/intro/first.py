# '''we want to print the patient age , name and number.'''
# patient_name= "Ram Thapa"
# patient_age=38
# patient_number= "9845671230"
# print("Patient Name:",patient_name)
# print("patient age:", patient_age)
# print("patient number:",patient_number)
# is_new_patient=True
# patient ={"name":"Ram Thapa", "age":38 ,"number":"9845671230"}
# print(patient)
# for val in patient.keys():
#     print(val)



# '''making the simple calculator'''
# print("Welcome to the simple calculator")
# print("Here are your options:")
# print("1.Addition")
# print("2.Subtraction")
# print("3.Multiplication")
# print("4.Division")
# choice=int(input("Enter the operration that you want to run:"))

# print("You have selected option:", choice)
# if choice in [1,2,3,4]:
#     num1=int(input("Enter first number:"))
#     num2=int(input("Enter second number:"))

# if (choice==1):
#     Result= (num1)+(num2)
# elif (choice==2):
#     Result=(num1)-(num2)
# elif (choice==3):
#     Result= (num1)*(num2)
# elif (choice==4):
#     Result=(num1)//(num2)
# else:
#     print("Invalid choice selected")

# print("The result is:",Result)

# # '''finding the ASCII value of the charater'''
# # letter= input("Enter the character:")
# # print("The ASCII value of the letter is:", ord(letter))

# sorting the following using the selection sort
arr=[64, 25, 12, 22, 11]
for i in range(len(arr)):
 min_index=i
 for j in range(i+1, len(arr)):
    if arr[j]<arr[min_index]:
        min_index=j
 arr[i], arr[min_index]= arr[min_index], arr[i] 

 print("Sorted list:", arr)
 