# Token types
#
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis
INTEGER, PLUS, MINUS, EOF = 'INTEGER', 'PLUS', 'MINUS', 'EOF'

class Token():
    def __init__(self, type, value):
        # token type: INTEGER, PLUS, EOF
        self.type = type
        self.value = value

    def __str__(self):
        """String representation of the instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS, '+')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value))

    def __repr__(self):
        return self.__str__()