import os

source = "main.txt"
dest = "notmain.txt"

ask = input("Do you want to rename the file (main.txt = y / notmain.txt = n)?: ")

while ask == "y":
    os.rename(dest, source)

    ask = input("Do you want to rename the file (main.txt = y / notmain.txt = n)?: ")

else:
    os.rename(source, dest)

    ask = input("Do you want to rename the file (main.txt = y / notmain.txt = n)?: ")