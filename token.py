from tokentype import *
class Token:
    def init(self, tokenText, tokenKing):
        self.text=tokenText
        self.king=tokenKing

    @staticmethod
    def checkIfKeyword(tokentext):
        for king in TokenType:
            if king.name == tokentext and king.value >= 100 and king.value <= 200:
                return king
        return None