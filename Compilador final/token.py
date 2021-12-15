from tokentype import *
class Token:
    def __init__(self, tokenText, tokenKing):
        self.text=tokenText
        self.kind=tokenKing

    @staticmethod
    def checkIfKeyword(tokentext):
        for kind in TokenType:
            if kind.name == tokentext and kind.value >= 100 and kind.value <= 200:
                return kind
        return None