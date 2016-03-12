fh = open('small.txt', 'r')
contents = fh.read()  # reads the whole file in a single string
fh.close()
print(contents)


fh = open('small.txt', 'r')
contents = fh.readlines()  # reads the file in a list
fh.seek(10)  # move the cursor to the 10th character in the file
contents2 = fh.read()  # reads the file from the 10th character onwards
fh.close()
print('1:', contents)
print('2:', contents2)


# Load file contents to memory one line at a time
# This is the preferred way when reading very large files
fh = open('alice.txt', 'r')
for line in fh:
    # manipulate file content
    print(line.lower().strip())
