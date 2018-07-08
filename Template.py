from Tkinter import *
from sklearn import tree

def click():
	entered_text=textentry.get()
	output.delete(0.0, END)
	word1 = "Close: "
	output.insert(END, word1)
	close = clf1.predict([[entered_text]])
	output.insert(END, close)
	word2 = "   High: "
	output.insert(END, word2)
	high = clf2.predict([[entered_text]])
	output.insert(END, high)
	word3 = "   Low: "
	output.insert(END, word3)
	low = clf3.predict([[entered_text]])
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
