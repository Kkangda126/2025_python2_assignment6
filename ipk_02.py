import tkinter as tk

class Pet:
    def speak(self):
        return "..."

class Dog(Pet):
    def speak(self):
        return "멍멍!"

class Cat(Pet):
    def speak(self):
        return "야옹!"
    
class Person:
    def __init__(self, name, Pet=None):
        self.name = name
        self.Pet = Pet

root = tk.Tk()
root.title("문제2")
root.geometry("400x200")

Label1 = tk.Label(root, text="반려동물을 선택하고 '말하기'를 누르세요.", font=("맑은 고딕", 12)).pack(pady=10)

person = Person("홍길동")

def select_Dog():
    person.Pet = Dog()
    result.set("강아지를 선택했습니다.")

def select_Cat():
    person.Pet = Cat()
    result.set("고양이를 선택했습니다.")

def speak():
    result.set(f"{person.name}의 반려동물 → {person.Pet.speak()}")

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Button(frame, text="강아지 선택", command=select_Dog).pack(side="left", padx=8)
tk.Button(frame, text="고양이 선택", command=select_Cat).pack(side="left", padx=8)
tk.Button(root, text="말하기", command=speak).pack(pady=10)

result = tk.StringVar(value="")
label2 = tk.Label(root, textvariable=result, font=("맑은 고딕", 12), fg="blue")
label2.pack(pady=10)

root.mainloop()
