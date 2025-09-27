file = open(r'D:\Delta Workout\FRONTEND\JS WorkShop\JS Part 4\break Keyword\index.html')
# print(file.read())

my_file = open('f1.py')
# my_file = open('e1.py') # FileNotFoundError
# print(my_file.read())

# photo = open("photo.txt", 'w')
photo = open("photo.txt", 'a')
photo.write("Tu Photo Helu...")
photo.write("Jaha kahibu bhul haba...")
photo.close()