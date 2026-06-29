private class privateClass:
    def __init__(self):
        self.__private_attribute = "I am private"

    def __private_method(self):
        return "This is a private method"

    def public_method(self):
        return self.__private_method()

public class    PublicClass:
    def __init__(self):
        self.public_attribute = "I am public"

    def public_method(self):
        return "This is a public method"
    

def unittest_function():
    private_instance = privateClass()
    public_instance = PublicClass()
    
    # Accessing public method of private class
    private_output = private_instance.public_method()
    print(private_output)

    # Accessing public method of public class
    public_output = public_instance.public_method()
    print(public_output)Yno = np.array(C @ Xno.T).T
for yi in range(len(Yno[0])):                   