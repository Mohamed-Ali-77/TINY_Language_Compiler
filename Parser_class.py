class Node: # node class
    def __init__(self, t, c, s):    # constructor
        self.token_value = t    # token value
        self.code_value = c # code value
        self.shape = s  # shape of the node
        self.children = []  # children of the node
        self.sibling = None # sibling of the node
        self.index = None   # index of the node

    def set_children(self, y):  # set the children of the node
        try:    # try to append the children to the list
            assert isinstance(y, list)  # check if the children is a list
            for i in y: # loop on the children
                self.children.append(i) # append the children to the list
        except: # if the children is not a list
            self.children.append(y) # append the children to the list

    def set_sibling(self, y):   # set the sibling of the node
        self.sibling = y    # set the sibling


class Parser:   # parser class
    nodes_table = {}    # nodes table
    tmp_index = 0   # index of the current node
    edges_table = []    # edges table

    def __init__(self): # constructor
        self.token = "" # current token
        self.tokens_types = ['READ', 'IDENTIFIER', 'SEMICOLON', 'IF', 'NUMBER', 'LESSTHAN', 'IDENTIFIER', 'THEN', 'IDENTIFIER', 'ASSIGN', 'NUMBER', 'SEMICOLON', 'REPEAT', 'IDENTIFIER', 'ASSIGN', 'IDENTIFIER', 'MULT', 'IDENTIFIER', 'SEMICOLON', 'IDENTIFIER', 'ASSIGN', 'IDENTIFIER', 'MINUS', 'NUMBER', 'UNTIL', 'IDENTIFIER', 'EQUAL', 'NUMBER', 'SEMICOLON', 'WRITE', 'IDENTIFIER', 'END']
        self.tokens_values = ['read', 'x', ';', 'if', '0', '<', 'x', 'then', 'fact', ':=', '1', ';', 'repeat', 'fact', ':=', 'fact', '*', 'x', ';', 'x', ':=', 'x', '-', '1', 'until', 'x', '=', '0', ';', 'write', 'fact', 'end']
        self.token = self.tokens_types[self.tmp_index]  # current token
        self.parse_tree = None  # parse tree
        self.nodes_table = None # nodes table
        self.edges_table = None # edges table
        self.same_rank_nodes = []   # same rank nodes
        self.error_tokens = [] # errors token
        self.error_indcies = []  # errors index

    def set_tokens_types_and_tokens_values(self, x, y): # set the tokens types and tokens values
        self.tokens_values = y  # set the tokens values
        self.tokens_types = x   # set the tokens types  
        self.tmp_index = 0  # set the index to 0
        self.token = self.tokens_types[self.tmp_index]  # set the current token

    def next_token(self):   # get the next token
        if(self.tmp_index == len(self.tokens_types)-1): # if we have reachd the end of the list
            return False  # we have reachd the end of the list  
        self.tmp_index = self.tmp_index + 1 # increment the index
        self.token = self.tokens_types[self.tmp_index]  # get the next token
        return True # return true

    def match(self, x): # match the current token with the expected token
        if self.token == x: # if the current token is the expected token
            self.next_token()   # get the next token
            return True # return true
        else:   # if the current token is not the expected token
            self.error_tokens.append(self.token) # set the error token
            self.error_indcies.append(self.tmp_index) # set the error index
            return False    # return false


    def statement(self): # statement -> if_stmt | repeat_stmt | assign_stmt | read_stmt | write_stmt
        if self.token == 'IF': # match if_stmt
            t = self.if_stmt() # match if_stmt
            return t # return the node
        elif self.token == 'REPEAT': # match repeat_stmt
            t = self.repeat_stmt() # match repeat_stmt
            return t # return the node
        elif self.token == 'IDENTIFIER': # match assign_stmt
            t = self.assign_stmt() # match assign_stmt
            return t    # return the node
        elif self.token == 'READ':  # match read_stmt
            t = self.read_stmt()    # match read_stmt
            return t    # return the node
        elif self.token == 'WRITE': # match write_stmt
            t = self.write_stmt()   # match write_stmt
            return t    # return the node
        else:   # if none of the above
            #raise ValueError('SyntaxError', self.token) # raise an error
            pass

    def stmt_sequence(self): # stmt_sequence -> statement ; stmt_sequence | statement
        t = self.statement() # match statement
        p = t # set p to statement
        while self.token == 'SEMICOLON': # match ';'
            q = Node(None, None, None) # create a node for ';'
            self.match('SEMICOLON') # match ';' 
            q = self.statement() # match statement
            if q == None: # if statement is empty
                break # break
            else: # if statement is not empty
                if t == None: # if statement is empty
                    t = p = q # set t to statement
                else: # if statement is not empty
                    p.set_sibling(q) # set sibling of statement
                    p = q # set p to statement
        return t # return the node

    def factor(self): # factor -> ( exp ) | number | identifier
        if self.token == 'OPENBRACKET': # match '('
            self.match('OPENBRACKET') # match '('
            t = self.exp() # match exp
            self.match('CLOSEDBRACKET') # match ')'
        elif self.token == 'NUMBER': # match number
            t = Node('CONSTANT', '(' + self.tokens_values[self.tmp_index] + ')', 'o') # create a node for number
            self.match('NUMBER') # match number
        elif self.token == 'IDENTIFIER': # match identifier
            t = Node('IDENTIFIER', '(' + self.tokens_values[self.tmp_index] + ')', 'o') # create a node for identifier
            self.match('IDENTIFIER') # match identifier
        else: # if none of the above
            print("Syntax Error:", self.token,self.tmp_index) # print an error
            #raise ValueError('SyntaxError', self.token) # raise an error
            return Node("Error", "Error", 'o') # return an empty node
        return t # return the node

    def term(self): # term -> factor mulop factor | factor
        t = self.factor() # match factor
        while self.token == 'MULT' or self.token == 'DIV': # match mulop
            p = Node('OPERATOR', '(' + self.tokens_values[self.tmp_index] + ')', 'o') # create a node for mulop
            p.set_children(t) # set the children of mulop
            t = p # set t to mulop
            self.mulop() # match mulop
            p.set_children(self.factor()) # match factor
        return t # return the node

    def simple_exp(self): # simple_exp -> term addop term | term
        t = self.term() # match term
        while self.token == 'PLUS' or self.token == 'MINUS': # match addop
            p = Node('OPERATOR', '(' + self.tokens_values[self.tmp_index] + ')', 'o') # create a node for addop
            p.set_children(t) # set the children of addop
            t = p # set t to addop
            self.addop() # match addop
            t.set_children(self.term()) # match term
        return t

    def exp(self): # exp -> simple_exp comparison_op simple_exp | simple_exp
        t = self.simple_exp() # match simple_exp
        if self.token == 'LESSTHAN' or self.token == 'EQUAL' or self.token == 'GREATERTHAN': # match comparison_op
            p = Node('OPERATOR', '(' + self.tokens_values[self.tmp_index] + ')', 'o') # create a node for comparison_op
            p.set_children(t) # set the children of comparison_op
            t = p # set t to comparison_op
            self.comparison_op() # match comparison_op
            t.set_children(self.simple_exp()) # match simple_exp
        return t # return the node

    def if_stmt(self): # if_stmt -> if exp then stmt_sequence [else stmt_sequence] end
        t = Node('IF', '', 's') # create a node for if
        if self.token == 'IF': # match if
            self.match('IF') # match if
            t.set_children(self.exp()) # match exp
            self.match('THEN')  # match then
            t.set_children(self.stmt_sequence()) # match stmt_sequence
            if self.token == 'ELSE':               #optional else
                self.match('ELSE')
                t.set_children(self.stmt_sequence())
            self.match('END') # match end
        return t # return the node

    def comparison_op(self):  # match the comparison operator
        if self.token == 'LESSTHAN':    # match the LESSTHAN operator
            self.match('LESSTHAN')    
        elif self.token == 'EQUAL':  # match the EQUAL operator
            self.match('EQUAL')
        elif self.token == 'GREATERTHAN':  # match the GREATERTHAN operator
            self.match('GREATERTHAN')

    def addop(self):   # match the add operator
        if self.token == 'PLUS':  # match the PLUS operator
            self.match('PLUS')
        elif self.token == 'MINUS': # match the MINUS operator
            self.match('MINUS')

    def mulop(self): # match the mul operator
        if self.token == 'MULT': # match the MULT operator
            self.match('MULT')
        elif self.token == 'DIV': # match the DIV operator
            self.match('DIV')

    def repeat_stmt(self):
        t = Node('REPEAT', '', 's') # create a node
        if self.token == 'REPEAT': # match the REPEAT keyword
            self.match('REPEAT')
            t.set_children(self.stmt_sequence()) # match the stmt_sequence
            self.match('UNTIL')  # match the UNTIL keyword
            t.set_children(self.exp()) # match the exp
        return t # return the node

    def assign_stmt(self):  # match the assign statement
        t = Node('ASSIGN', '(' + self.tokens_values[self.tmp_index] + ')', 's') # create a node
        self.match('IDENTIFIER') # match the IDENTIFIER
        self.match('ASSIGN')    # match the ASSIGN operator
        t.set_children(self.exp()) # match the exp
        return t # return the node

    def read_stmt(self):   # match the read statement
        t = Node('READ', '(' + self.tokens_values[self.tmp_index+1] + ')', 's') # create a node
        self.match('READ') # match the READ keyword
        self.match('IDENTIFIER') # match the IDENTIFIER
        return t # return the node

    def write_stmt(self): # match the write statement
        t = Node('WRITE', '', 's') # create a node
        self.match('WRITE')     # match the WRITE keyword
        t.set_children(self.exp()) # match the exp
        return t    # return the node

    def create_nodes_table(self, args=None): # create the nodes table
        if args == None: # check if the function is called for the first time
            self.parse_tree.index = Parser.tmp_index # set the index of the node
            Parser.nodes_table.update(
                {Parser.tmp_index: [self.parse_tree.token_value, self.parse_tree.code_value, self.parse_tree.shape]}) # add the node to the nodes table
            Parser.tmp_index = Parser.tmp_index + 1 # increment the index
            if len(self.parse_tree.children) != 0: # check if the node has children
                for i in self.parse_tree.children: # loop on the children
                    self.create_nodes_table(i) # call the function recursively
            if self.parse_tree.sibling != None: # check if the node has a sibling
                self.create_nodes_table(self.parse_tree.sibling) # call the function recursively
        else: # if the function is called recursively
            #print(args.index)
            args.index = Parser.tmp_index # set the index of the node
            #print(args.index) 
            Parser.nodes_table.update(
                {Parser.tmp_index: [args.token_value, args.code_value, args.shape]}) # add the node to the nodes table
            Parser.tmp_index = Parser.tmp_index + 1 # increment the index
            if len(args.children) != 0: # check if the node has children
                for i in args.children: # loop on the children
                    self.create_nodes_table(i) # call the function recursively
            if args.sibling != None: # check if the node has a sibling
                self.create_nodes_table(args.sibling) # call the function recursively

    def create_edges_table(self, args=None): # create the edges table
        if args == None: # check if the function is called for the first time
            if len(self.parse_tree.children) != 0: # check if the node has children
                for i in self.parse_tree.children: # loop on the children
                    Parser.edges_table.append((self.parse_tree.index, i.index)) # add the edge to the edges table
                for j in self.parse_tree.children: # loop on the children
                    self.create_edges_table(j) # call the function recursively
            if self.parse_tree.sibling != None: # check if the node has a sibling
                Parser.edges_table.append(
                    (self.parse_tree.index, self.parse_tree.sibling.index)) # add the edge to the edges table
                self.same_rank_nodes.append(
                    [self.parse_tree.index, self.parse_tree.sibling.index]) # add the nodes to the same_rank_nodes list
                self.create_edges_table(self.parse_tree.sibling) # call the function recursively
        else: # if the function is called recursively
            if len(args.children) != 0:     # check if the node has children
                for i in args.children:    # loop on the children
                    Parser.edges_table.append((args.index, i.index)) # add the edge to the edges table
                for j in args.children:   # loop on the children
                    self.create_edges_table(j) # call the function recursively
            if args.sibling != None: # check if the node has a sibling
                Parser.edges_table.append((args.index, args.sibling.index))     # add the edge to the edges table
                self.same_rank_nodes.append([args.index, args.sibling.index]) # add the nodes to the same_rank_nodes list
                self.create_edges_table(args.sibling) # call the function recursively

    def run(self): # run the parser
        self.parse_tree = self.stmt_sequence()  # create parse tree
        self.create_nodes_table()  # create nodes_table
        self.create_edges_table()  # create edges_table
        self.edges_table = Parser.edges_table  # save edges_table
        self.nodes_table = Parser.nodes_table  # save nodes_table


        if self.tmp_index == len(self.tokens_types) - 1 and self.error_tokens == [] : # check if the parser is successful
            return True, None, None # return True if the parser is successful
        
        elif self.tmp_index < len(self.tokens_types) or self.error_tokens != []: # check if the parser is not successful
            return False, self.error_tokens, self.error_indcies # return False if the parser is Unsuccessful and the token that caused the error
            #raise ValueError('SyntaxError', self.token) # raise an error if the parser is not successful

    def clear_tables(self): # clear the tables
        self.nodes_table.clear() # clear the nodes_table
        self.edges_table.clear() # clear the edges_table



if __name__ == '__main__': # main function
    parser = Parser() # create an object from the Parser class
    parser.run() # run the parser
    print(parser.nodes_table) # print the nodes_table
    print(parser.edges_table) # print the edges_table
    print(parser.same_rank_nodes) # print the same_rank_nodes list
