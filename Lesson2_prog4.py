a_dict = dict()
a_dict = {'name' : 'ivan', 'second_name' : 'pup', 'brother' : 'yes', 'sister' : 'no'}
write = input("Check the dict: ")
if write in a_dict:
    print("This key is inside the dict.")
    print(write)
else:
    print("This key is outside the dict.")
