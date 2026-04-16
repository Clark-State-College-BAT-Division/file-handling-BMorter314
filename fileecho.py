#Tead in the echo.txt file and display it in the terminal using print()
#This is a guided practice. Either follow the video or your instructor in class.

file = open("echo.txt", "r")
content = file.read()
print(content)
file.close()