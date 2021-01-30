from token import *

class Interpreter():
    def __init__(self, text):
        # client string input, e.g., 3+5
        self.text = text
        self.pos = 0
        self.current_token = None

    def error(self):
        raise Exception("Error parsing input")

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
            self.pos +=1
            return get_next_token(self)

        if current_char.isdigit():
            current_value = 0
            while current_char.isdigit():
                current_value = current_value * 10 + int(current_char)
                self.pos += 1
                if self.pos >= len(text):
                    break

                current_char = text[self.pos]

            token = Token(INTEGER, current_value)
            return token

        if current_char == '+':
            token = Token(PLUS, current_char)
            self.pos += 1
            return token

        if current_char == '-':
            token = Token(MINUS, current_char)
            self.pos += 1
            return token

        self.error()

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        self.current_token = self.get_next_token()

        left = self.current_token
        self.eat(INTEGER)

        op = self.current_token
        if op.type == PLUS:
            self.eat(PLUS)
        elif op.type == MINUS:
            self.eat(MINUS)

        right = self.current_token
        self.eat(INTEGER)

        if op.type == PLUS:
            result = left.value + right.value
        elif op.type == MINUS:
            result = left.value - right.value
        return result
