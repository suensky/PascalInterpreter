from token import *

class Interpreter():
    def __init__(self, text):
        # client string input, e.g., 3+5
        self.text = text
        self.pos = 0
        self.current_token = None
        self.current_char = text[self.pos]

    ##########################################################
    # Lexer code                                             #
    ##########################################################
    def error(self):
        raise Exception("Error parsing input")

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespaces(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = 0
        while self.current_char is not None and self.current_char.isdigit():
            result = result * 10 + int(self.current_char)
            self.advance()
        return result

    def get_next_token(self):
        """Lexical analyzer, also known as tokenizer or scanner

        This method breaks a sentence apart into tokens. One token
        at a time.
        """
        text = self.text
        if self.pos >= len(text):
            return Token(EOF, None)

        current_char = text[self.pos]

        if current_char.isspace():
            self.skip_whitespaces()
            return self.get_next_token()

        if current_char.isdigit():
            return Token(INTEGER, self.integer())

        if current_char == '+':
            token = Token(PLUS, current_char)
            self.advance()
            return token

        if current_char == '-':
            token = Token(MINUS, current_char)
            self.advance()
            return token

        if current_char == '*':
            token = Token(MUL, current_char)
            self.advance()
            return token

        if current_char == '/':
            token = Token(DIV, current_char)
            self.advance()
            return token

        self.error()

    ##########################################################
    # Parser / Interpreter code                              #
    ##########################################################
    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def factor(self):
        """factor: INTEGER"""
        token = self.current_token
        self.eat(INTEGER)
        return token.value

    def term(self):
        """term: factor((MUL | DIV)factor)* """
        result = self.factor()

        while self.current_token.type in (MUL, DIV):
            if self.current_token.type == MUL:
                self.eat(MUL)
                result *= self.factor()
            else:
                self.eat(DIV)
                result /= self.factor()

        return result

    def expr(self):
        """expr: term((PLUS|MINUS)term)* """
        self.current_token = self.get_next_token()

        # keep track of the expr with left_val + right_op * right_val
        result = self.term()
        while self.current_token.type in (PLUS, MINUS):
            if self.current_token.type == PLUS:
                self.eat(PLUS)
                result += self.term()
            else:
                self.eat(MINUS)
                result -= self.term()

        return result
