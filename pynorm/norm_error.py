# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    norm_error.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: crenfrow <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2016/10/26 23:08:43 by crenfrow          #+#    #+#              #
#    Updated: 2016/10/27 00:20:49 by crenfrow         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Error(object):
	def __init__(self, e_type, e_id, line):
		self.e_type = e_type
		self.e_id	= e_id
		self.line	= line

	def print_message(self):
		message = "line: {0} -> {1} error: ".format(self.line, self.e_type)
		message += self.get_message()
		print "dafadf"	
		print message
	
	def get_message(self):
		error_messages = {
			'header': [
				"the header is not at the top of the file",
				"new message"
			],
			'new type baby': [
				"ayyyy"
			]
		}
		message_array = error_messages['header']

		return message_array[self.e_id]
