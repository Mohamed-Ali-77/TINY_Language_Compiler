import sys
import os
from io import StringIO

class Scanner():
    # constructor
    def __init__(self, file_name=""):
        self.file_name = file_name
        text_file = open(self.file_name, "r")
        tiny_code = text_file.read()
        tiny_code.encode(encoding="utf-8")
        tiny_code = tiny_code.translate(str.maketrans({"-":  r"\-",
                                                       "]":  r"\]",
                                                       "\\": r"\\",
                                                       "^":  r"\^",
                                                       "$":  r"\$",
                                                       "*":  r"\*",
                                                       ".":  r"\.",
                                                       ":":  r"\:"}))
        self.tiny_code = tiny_code
        self.tokens_types = []
        self.tokens_values = []

    @staticmethod
    def remove_comments(self):
        for i in range(len(self.tiny_code)):
            if i < len(self.tiny_code):
                if self.tiny_code[i] == '{' :
                    j = i
                    while self.tiny_code[j] != '}' and j < len(self.tiny_code):
                        j= j+1
                    self.tiny_code = self.tiny_code[:i] + self.tiny_code[j+1:]
        return
    
    # method that generate output file of tokens
    def generate_tokens(self): 
        Scanner.Scan(self) # call scan method
        Scanner_out = "" # local variable to store output
        self.tokens_values = [e for e in self.tokens_values if e not in ["\n (ERROR)", "\\ (ERROR)","\n","\\"]] # remove error tokens
        self.tokens_types = [e for e in self.tokens_types if e not in ("\n (ERROR)", "\\ (ERROR)")] # remove error tokens
        for i in range(len(self.tokens_values)): # loop over tokens_types list
            Scanner_out += "{},{}\n".format(self.tokens_values[i],self.tokens_types[i]) # append to output
        f = open("output_tokens/tokens_"+ str(os.path.basename(self.file_name)), "w+") # open file to write
        f.write(Scanner_out) # write output to file
        f.close()   # close file
    
    # method that generate output tokens For UI
    def generate_tokens_UI(self):
        Scanner.Scan(self) # call scan method
        Scanner_out = "" # local variable to store output
        error_line = None
        self.tokens_values = [e for e in self.tokens_values if e not in ["\n (ERROR)", "\\ (ERROR)","\n","\\"]]
        self.tokens_types = [e for e in self.tokens_types if e not in ("\n (ERROR)", "\\ (ERROR)")]
        for i in range(len(self.tokens_values)): # loop over tokens_types list
            Scanner_out += "{},{}\n".format(self.tokens_values[i],self.tokens_types[i]) # append to output
            if self.tokens_types[i].find("ERROR") != -1:
                error_line = i 
        if error_line == None:
            return Scanner_out , None
        return Scanner_out, error_line # return output

    def Scan(self): # method that scan the input file
        #remove comments before start scanning
        Scanner.remove_comments(self)   # call remove_comments method

        special_sympols = [';','=','<','>','+','-','*','/','(',')'] # list of special symbols
        reversed_words = ['if','then','else','end','repeat','until','read','write'] # list of reversed words

        tokens_map = {";":"SEMICOLON","=":"EQUAL","<":"LESSTHAN",">":"GREATERTHAN","+":"PLUS","-":"MINUS","*":"MULT",
                        "/":"DIV","(":"OPENBRACKET",")":"CLOSEDBRACKET"} # map of special symbols
        
        #local list to store token_values on it
        tokens_list = [] 
        #loop over each line
        for tiny_in in StringIO(self.tiny_code): # loop over each line
            token_string = "" # local variable to store token_value
            state = "START" # local variable to store state
            i = 0 
            #iterate for every char
            while i < len(tiny_in): # iterate for every char
                if tiny_in[i] in special_sympols and state != "INASSIGN": # check if char is special symbol
                    if (token_string != ""): # check if token_string is not empty
                        tokens_list.append(token_string) # append token_string to tokens_list
                        token_string = "" # reset token_string
                    tokens_list.append(tiny_in[i]) # append char to tokens_list
                    state = "START" # reset state
                elif state == "START": # check if state is START
                    if tiny_in[i] == " ": # check if char is space
                        state = "START" # Stay in START state
                    elif tiny_in[i].isalpha(): # check if char is alphabet
                        token_string += tiny_in[i] # append char to token_string
                        state = "INID" # change state to INID
                    elif tiny_in[i].isdigit(): # check if char is digit
                        token_string += tiny_in[i] # append char to token_string
                        state = "INNUM" # change state to INNUM
                    elif tiny_in[i] == ":": # check if char is :
                        token_string += tiny_in[i] # append char to token_string
                        state = "INASSIGN" # change state to INASSIGN
                    else: # check if char is any other char
                        token_string += tiny_in[i] # append char to token_string
                        state = "DONE"  # change state to DONE
                elif state == "INID": # check if state is INID
                    if tiny_in[i].isalpha(): # check if char is alphabet
                        token_string += tiny_in[i] # append char to token_string
                        state = "INID" # Stay in INID state
                    else: # check if char is any other char
                        state = "DONE" # change state to DONE
                elif state == "INNUM": # check if state is INNUM
                    if tiny_in[i].isdigit(): # check if char is digit
                        token_string += tiny_in[i] # append char to token_string
                        state = "INNUM" # Stay in INNUM state
                    else: # check if char is any other char
                        state = "DONE" # change state to DONE
                elif state == "INASSIGN": # check if state is INASSIGN
                    if tiny_in[i] == "=": # check if char is =
                        token_string += tiny_in[i] # append char to token_string
                        state = "DONE" # change state to DONE
                    else: # check if char is any other char
                        state = "DONE" # change state to DONE
                elif state == "DONE": # check if state is DONE
                    tokens_list.append(token_string) # append token_string to tokens_list
                    token_string = "" # reset token_string
                    state = "START" # reset state
                    i -= 1 # decrement i
                i += 1 # increment i

            if(token_string != ""): # check if token_string is not empty
                tokens_list.append(token_string) # append token_string to tokens_list
                token_string = "" # reset token_string

        #local list to store token_types
        tokens_types = [] 
        for t in tokens_list: # loop over tokens_list
            if t in reversed_words: # check if token is reversed word
                tokens_types.append(t.upper()) # append token to tokens_types
            elif t in special_sympols: # check if token is special symbol
                tokens_types.append(tokens_map[t]) # append token to tokens_types
            elif t == ":=": # check if token is :=
                tokens_types.append('ASSIGN') # append token to tokens_types
            elif t.isdigit(): # check if token is digit
                tokens_types.append('NUMBER') # append token to tokens_types
            elif t.isalpha(): # check if token is alphabet
                tokens_types.append('IDENTIFIER') # append token to tokens_types
            else:
                tokens_types.append(t + " (ERROR)") # error token
        # Store the local variables into object attributes
        self.tokens_values = tokens_list    
        self.tokens_types = tokens_types

###############################################################################################################
# Main Function
if __name__ == "__main__":
    #if len(sys.argv) == 1:
        #print("Please enter right arguments\npython scanner.py FILE_NAME\nFILE_NAME that have TINY_CODE")
    #elif len(sys.argv) == 2:
    print("Please Enter the file name that have TINY_CODE and tokens file will be generated in the same directory:")
    file_name = "test_codes/input.txt"
    print("Tokens generated from {} file:".format(file_name))
    Scanner_test = Scanner(file_name)
    Scanner_test.Scan()
    tokens , line = Scanner_test.generate_tokens_UI()
    print(tokens)
    print(line)
    #else:
        #pass
