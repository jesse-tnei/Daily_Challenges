# while True:
#     print("Start of loop")
#     choice = input("Enter something (or type 'x' for continue, 'q' for quit): ").strip()
#
#     if choice == 'q':
#         print("Exiting loop")
#         break
#     if choice == 'x':
#         print("You chose to continue")
#         continue
#
#     print("You did not choose 'x' or 'q'")

i = 0
while i < 5:
    i += 1
    if i == 3:
        continue  # Skip the rest of the code for i == 3
    print(i)



