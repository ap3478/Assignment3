class Operations:
   

    @staticmethod
    def addition(a: float, b: float) -> float:
        
        return a + b  # This performs the addition of the two numbers and returns the result.

    @staticmethod
    def subtraction(a: float, b: float) -> float:
      
        return a - b  # This subtracts the second number (b) from the first number (a) and returns the result.

    @staticmethod
    def multiplication(a: float, b: float) -> float:
       
        return a * b  # This multiplies the two numbers and returns the result.

    @staticmethod
    def division(a: float, b: float) -> float:
        
        if b == 0:
            # This part checks if 'b' is zero. If it is, we raise an error and stop the method.
            raise ValueError("Division by zero is not allowed.")  # This sends an error message when someone tries to divide by zero.
        return a / b  # If 'b' is not zero, we divide the first number (a) by the second number (b) and return the result.