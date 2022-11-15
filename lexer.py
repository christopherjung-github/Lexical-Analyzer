import json
import keyword

op = "operator"
key = "keyword"
id = "identifier"
real = "real"
sep = "separator"

operators = ['<', '>', '+', '-', '=']
separator = ['(', ')', ';']

# def write_data(filename, input):
#     with open(filename, 'w') as f:
#         json.dump(input, f, separators='\n')

def lexer(filename):
    try:
        with open(filename, 'r') as f:
            display =   "token             lexeme   \n"
            display +=  "----------------  ---------\n"
            
            new = ""
            for line in f:
                for character in line:
                    if character != " ":
                        #check if character before other characters is operator
                        if character in operators and len(new) == 0:
                            display +=  f"{op:18}{character:9}\n"
                        #check if character before other characters is separator
                        elif character in separator and len(new) == 0:
                            display +=  f"{sep:18}{character:9}\n"
                        #check if character after other characters is separator
                        elif character in separator and len(new) != 0:
                            if new.isdecimal() or new.isdigit():
                                display +=  f"{real:18}{new:9}\n"
                                new = ""
                            elif new in key:
                                display +=  f"{key:18}{new:9}\n"
                                new = ""
                            else:
                                # display +=  f"{id:18}{new:9}\n"
                                try:
                                    float(new)
                                    display +=  f"{real:18}{new:9}\n"
                                    # new = ""
                                except ValueError:
                                    display +=  f"{id:18}{new:9}\n"
                                    # new = ""
                                new = ""
                            display +=  f"{sep:18}{character:9}\n"
                        else:
                            new += character
                    elif new != "" and new.isnumeric():
                        display +=  f"{real:18}{new:9}\n"
                        new = ""
                    elif new != "" and keyword.iskeyword(new):
                        display +=  f"{key:18}{new:9}\n"
                        new = ""
                    elif len(new) != 0:
                        display +=  f"{id:18}{new:9}\n"
                        new = ""
            output_file = open("output.txt", "a")
            output_file.write(display)
            output_file.close()
            f.close()
    except FileNotFoundError:
        return "{filename} not found"
    return display


print(lexer("input_scode.txt"))
# write_data("output.txt", input=l)