import math
import numpy as np
import sympy as sym
from sympy import sin, cos
from numpy import pi
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt


'''Sine and Cosine functions were separated for the reason to avoid spelling mistakes and achieve much accurate results
Parameters of these functions below are the following: 
"val" - trigonometric function which is sin
"a" - left point of the limit
"b" - right point of the limit
"N" - Number of intervals
"n" - variable for more accurate plotting'''

def sine_func(val,a,b,N,n = 20):
	x = sym.Symbol('x')
	max_value_of_function = 0

	# Variable which keeps value from the entry field
	trig_val_sin = input_field_for_function.get()

	# These lines are defined for CALCULATIONS
	x_range = np.linspace(a, b, N+1)
	y_sin = np.sin(x_range)

	# These lines are defined for PLOTTING AREA WITHIN THE RANGE
	X_sin_graph = np.linspace(a,b,n*N+1)
	Y = np.sin(X_sin_graph)

	# These lines allow us to EXPAND THE GRAPH from (-a*0.5 to b+10)
	x_general_plot = np.linspace(-a*0.5, b+10, 1000)
	y_gen_pl = np.sin(x_general_plot)	

	# We take second derivative for Error Boundary calculation
	second_dx = str(sym.diff(sym.diff(eval(trig_val_sin), x), x))

	# We find maximum value of function for Error Formula
	for max_x in range(a,b+1):
		if max_x == 0:
			continue

		# We subsbtitude every number from the range of limit
		sub_root = math.ceil(eval(str(second_dx.replace ('x', str(max_x)))))

		if sub_root > max_value_of_function:
			max_value_of_function = sub_root


		# Here the Error Function is
		e_T_f = (np.sin(max_value_of_function) * (b-a)**3) / (12*(N**2))

	
	# Here we calculate area of every single trapezoid	
	y = np.sin(x_range)
	y_right = y[1:]
	y_left = y[:-1]
	dx = (b - a)/N
	area_dx = ((y_left + y_right)/2) * dx


	# After getting all variables we estimate approximate area
	aprox_area = (dx/2) * np.sum(np.abs(y_right) + np.abs(y_left))


	# By integration we get exactly area between "a" and "b"
	exact_area = sym.integrate(eval(trig_val_sin), x)


	# The loop below draw trapezoids according to values of function
	for i in range(N):
		xs = [x_range[i], x_range[i], x_range[i+1] ,x_range[i+1]]
		ys = [0, np.sin(x_range[i]), np.sin(x_range[i+1]) ,0]
		plt.fill(xs, ys, edgecolor='b', alpha=0.1)


	# We plot exactly part from from "a" to "b"
	plt.plot(X_sin_graph, Y)
	plt.axhline (color = 'm')
	plt.axvline (color = 'g')


	# Here we plot general graph and put exact part onto it
	plt.plot (x_general_plot, y_gen_pl)
	plt.axhline (color = 'm')
	plt.axvline (color = 'g')
	plt.xlabel('Approximate area = {}'.format(aprox_area))
	plt.show()

	# We show result of all our calculation below the button
	result_label.config(text = 'Aproximate area: ' + str(aprox_area) + '\n' + 'Exact Area: ' + str(exact_area) + '\n' + 'Error Boundary at: ' + str(e_T_f))
	
	return np.abs(aprox_area - exact_area), e_T_f


