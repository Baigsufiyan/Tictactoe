def play():
	menu = Tk()
	menu.geometry("250x250")
	menu.title("Tic Tac Toe")
	wpc = partial(withpc, menu)
	wpl = partial(withplayer, menu)

	head = Button(menu, text="---Welcome to tic-tac-toe---",
				activeforeground='red',
				activebackground="yellow", bg="red",
				fg="yellow", width=500, font='summer', bd=5)

	B1 = Button(menu, text="Single Player", command=wpc,
				activeforeground='red',
				activebackground="yellow", bg="red",
				fg="yellow", width=500, font='summer', bd=5)

	B2 = Button(menu, text="Multi Player", command=wpl, activeforeground='red',
				activebackground="yellow", bg="red", fg="yellow",
				width=500, font='summer', bd=5)

	B3 = Button(menu, text="Exit", command=menu.quit, activeforeground='red',
				activebackground="yellow", bg="red", fg="yellow",
				width=500, font='summer', bd=5)
	head.pack(side='top')
	B1.pack(side='top')
	B2.pack(side='top')
	B3.pack(side='top')
	menu.mainloop()