import sys
from PyQt5.QtWidgets import QApplication
from view import GUI
from controller import Controller
from  model import evaluateExpression

# Client code
def main():
    """Main function."""
    # Create an instance of QApplication
    pycalc = QApplication(sys.argv)
    # Show the calculator's GUI
    view = GUI()
    view.show()

	# Create instances of the model and the controller
    model = evaluateExpression
    Controller(model=model, view=view)

    # Execute the calculator's main loop
    sys.exit(pycalc.exec_())

if __name__ == '__main__':
    main()
def decimal_into_binary(decimal_1):  
    decimal = int(decimal_1)  
    print ("The given decimal number", decimal, "in Binary number is: ", bin(decimal))  
 
def decimal_into_octal(decimal_1):  
    decimal = int(decimal_1)  
    
    print ("The given decimal number", decimal, "in Octal number is: ", oct(decimal))  
  
def decimal_into_hexadecimal(decimal_1):  
    decimal = int(decimal_1)  
     
    print ("The given decimal number", decimal, " in Hexadecimal number is: ", hex(decimal))  
    decimal_1 = int (input (" Enter the Decimal Number: "))  
    decimal_into_binary(decimal_1)  
    decimal_into_octal(decimal_1)  
    decimal_into_hexadecimal(decimal_1)

