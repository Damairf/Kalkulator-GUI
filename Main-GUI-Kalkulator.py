from tkinter import *

def button_press(num):
    global hasil_text
    if hasil_text == "0" and num != ".":
        hasil_text = str(num)
    else:
        hasil_text = hasil_text + str(num)
    hasil_label.set(hasil_text)

def equals(event):
    global hasil_text
    try:
        total = str(eval(hasil_text))
        if len(total) > 13:
            hasil_label.set("{:E}".format(float(total)))
        else:
            hasil_label.set(total)
        hasil_text = total+""
    except ZeroDivisionError:
        hasil_label.set("Error")
        hasil_text = ""
    except SyntaxError:
        hasil_label.set("Error")
        hasil_text = ""

def clear(event):
    global hasil_text
    hasil_label.set("")
    hasil_text = ""

def backspace(event):
    global hasil_text
    hasil_text = hasil_text[:-1]
    hasil_label.set(hasil_text)

window = Tk()
window.title("Kalkulator")
window.geometry("280x470")
window.resizable(False, False)
window.config(background="#272727")

icon = PhotoImage(file='kalkulator.png')
window.iconphoto(True, icon)

hasil_text = ""
hasil_label = StringVar()

label = Label(window, textvariable=hasil_label,font=("consolas", 20), bg="white", width=16, height=2, anchor='e', padx=5, pady=5)
label.pack(pady=10)

frame = Frame(window, bg="#272727")
frame.pack()

# Button angka
button7 = Button(frame, text="7", font=20, width=4, height=2, command=lambda: button_press(7))
button7.grid(row=0, column=0, padx=5, pady=5)
button8 = Button(frame, text="8", font=20, width=4, height=2, command=lambda: button_press(8))
button8.grid(row=0, column=1, padx=5, pady=5)
button9 = Button(frame, text="9", font=20, width=4, height=2, command=lambda: button_press(9))
button9.grid(row=0, column=2, padx=5, pady=5)
button4 = Button(frame, text="4", font=20, width=4, height=2, command=lambda: button_press(4))
button4.grid(row=1, column=0, padx=5, pady=5)
button5 = Button(frame, text="5", font=20, width=4, height=2, command=lambda: button_press(5))
button5.grid(row=1, column=1, padx=5, pady=5)
button6 = Button(frame, text="6", font=20, width=4, height=2, command=lambda: button_press(6))
button6.grid(row=1, column=2, padx=5, pady=5)
button1 = Button(frame, text="1", font=20, width=4, height=2, command=lambda: button_press(1))
button1.grid(row=2, column=0, padx=5, pady=5)
button2 = Button(frame, text="2", font=20, width=4, height=2, command=lambda: button_press(2))
button2.grid(row=2, column=1, padx=5, pady=5)
button3 = Button(frame, text="3", font=20, width=4, height=2, command=lambda: button_press(3))
button3.grid(row=2, column=2, padx=5, pady=5)
button0 = Button(frame, text="0", font=20, width=4, height=2, command=lambda: button_press(0))
button0.grid(row=3, column=1, padx=5, pady=5)

window.bind("1", lambda num: button_press("1"))
window.bind("2", lambda num: button_press("2"))
window.bind("3", lambda num: button_press("3"))
window.bind("4", lambda num: button_press("4"))
window.bind("5", lambda num: button_press("5"))
window.bind("6", lambda num: button_press("6"))
window.bind("7", lambda num: button_press("7"))
window.bind("8", lambda num: button_press("8"))
window.bind("9", lambda num: button_press("9"))
window.bind("0", lambda num: button_press("0"))

# Button operasi
button_clear = Button(frame, text="C", font=20, width=4, height=2, fg="red", command=lambda: clear("Delete"))
button_clear.grid(row=3, column=0, padx=5, pady=5)
button_titik = Button(frame, text=".", font=20, width=4, height=2, command=lambda: button_press("."))
button_titik.grid(row=3, column=2, padx=5, pady=5)
button_tambah = Button(frame, text="+", font=20, width=4, height=2, command=lambda: button_press("+"))
button_tambah.grid(row=3, column=3, padx=5, pady=5)
button_kurang = Button(frame, text="-", font=20, width=4, height=2, command=lambda: button_press("-"))
button_kurang.grid(row=2, column=3, padx=5, pady=5)
button_kali = Button(frame, text="x", font=20, width=4, height=2, command=lambda: button_press("*"))
button_kali.grid(row=1, column=3, padx=5, pady=5)
button_bagi = Button(frame, text="/", font=20, width=4, height=2, command=lambda: button_press("/"))
button_bagi.grid(row=0, column=3, padx=5, pady=5)
button_del = Button(frame, text="Back", font=20, width=10, height=2, bg="Orange", activebackground="Orange", command=lambda: backspace("BackSpace"))
button_del.grid(row=4, column=0, padx=5, pady=5, columnspan=2)
button_hasil = Button(frame, text="=", font=20, width=10, height=2, bg="Orange", activebackground="Orange", command=lambda: equals("Return"))
button_hasil.grid(row=4, column=2, columnspan=2, padx=5, pady=5)

window.bind("-", lambda num: button_press("-"))
window.bind(".", lambda num: button_press("."))
window.bind("/", lambda num: button_press("/"))
window.bind("*", lambda num: button_press("*"))
window.bind("+", lambda num: button_press("+"))
window.bind("<Delete>", clear)
window.bind("<BackSpace>", backspace)
window.bind("<Return>", equals)

window.mainloop()