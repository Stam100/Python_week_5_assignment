new_file = open("my_file.txt", "w")
file_content = new_file.writelines(["Country: Kenya\n", "The code is: ", str(254) + "\n", "City: Mombasa\n"])
new_file.close

new_file = open("my_file.txt", "a")
new_file.writelines(["Food: Chicken Biryani\n", "Tour site: Fort Jesus\n", "Guide's address: ", str(558972) + "\n"])
new_file.close

new_file = open("my_file.txt", "r")
print(new_file.read())
new_file.close

try:
    second_file = open("my_file.txt", "x")
    print("New file successfully created.")
except:
    print("File already exists.")
else:
    second_file.close
finally:
    print("Process completed.")