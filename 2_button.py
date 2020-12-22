from tkinter import * 

root = Tk() 
root.title("Nouu GUI")
# root.geometry("640x480+300+100")
# root.resizable(False, False)

button1 = Button(root, text="버튼1") # 버튼 생성 
button1.pack()

button2 = Button(root, padx=5, pady=10, text="버튼2") # padx, pady는 상대적인 크기 (여백)
button2.pack()

button3 = Button(root, padx=10, pady=5, text="버튼2")
button3.pack()

button4 = Button(root, width=10, height=3, text="버튼4") # width, height는 고정크기 
button4.pack()

button5 = Button(root, fg="red", bg="yellow", text=5) # fg = 글자색, bg = 백그라운드 색
button5.pack()

photo = PhotoImage(file="img.png")
button6 = Button(root, image=photo)
button6.pack()

def btncmd() : 
    print("버튼이 동작되었습니다.")

button7 = Button(root, text="동작하는 버튼", command=btncmd) # command 인자의 할당 값은 함수로 해야하나?
button7.pack()

root.mainloop()