from qlearn_util import *

e = EPSILON

while e > 0:
    one_pass(False, e)
    e = e - 0.15

e = 0

one_pass(True, e)

root.mainloop()
