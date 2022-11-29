import sys
from io import StringIO

class Scanner():
    def __init__(self, file_name):
        text_file = open(file_name, "r")
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
                    while self.tiny_code[j] != '}' and j < len(self.tiny_code) :
                        j= j+1
                    self.tiny_code = self.tiny_code[:i] + self.tiny_code[j+1:]
        return
    
    #method that generate output file of tokens
    def generate_tokens(self):
        Scanner.Scan(self)
        Scanner_out = ""
        while("" in self.tokens_values):
            self.tokens_values.remove("")
        for i in range(len(self.tokens_types)):
            Scanner_out += "{},{}\n".format(self.tokens_values[i],self.tokens_types[i])
        print(Scanner_out)
        f = open("tokens.txt", "w+")
        f.write(Scanner_out)
        f.close()

    @staticmethod
    def Scan(self):
        #remove comments before start scanning
        Scanner.remove_comments(self)

        special_sympols = [';','=','<','>','+','-','*','/','(',')']
        reversed_words = ['if','then','else','end','repeat','until','read','write']

        tokens_map = {";":"SEMICOLON","=":"EQUAL","<":"LESSTHAN",">":"GREATERTHAN","+":"PLUS","-":"MINUS","*":"MULT",
                        "/":"DIV","(":"OPENBRACKET",")":"CLOSEDBRACKET"}
        
        #local list to store token_values on it
        tokens_list = []
        #loop over each line
        for tiny_in in StringIO(self.tiny_code):
            token_string = ""
            state = "START"
            i = 0
            #iterate for every char
            while i < len(tiny_in):
                if tiny_in[i] in special_sympols and state != "INASSIGN":
                    if (token_string != ""):
                        tokens_list.append(token_string)
                        token_string = ""
                    tokens_list.append(tiny_in[i])
                    state = "START"
                elif state == "START":
                    if tiny_in[i] == " ":
                        state = "START"
                    elif tiny_in[i].isalpha():
                        token_string += tiny_in[i]
                        state = "INID"
                    elif tiny_in[i].isdigit():
                        token_string += tiny_in[i]
                        state = "INNUM"
                    elif tiny_in[i] == ":":
                        token_string += tiny_in[i]
                        state = "INASSIGN"
                    else:
                        state = "DONE"
                elif state == "INID":
                    if tiny_in[i].isalpha():
                        token_string += tiny_in[i]
                        state = "INID"
                    else:
                        state = "DONE"
                elif state == "INNUM":
                    if tiny_in[i].isdigit():
                        token_string += tiny_in[i]
                        state = "INNUM"
                    else:
                        state = "DONE"
                elif state == "INASSIGN":
                    if tiny_in[i] == "=":
                        token_string += tiny_in[i]
                        state = "DONE"
                    else:
                        state = "DONE"
                elif state == "DONE":
                    tokens_list.append(token_string)
                    token_string = ""
                    state = "START"
                    i -= 1
                i += 1

            if(token_string != ""):
                tokens_list.append(token_string)
                token_string = ""

        #local list to store token_types
        tokens_types = []
        for t in tokens_list:
            if t in reversed_words:
                tokens_types.append(t.upper())
            elif t in special_sympols:
                tokens_types.append(tokens_map[t])
            elif t == ":=":
                tokens_types.append("ASSIGN")
            elif t.isdigit():
                tokens_types.append("NUMBER")
            elif t.isalpha():
                tokens_types.append("IDENTIFIER")
            else:
                pass
        # Store the local variables into object attributes
        self.tokens_values = tokens_list
        self.tokens_types = tokens_types

###############################################################################################################

if __name__ == "__main__":
    #if len(sys.argv) == 1:
        #print("Please enter right arguments\npython scanner.py FILE_NAME\nFILE_NAME that have TINY_CODE")
    #elif len(sys.argv) == 2:
    print("Please Enter the file name that have TINY_CODE and tokens file will be generated in the same directory:")
    file_name = input("Enter File name: ")
    print("Tokens generated from {} file:".format(file_name))
    Scanner_test = Scanner(file_name)
    Scanner_test.generate_tokens()
    #else:
        #pass