def cosine_func(val,a,b,N,n = 20):

	x = sym.Symbol('x')
	max_value_of_function = 0
	trig_val_sin = input_field_for_function.get()

	# Look at the sine_func comments as they are absolutely identical
	x_range = np.linspace(a, b, N+1)
	y_sin = np.cos(x_range)

	# Look at the sine_func comments as they are absolutely identical
	X_sin_graph = np.linspace(a,b,n*N+1)
	Y = np.cos(X_sin_graph)

	# Look at the sine_func comments as they are absolutely identical
	x_general_plot = np.linspace(-a*0.5, b+10, 1000)
	y_gen_pl = np.cos(x_general_plot)	

	# Look at the sine_func comments as they are absolutely identical
	second_dx = str(sym.diff(sym.diff(eval(trig_val_sin), x), x))

	# Look at the sine_func comments as they are absolutely identical
	for max_x in range(a,b+1):
		if max_x == 0:
			continue

		# Look at the sine_func comments as they are absolutely identical
		sub_root = math.ceil(eval(str(second_dx.replace ('x', str(max_x)))))

		if sub_root > max_value_of_function:
			max_value_of_function = sub_root


		# Look at the sine_func comments as they are absolutely identical
		e_T_f = (np.cos(max_value_of_function) * (b-a)**3) / (12*(N**2))
		
	
	# Look at the sine_func comments as they are absolutely identical	
	y = np.cos(x_range)
	y_right = y[1:]
	y_left = y[:-1]
	dx = (b - a)/N
	area_dx = ((y_left + y_right)/2) * dx

	aprox_area = (dx/2) * np.sum(np.abs(y_right) + np.abs(y_left))
	exact_area = sym.integrate(eval(trig_val_sin), x)

	# Look at the sine_func comments as they are absolutely identical
	for i in range(N):
		xs = [x_range[i], x_range[i], x_range[i+1] ,x_range[i+1]]
		ys = [0, np.cos(x_range[i]), np.cos(x_range[i+1]) ,0]
		plt.fill(xs, ys, edgecolor='b', alpha=0.1)

	# Look at the sine_func comments as they are absolutely identical
	plt.plot(X_sin_graph, Y)
	plt.axhline (color = 'm')
	plt.axvline (color = 'g')

	# Look at the sine_func comments as they are absolutely identical
	plt.plot (x_general_plot, y_gen_pl)
	plt.axhline (color = 'm')
	plt.axvline (color = 'g')
	plt.xlabel('Approximate area = {}'.format(aprox_area))
	plt.show()

	result_label.config(text = 'Aproximate area: ' + str(aprox_area) + '\n' + 'Exact Area: ' + str(exact_area) + '\n' + 'Error Boundary at: ' + str(e_T_f))
	return np.abs(aprox_area - exact_area), e_T_f


def trapezoidal_graph(a,b,N,n = 20):

	# We just try to avoid empty value for the function
	if input_field_for_function.get() != '':
		
		expression = input_field_for_function.get()
		x = sym.Symbol('x')
		second_dx = str(sym.diff(sym.diff(eval(expression))))
		max_value_of_function = 0

		if 'x' not in expression:
			x_function = np.linspace(a,b,N+1)
			y = [eval(expression) for i2 in range(len(x_function))]

			plt.plot (x_function, y)
			plt.axhline (color = 'm')
			plt.axvline (color = 'g')
			for i in range(N):
				xs = [x_function[i], x_function[i], x_function[i+1] ,x_function[i+1]]
				ys = [0, y[i], y[i+1] ,0]
				plt.fill(xs, ys, edgecolor='b', alpha=0.1)

			aprox_area = exact_area = (b-a) * eval(expression)
			e_T_f = 0

		else:
			# The "f" function calculates all variables if there are any
			f = lambda x : eval(expression)

			# Look at the sine_func comments as they are absolutely identical
			x_function = np.linspace(a,b,N+1)
			y = f(x_function)
			
			# Look at the sine_func comments as they are absolutely identical 
			X_graph = np.linspace(a,b,n*N+1)
			Y = f(X_graph)

			# Look at the sine_func comments as they are absolutely identical
			x_general_plot = np.linspace(-1,b+10,1000)
			y_gen_pl = f(x_general_plot)

		
			plt.plot (X_graph, Y)
			plt.axhline (color = 'black')
			plt.axvline (color = 'black')
			
			
			plt.plot (x_general_plot, y_gen_pl)
			plt.axhline (color = 'm')
			plt.axvline (color = 'g')

			# Look at the sine_func comments as they are absolutely identical
			for i in range(N):
				xs = [x_function[i], x_function[i], x_function[i+1] ,x_function[i+1]]
				ys = [0, f(x_function[i]), f(x_function[i+1]) ,0]
				plt.fill(xs, ys, edgecolor='b', alpha=0.1)


			# Look at the sine_func comments as they are absolutely identical
			for max_x in range(a,b+1):
				if expression == '1/x':
					if max_x == 0:
						continue

				sub_root = math.ceil(eval(str(second_dx.replace ('x', str(max_x)))))

				if sub_root > max_value_of_function:
					max_value_of_function = sub_root

			# Look at the sine_func comments as they are absolutely identical
			e_T_f = (f(max_value_of_function) * (b-a)**3) / (12*(N**2))

			# Look at the sine_func comments as they are absolutely identical
			y = f(x_function)
			y_right = y[1:]
			y_left = y[:-1]
			dx = (b - a)/N
			area_dx = ((y_left + y_right)/2) * dx

			aprox_area = (dx/2) * np.sum(y_right + y_left)
			exact_area = sym.integrate(f(x), (x, a, b))

			
		
		plt.xlabel('X')
		plt.ylabel('Y')
		plt.title('Trapezoid Rule, N = {}'.format(N))
		plt.xlabel('Approximate area = {}'.format(aprox_area))
	
	# We show the error window in case of empty field of function	
	else:
		messagebox.showerror('Function Error', 'Set a function!')

	result_label.config(text = 'Aproximate area: ' + str(aprox_area) + '\n' + 'Exact Area: ' + str(exact_area) + '\n' + 'Error Boundary at: ' + str(e_T_f))
	return np.abs(aprox_area - exact_area), e_T_f


