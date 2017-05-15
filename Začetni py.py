
import tkinter as tk

okno=tk.Tk()
okno.title('Kalkulator')

stolpec1=tk.Frame(okno)
stolpec1.pack()
tk.Button(stolpec1, text='{: ^5}'.format('7')).grid(row=1,column=1)
tk.Button(stolpec1, text='{: ^5}'.format('4')).grid(row=2,column=1)
tk.Button(stolpec1, text='{: ^5}'.format('1')).grid(row=3,column=1)
tk.Button(stolpec1, text='{: ^5}'.format('0')).grid(row=4,column=1)

stolpec2=tk.Frame(okno)
stolpec2.pack()
tk.Button(stolpec2, text='{: ^5}'.format('8')).grid(row=1,column=2)
tk.Button(stolpec2, text='{: ^5}'.format('5')).grid(row=2,column=2)
tk.Button(stolpec2, text='{: ^5}'.format('2')).grid(row=3,column=2)
tk.Button(stolpec2, text='{: ^6}'.format('.')).grid(row=4,column=2)

gumb9 = tk.Button(okno, text='{: ^5}'.format('9'))
gumb9.grid(row=1,column=3)
gumb6 = tk.Button(okno, text='{: ^5}'.format('6'))
gumb6.grid(row=2,column=3)
gumb3 = tk.Button(okno, text='{: ^5}'.format('3'))
gumb3.grid(row=3,column=3)


gumb_neg = tk.Button(okno, text='{: ^5}'.format('(-)'))
gumb_neg.grid(row=4,column=3)

gumbC = tk.Button(okno, text='{: ^14}'.format('C'))
gumbC.grid(row=1,column=4,columnspan=2)
gumb_mnozenje = tk.Button(okno, text='{: ^5}'.format('*'))
gumb_mnozenje.grid(row=2,column=4)
gumb_plus = tk.Button(okno, text='{: ^5}'.format('+'))
gumb_plus.grid(row=3,column=4)
gumb_enako = tk.Button(okno, text='{: ^14}'.format('='))
gumb_enako.grid(row=4,column=4,columnspan=2)


gumb_mnozenje = tk.Button(okno, text='{: ^5}'.format('/'))
gumb_mnozenje.grid(row=2,column=5)
gumb_plus = tk.Button(okno, text='{: ^5}'.format('-'))
gumb_plus.grid(row=3,column=5)

zgoraj=tk.Frame(okno)
zgoraj.pack(side=Top)
tk.Entry(zgoraj).grid(row=0)

okno.mainloop()
