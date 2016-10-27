import os.path
from  norm_error import Error

error_stack = []

abs_path_file = os.path.abspath('ft_strcpy.c')
abs_path_htemplate = os.path.abspath('header_template')

c_file 		= open(abs_path_file, 'r')
htemplate 	= open(abs_path_htemplate, 'r')


error_stack.append(Error("new type baby", 0, 1337))

print error_stack
print error_stack[0]
print error_stack[0].print_message()



c_lines = c_file.readlines()
htemplate_lines = htemplate.readlines()

'''
stream =  ""
for line in c_lines:
	stream += line

print stream
'''

c_file.close()
