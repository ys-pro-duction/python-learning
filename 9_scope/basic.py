CONSTANTS_NUM = 420
global_var = 100
global_var_two = 10
hi = 8520

def func_one():
    global_var = 50
    global global_var_two  # Now global_var_two can modify inside func
    global_var_two = 5
    print(f"func_one global_var {global_var}")


if True:
    global_var_three = 999  # can declair new var and access ouside if block

func_one()
print(f"global global_var {global_var}")
print(f"global global_var_two {global_var_two}")
print(f"global global_var_three {global_var_three}")
