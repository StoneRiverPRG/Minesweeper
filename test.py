if not (False and False):
    print("False and False")

if not (True and True):
    print("True and True")

if not (False and True):
    print("False and True")

if not (True and False):
    print("True and False")

print(False and False)

def return_int():
    return

print(return_int())
# None

def coordinate_to_rowcol(coord):
    # *check legal position
    if not len(coord) == 2:
        return
    x, y = coord
    if not ((0 <= x < 16) and (0 <= y < 32)):
        # ! if list index is out of range.
        return

    return (y, x)

tp = (20, 20)
print(coordinate_to_rowcol(tp))

number_cell = list("12345678")
print(number_cell)

d = {}
d["?"] = 1
print(d)
print(d.get("?"))
if not d.get("?") == None:
    d["?"] += 1
print(d)

if not None == int("1"):
    print("Yes")