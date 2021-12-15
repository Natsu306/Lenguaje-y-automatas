import sys
from tokentype import *
from token import Token

class Lexer:
    #Constructor 
    def __init__(self, input):
        self.source=input
        self.curChar = ""
        self.curPos = -1
        self.nextChar()

    #Procesa el caracter actual 
    def nextChar(self):
        self.curPos+=1
        if self.curPos >= len(self.source):
            self.curChar = '\0' #EOF
        else:
            self.curChar = self.source[self.curPos]

    #Anticipa el caracter que sigue
    def peek(self):
        if self.curPos + 1 >= len(self.source):
            return '\0'
        return self.source[self.curPos + 1]

    #Muestra el error por si hay token invalido
    def about(self, message):
        sys.exit("Tas bien bb, aqui tienes un error de léxico" + message)

    #saltar los espacios en blanco
    def skipWhiteespace(self):
        while self.curChar == ' ' or self.curChar == '\t' or self.curChar == '\r':
            self.nextChar()

    #Saltar comentario
    def skipComment(self):
        if self.curChar == '♠':
            while self.curChar != "\n":
                self.nextChar()
    
    #obtiene el token siguiente 
    def getToken(self):
        self.skipWhiteespace()
        self.skipComment()
        token = None
        #chacar si el primer caracter + = 
        if self.curChar == '+':
            token = Token(self.curChar, TokenType.PLUS)
        elif self.curChar == '-':
            token = Token(self.curChar, TokenType.MINUS)
        elif self.curChar == '*':
            token = Token(self.curChar, TokenType.ASTERISK)
        elif self.curChar == '/':
            token = Token(self.curChar, TokenType.SLASH)
        elif self.curChar == '=':
            #verificar si estan asignando o comparando 
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar+self.curChar, TokenType.EQEQ)
            else:
                token = Token(self.curChar, TokenType.EQ)

        elif self.curChar == '>':
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                ##token = Token()(lastChar+self.curChar, TokenType.GTEQ)
                token = Token(lastChar+self.curChar, TokenType.GTEQ)
            else:
                #token = Token()(self.curChar, TokenType.GT)
                token = Token(self.curChar, TokenType.GT)

        elif self.curChar == '<':
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar+self.curChar, TokenType.LTEQ)
            else:
                token = Token(self.curChar, TokenType.LT)

        elif self.curChar == '!':
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar+self.curChar, TokenType.NOTEQ)
            else:
                self.about(" se esperaba != y escribiste un ! "+ self.peek() )

        elif self.curChar == '\"':
            self.nextChar()
            starPos = self.curPos
            while self.curChar != '\"':
                if self.curChar == '\r' or self.curChar == '\n' or self.curChar == '\\' or self.curChar == '%':
                    self.about("carater no valido en el string")
                self.nextChar()
            tokenText= self.source[starPos: self.curPos]
            token = Token(tokenText, TokenType.STRING)
        #capturar numeros 
        elif self.curChar.isdigit():
            starPos = self.curPos
            while self.peek().isdigit():
                self.nextChar()
            if self.peek() == '.':
                self.nextChar()
                if not self.peek().isdigit():
                    self.about("caracter no valido en el numero")
                
                while self.peek().isdigit():
                    tokenText = self.source[starPos: self.curPos+1]
            token = Token(tokenText, TokenType.NUMBER)

        elif self.curChar.isalpha():
            starPos = self.curPos
            while self.peek().isalnum():
                self.nextChar()
            tokenText=self.source[starPos : self.curPos +1 ]
            keyword = Token.checkIfKeyword(tokenText)
            if keyword == None:
                
                token = Token(tokenText, TokenType.IDENT)
            else:
                token = Token(tokenText, keyword)
        elif self.curChar== '\n':
            token = Token(self.curChar, TokenType.NEWLINE)
        elif self.curChar== '\0':
            token = Token(self.curChar, TokenType.EOF)
        else:
            self.about("Token Desconocido" + self.curChar)

        self.nextChar()
        return token;

