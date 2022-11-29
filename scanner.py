import sys


class Scanner():
    def __init__(self, file_name):
        text_file = open(file_name, "r")
        code_string = text_file.read()

        self.tiny_code = code_string.replace(";"," ; ")
        self.tokens_types = []
        self.tokens_values = []


    def remove_comments(self):
        for i in range(len(self.tiny_code)):
            if i < len(self.tiny_code):
                if self.tiny_code[i] == '{' :
                    j = i
                    while self.tiny_code[j] != '}' and j < len(self.tiny_code) :
                        j= j+1
                    self.tiny_code = self.tiny_code[:i] + self.tiny_code[j+1:]
        return
    

    def Scan(self):
        #remove comments before start
        self.remove_comments()
        #local list to store token_values on it
        tokens_list = []

        special_sympols = [';','=','<','>','+','-','*','/','(',')']
        reversed_words = ['if','then','else','end','repeat','until','read','write']

        tokens_map = {";":"SEMICOLON","=":"EQUAL","<":"LESSTHAN",">":"GREATERTHAN","+":"PLUS","-":"MINUS","*":"MULT",
                        "/":"DIV","(":"OPENBRACKET",")":"CLOSEDBRACKET"}
        #Split the text file into list of strings seprated by white space
        tiny_list = self.tiny_code.split()
        
        #loop over each string
        for tiny_in in tiny_list:
            token_string = ""
            state = "START"
            i = 0
            #iterate for every string
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

        # local list to store token_types
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

######################################################################

if __name__ == "__main__":
    Scanner_test = Scanner(sys.argv[1])
    Scanner_test.Scan()
    Scanner_out = ""
    for i in range(len(Scanner_test.tokens_values)-1):
        Scanner_out += "{},{}\n".format(Scanner_test.tokens_values[i],Scanner_test.tokens_types[i])
    print(Scanner_out)
    f = open("Scanner_out.txt", "w+")
    f.write(Scanner_out)
    f.close()

