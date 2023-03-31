from setup import *

root = tkinter.Tk()
root.title("Q-Learn-1")

frm = tkinter.Frame(root)
tkinter.Button(frm, text="Quit", font=("Helvetica", 20), command=root.destroy).grid(column=9, row=0, rowspan=3)


def get_description(number, final_pass):
    text = "Pass no"
    if final_pass:
        return "  FINAL  "

    return text + str(number)


def draw(status, description, e):
    frm.grid()

    tkinter.Label(frm, text=description, font=("Helvetica", 20)).grid(column=0, row=0)
    tkinter.Label(frm, text="L-weight", font=("Helvetica", 20)).grid(column=0, row=1)
    tkinter.Label(frm, text="R-weight", font=("Helvetica", 20)).grid(column=0, row=2)
    tkinter.Label(frm, text="E="+str("{:.2f}".format(e)), font=("Helvetica", 20)).grid(column=8, row=1, rowspan=2)

    for i in range(6):
        if i == status:
            tkinter.Label(frm, text="☒", font=("Helvetica", 100)).grid(column=i+1, row=0)
            continue

        tkinter.Label(frm, text="☐", font=("Helvetica", 100)).grid(column=i+1, row=0)

        tkinter.Label(frm, text=str("{:.1e}".format(array[0][i])), font=("Helvetica", 20)).grid(column=i + 1, row=1)
        tkinter.Label(frm, text=str("{:.1e}".format(array[1][i])), font=("Helvetica", 20)).grid(column=i + 1, row=2)

    if status != 7:
        tkinter.Label(frm, text="☑", font=("Helvetica", 100)).grid(column=8, row=0)
    else:
        tkinter.Label(frm, text="☒", font=("Helvetica", 100)).grid(column=8, row=0)

    frm.update()
    time.sleep(0.10)
