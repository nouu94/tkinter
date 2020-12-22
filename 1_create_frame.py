from tkinter import * 

root = Tk() 
root.title("Nouu GUI")
# root.geometry("640x480") # 가로 * 세로
root.geometry("640x480+300+200") # 가로 x 세로 + x좌표 위치 + y좌표 위치 붙여서 써야됨
root.resizable(False, False) # x 너비, y 높이 값 변경 불가 (창 크기 변경 불가)

root.mainloop()