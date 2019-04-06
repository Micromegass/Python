
#Import Module
import os
import tkinter as tk
import tkinter.messagebox as msg
import tkinter.filedialog as fd
import random
import datetime as dt


def get_route():
	#create window
	window = tk.Tk()
	#Hide principal window
	window.withdraw()
	filters = [('All archives', '.*'),
			             ('textfiles txt', '.txt'),
			            ('Pictures files', '.png'),
                        ('csv files', '.csv'),
                        ('Scripts Python py', '.py'),
                        ('Scripts Python pyw', '.pyw'),
                        ('Excel xlsx', '.xlsx'),
                        ('Excel xls', '.xls')]

	title = "Select file you want to destroy"
	full_path = os.path.dirname(os.path.realpath(__file__))

	answer_user = fd.askopenfilename(parent=window,
	                                       initialdir=full_path,
	                                       title=title,
	                                       filetypes=filters)

	# Overwrite archive if existent
	if os.path.exists(answer_user):
		#show warning
		warning = tk.Tk()
		warning.withdraw()
		message = "Are you sure you want to destroy this file? (Can't be undone!)"
		title = "Warning"
		warning_answer = msg.askokcancel(title,message)
		if warning_answer:
			#pass route to overwrite function
			overwrite(answer_user)
		else:
			print("Aborting...")
	else:
		return "This file doesn't exist"



def overwrite(route_archive, overwrites=27):

	start = dt.datetime.now()
	size_bites = os.path.getsize(route_archive)

	for i in range(overwrites):
		print("Overwriting ", (i + 1))
		a = open(route_archive, "wb")
		for item in range(size_bites):
			by = bytes([random.randint(0, 255)])
			a.write(by)
		a.close()
	
	end = dt.datetime.now()

	diff = end -start
	diff = str(diff)

	print("Operation succesful. Time needed: " + diff)



get_route()

