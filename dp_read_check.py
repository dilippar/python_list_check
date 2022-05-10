import sys
#usage python dp_read_check.py AWS
file1 = open('c:\\rd\\data\\aws.data.txt', 'r')

# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)
# Arguments passed
print("\nName of Python script:", sys.argv[0])
 
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")
print('Start...................')

arg1 = sys.argv[1]
print(arg1)
print('>>')
for lines in file1:
 if arg1 in lines:
  print (arg1 + ' exist at line> ' + lines)
print('<<')
print('Checked!')
