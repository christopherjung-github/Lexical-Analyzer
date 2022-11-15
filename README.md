# Lexical-Analyzer

## Project Objective
1. Write a python program using:
    1. modules
    2. json library
    3. loops
    4. file input/output

## Program Instruction
1. Run the program using the command below and repeat the steps above until you are satisfied your program output meets the above requirements.

    ```
    python3 -m lexer
    ```
    
    When the program has successfully compiled the output of the program should be displayed on both terminal and the following file:
    ```
    output.txt

    input:
        input_scode.txt

    output:
        token             lexeme   
        ----------------  ---------
        keyword           while    
        separator         (        
        identifier        s        
        operator          <        
        identifier        upper    
        separator         )        
        identifier        t        
        operator          =        
        real              33.00    
        separator         ;        
    ```

1. All the following files should be contain within the executable project folder for the Lexical Analyzer assignment:
    ```
    lexer.py
    output.txt
    input_scode.txt
    ```