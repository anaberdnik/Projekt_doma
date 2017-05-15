import tkinter as tk

okno=tk.Tk()
gumb7 = tk.Button(okno, text='{: ^5}'.format('7'))
gumb7.grid(row=1,column=1)
gumb4 = tk.Button(okno, text='{: ^5}'.format('4'))
gumb4.grid(row=2,column=1)
gumb1 = tk.Button(okno, text='{: ^5}'.format('1'))
gumb1.grid(row=3,column=1)

gumb8 = tk.Button(okno, text='{: ^5}'.format('8'))
gumb8.grid(row=1,column=2)
gumb5 = tk.Button(okno, text='{: ^5}'.format('5'))
gumb5.grid(row=2,column=2)
gumb2 = tk.Button(okno, text='{: ^5}'.format('2'))
gumb2.grid(row=3,column=2)

gumb9 = tk.Button(okno, text='{: ^5}'.format('9'))
gumb9.grid(row=1,column=3)
gumb6 = tk.Button(okno, text='{: ^5}'.format('6'))
gumb6.grid(row=2,column=3)
gumb3 = tk.Button(okno, text='{: ^5}'.format('3'))
gumb3.grid(row=3,column=3)

gumb0 = tk.Button(okno, text='{: ^5}'.format('0'))
gumb0.grid(row=4,column=1)
gumb_pika = tk.Button(okno, text='{: ^5}'.format('.'))
gumb_pika.grid(row=4,column=2)
gumb_neg = tk.Button(okno, text='{: ^5}'.format('(-)'))
gumb_neg.grid(row=4,column=3)

gumbC = tk.Button(okno, text='{: ^5}'.format('C'))
gumbC.grid(row=1,column=4)
gumb_mnozenje = tk.Button(okno, text='{: ^5}'.format('*'))
gumb_mnozenje.grid(row=2,column=4)
gumb_plus = tk.Button(okno, text='{: ^5}'.format('+'))
gumb_plus.grid(row=3,column=4)
gumb_enako = tk.Button(okno, text='{: ^5}'.format('='))
gumb_enako.grid(row=4,column=4)


gumb_mnozenje = tk.Button(okno, text='{: ^5}'.format('/'))
gumb_mnozenje.grid(row=2,column=5)
gumb_plus = tk.Button(okno, text='{: ^5}'.format('-'))
gumb_plus.grid(row=3,column=5)

vhod=tk.Entry(okno)
vhod.grid(row=0)


    
