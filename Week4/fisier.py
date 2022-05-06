# file = open('data.txt', 'a')
# file.write('Hello1')
# file.close()
#
# file = open('data2.txt', 'w')
# try:
#     file.write('Hello')
# finally:
#     file.close()

# with open('data.txt', 'w') as file:
#     file.write('Curs Python\n')
#     file.write('Curs Python2\n')

with open('data.txt', 'r') as file:
    for line in file.readlines():
        print(line)
