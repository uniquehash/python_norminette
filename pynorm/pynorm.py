import os.path

abs_path_file = os.path.abspath('ft_strcpy.c')
abs_path_htemplate = os.path.abspath('ft_strcpy.c')


file = open(abs_path, 'r')

lines = file.readlines()
header = lines[0:11]

stream = ""

header_temp[0] = "/* ************************************************************************** */"




for line in header:
	stream += line

print stream


file.close()
