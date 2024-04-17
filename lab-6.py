import tkinter as tk
from rx.subject import BehaviorSubject
from rx.operators import map

def update_ui(value):
    print("Слайдердың мәні өзгерді:", value)

root = tk.Tk()
root.title("FRP - қолданылатын слайдер")

slider_value_subject = BehaviorSubject(0)

def on_slider_change(event):
    value = slider.get()
    slider_value_subject.on_next(value)

CONSTANT=10

slider_value_subject.pipe(
    map(lambda value: value + CONSTANT)
).subscribe(update_ui)

slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=on_slider_change)
slider.pack(padx=10, pady=10)

root.mainloop()