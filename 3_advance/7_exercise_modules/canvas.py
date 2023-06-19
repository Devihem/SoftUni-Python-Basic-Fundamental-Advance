from tkinter import Tk, Canvas


def create_root():
    root = Tk()

    # window name
    root.title('GUI Shop')

    # windows size
    root.geometry('700x600')

    # block windows resize - 1 False - block  H resize, 2 False - block W resize
    root.resizable(False, False)

    return root


# invisible layer/frame over the created window  ( we attach every element on the canvas )
def create_frame():
    frame = Canvas(root, width=700, height=700)
    frame.grid(row=0, column=0)
    return frame


root = create_root()
frame = create_frame()
