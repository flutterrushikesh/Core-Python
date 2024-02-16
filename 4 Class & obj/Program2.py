#Classes and object

class employee:
    name="Kanha"
    empid=22
    sal=1.5

    def Work():
        print("Frontend dev")

obj1=employee()
obj1.Work()

# Type error: employee takes 0 positional arguments and 1 is given
# in class self parameter is required in class method