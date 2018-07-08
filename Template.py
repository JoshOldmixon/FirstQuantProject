from Tkinter import *
from sklearn import tree

words1 = 1

est1 = 1

words2 = 1

est2 = 1

words3 = 1

est3 = 1

def click():
	entered_text=textentry.get()
	output.delete(0.0, END)
	if words1 == 1:
		word1 = "Close: "
	else:
		word1 = "ERROR!"
	output.insert(END, word1)

	if est1 == 1:
		close = clf1.predict([[entered_text]])
	else:
		close = "ERROR!"
	output.insert(END, close)

	if words2 == 1:
		word2 = "   High: "
	else:
		word2 = "ERROR!"
	output.insert(END, word2)

	if est2 == 1:
		high = clf2.predict([[entered_text]])
	else:
		high = "ERROR!"
	output.insert(END, high)

	if words3 == 1:
		word3 = "   Low: "
	else:
		word3 = "ERROR!"
	output.insert(END, word3)

	if est3 == 1:
		low = clf3.predict([[entered_text]])
	else:
		low = "ERROR!"
	output.insert(END, low)

window = Tk()
window.title("The STAC App")
window.configure(width=600, height=700, bg="blue")

Label (window, text="Stock: CHANGE THIS", bg="blue", fg="white", font="plump 44 bold") .grid(row=1, column=0, sticky=W)
Label (window, text="Enter Today's Opening Price:", bg="blue", fg="white", font="plump 20 bold") .grid(row=3, column=0, sticky=W)

textentry = Entry(window, width=30, bg="white")
textentry.grid(row=4, column=0, sticky=W)

Button(window, text="Submit", command=click, font="plump 18") .grid(row=4, column=0, sticky=E)

Label (window, text="Estimates:", bg="blue", fg="white", font="plump 20 bold") .grid(row=6, column=0, sticky=W)

output = Text(window, width=60, height=3, bg="white")
output.grid (row=7, column=0, columnspan=2, sticky=W)

clf1 = tree.DecisionTreeClassifier()

O = []

C = []

clf1 = clf1.fit(O, C)

clf2 = tree.DecisionTreeClassifier()

H = []

clf2 = clf2.fit(O, H)

clf3 = tree.DecisionTreeClassifier()

L = []

clf3 = clf3.fit(O, L)

window.mainloop()