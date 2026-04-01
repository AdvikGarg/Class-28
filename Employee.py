class Employee:
    
    def __init__(self):
        print("Employee Created.")
        
    def __del__(self):
        print("Destructor Called.")
    
def createobj():
    print("Making Object")
    obj=Employee()
    print("Function End")
    return obj

print('Calling Create Object function...')
createobj()
print('Program end')       