def init_func():

	integral_button.config(text = 'Show the Graph')

	# These line storage all values from all Entries
	a = input_field_for_a.get()
	b = input_field_for_b.get()
	N = int(input_field_for_N.get())
	accur_pow = input_field_for_accuracy.get()

	if a == '' or b == '' or N == '':
		messagebox.showerror('Empty Field', 'Please set a value')

	else:
		trig_val = input_field_for_function.get()
		a = int(input_field_for_a.get())
		b = int(input_field_for_b.get())

	if accur_pow == '':
		accur_pow = 0

	else:
		accur_pow = float(input_field_for_accuracy.get().strip(' '))

	if 'sin' in trig_val:
		sine_func(trig_val, a, b, N)

	if 'cos' in trig_val:
		cosine_func(trig_val, a, b, N)


	# This block will work only if accuracy field has any number
	else:
		plt.show()
		try:
			while True:
				approx, error_bound = trapezoidal_graph(a,b,N)

				if approx < 10**(-accur_pow):	
					break
				N += 2
		except AttributeError:
			pass

	accuracy_label.config(text = 'Accuracy has been achieved at N = ' + str(N))


# We just connected "Enter" button
def keyboard_connection(key):
	keysymbol = key.keysym

	if keysymbol == 'Return':
		init_func()	

# All Tkinter stuff
main_app = Tk()
main_app.geometry('450x550')
main_app.title('Approximate area by trapezoids')
main_app.bind("<Key>", keyboard_connection)

header_title = Label(main_app, text = '* Input a function f(x):')
header_title.config(font = ('Times', 12 , 'bold'))
header_title.pack(pady = 10)

input_field_for_function = Entry(main_app, width = 15, font = ('Monster-eng', 9,), takefocus = '')
input_field_for_function.pack()

a_input_label = Label(main_app, text = '* Input \'a\' value: ')
a_input_label.config(font = ('Times', 12 , 'bold'))
a_input_label.pack(pady = 2)

input_field_for_a = Entry(main_app, width = 3, font = ('Monster-eng', 9,), takefocus = '')
input_field_for_a.pack()

b_input_label = Label(main_app, text = '* Input \'b\' value: ')
b_input_label.config(font = ('Times', 12 , 'bold'))
b_input_label.pack(pady = 2)

input_field_for_b = Entry(main_app, width = 3, font = ('Monster-eng', 9,), takefocus = '')
input_field_for_b.pack()

n_input_label = Label(main_app, text = '* Input \'N\' value: ')
n_input_label.config(font = ('Times', 12 , 'bold'))
n_input_label.pack(pady = 2)

input_field_for_N = Entry(main_app, width = 3, font = ('Monster-eng', 9,), takefocus = '')
input_field_for_N.pack()

accuracy_input_label = Label(main_app, text = 'How close to exact area you want to be \"10 ^ -(x)\":\n(Optional) ')
accuracy_input_label.config(font = ('Times', 12 , 'bold'))
accuracy_input_label.pack(pady = 2)

input_field_for_accuracy = Entry(main_app, width = 3, font = ('Monster-eng', 9,), takefocus = '')
input_field_for_accuracy.pack()

integral_button = Button(main_app, text = 'Estimate Area', command = init_func)
integral_button.config(font = ('Academy-Bold [Edited by me] Bold', 10, 'bold'), fg = '#22005E', bg = '#83C159', takefocus = '')
integral_button.pack(pady = 10)


result_label = Label(main_app, text = '')
result_label.config(font = ('Times', 12 , 'bold'))
result_label.pack()

accuracy_label = Label(main_app, text = '')
accuracy_label.config(font = ('Times', 12 , 'bold'))
accuracy_label.pack()

main_app.mainloop()