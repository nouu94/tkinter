from tkinter import * 

root = Tk() 
root.title("Nouu GUI")
# root.geometry("640x480") # 가로 * 세로
root.geometry("640x480+300+200") # 가로 x 세로 + x좌표 위치 + y좌표 위치 붙여서 써야됨

text = Text(root, width=30, height=5)
text.pack()
text.insert(END, "글자를 입력하세요")

e = Entry(root, width=30) # 로그인 id나 패스워드를 쓸 때 사용함
e.pack()
e.insert(END, "한 줄만 입력하세요")

def buttoncmd() : 
    # 내용 출력
    print(text.get("1.0", END)) # 1 : 첫번째 라인, 0 : 0번째 COLUMN 위치
    print(e.get())

    # 내용 삭제
    text.delete("1.0", END)
    e.delete(0, END)

button = Button(root, text="클릭", command=buttoncmd)
button.pack()


root.mainloop()