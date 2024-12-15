class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.actualTokenPos = -1
        self.actualToken = []

    #incompleto
    def match(self, matchString):
        tokenString = self.actualToken[0][0]

        if(tokenString == 'id'):
            #lógica de ID (olhar tabela de simbolos)
            return True
        elif(tokenString == 'number'):
            #lógica de number (olhar se tem valor)
            return True
        elif(tokenString == matchString):
            return True
        
        return False
    
    def getNextToken(self):
        zeroIndexLength = len(self.tokens) - 1

        if(self.actualTokenPos < zeroIndexLength):
            self.actualTokenPos += 1
            self.actualToken = self.tokens[self.actualTokenPos]
            #token atual sendo mostrado
            print(self.actualToken)
    
    #melhorar tratativas de erros
    def start(self):
        if self.program():
            print("\033[92m[ok] Execução bem-sucedida: Deu bom!\033[0m")  
            return True
        else:
            print("\033[91m[err] Execução falhou: Deu ruim.\033[0m")  
            return False

        
    """
    def start(self):
        try:
            if self.program():
                print("\033[92m[ok] Execução bem-sucedida: Deu bom!\033[0m")  
                return True
            else:
                print("\033[91m[err] Execução falhou: Deu ruim.\033[0m")  
                return False
        except Exception as e:
            print(f"\033[93m[!] Erro ao executar o programa: {e}\033[0m")  
            return False
    """
    # ================= Descrição BNF da Linguagem Simplificada ===================================== #
    
    def program(self):
        self.getNextToken()

        if self.subRoutineStep():
            return True
        elif self.mainBody():
            return True
        return False
    
    def mainBody(self):
        if(self.match("meme")):
            self.getNextToken()

            if(self.body()):
                return True
        return False 
    
    def body(self):
        #Valida se termina começa com "{"
        if(self.match("{")):
            self.getNextToken()

            #Valida se tem variáveis declaradas [<variable-declaration-step>]
            if(self.declarationVariableStep()):
                self.getNextToken()

            #Valida se tem comandos
            if(self.statements()):
                self.getNextToken()

                #Valida se termina com "}"
                if(self.match("}")):
                    return True
        return False
    
    #incompleto 
    def subRoutineStep(self):      
        if self.declarationProcedure():
            self.getNextToken()
            return True
        elif self.declarationFunction():
            self.getNextToken()
            return True
        return False
    
    #incompleto
    def declarationVariableStep(self):
    
        if self.declarationVariable():
            self.getNextToken()
            return True
        elif self.declarationVariableInitial():
            self.getNextToken()
            return True
        return False
    
    # ==================================== DECLARAÇÕES =============================================== #
    
    def type(self):
        if(self.match("int")):
            return True
        elif(self.match("bruh")):
            return True
        
        return False
    
    # Fazer mais declarações
    def declarationVariable(self):
        if self.type():
            self.getNextToken()
            if self.identifier():
                self.getNextToken()
                if self.colon():
                    self.getNextToken()
                    
                    while self.type():
                        if not self.declarationVariable():
                            return False

                    return True 
        return False

    def declarationVariableInitial(self):
        if self.type():
            self.getNextToken()
            if self.assignStatement():
                self.getNextToken()
                while self.type():
                    if not self.declarationVariableInitial():
                        return False
                return True 
        return False
    
    def declarationParameters(self):
        if(self.type()):
            self.getNextToken()
            if(self.identifier()):
                self.getNextToken()
                
            while self.match(','):
                self.getNextToken()
                self.declarationParameters()
                
            return True
        
        return False
    
    # <declaration-procedure> ::= void hora_do_show <identifier> ([<declaration-parameters>]*) <body>
    def declarationProcedure(self):
        if(self.match("void")):
            self.getNextToken()
            if(self.match('hora_do_show')):
                self.getNextToken()
                if(self.identifier()):
                    self.getNextToken()
                    if(self.match('(')):
                        self.getNextToken()
                        self.declarationParameters()
                        
                        if(self.match(')')):
                            self.getNextToken()
                            if(self.body()):
                                return True
                        
        return False
            
    def declarationFunction(self):
        if(self.type()):
            self.getNextToken()
            if(self.match('hora_do_show')):
                self.getNextToken()
                if(self.identifier()):
                    self.getNextToken()
                    if(self.match('(')):
                        self.getNextToken()
                        self.declarationParameters()
                        
                        if(self.match(')')):
                            self.getNextToken()
                            if(self.body()):
                                return True
        return False
    
    # ==================================== COMANDOS =============================================== #
    
    def statements(self):
        if(self.statement()):
            hasStatementsLeft = True
            while(hasStatementsLeft):
                self.getNextToken()

                hasStatementsLeft = self.statement()

            return True
        return False
    
    #completo mas precisar testar todos os casos
    def statement(self):
        if(self.conditionStatement()):
            return True
        elif(self.loopStatement()):
            return True
        elif(self.printStatement()):
            return True
        elif(self.readStatement()):
            return True
        elif(self.callOrAssignStatement()):
            return True
        return False
    
    #incompleto
    def conditionStatement(self):
        #não tá lendo o ?
        if(self.match("irineu_voce_sabe")):
            self.getNextToken()

            if(self.match("(")):
                self.getNextToken()

                if(self.expression()):
                    self.getNextToken()
                    
                    if(self.match(")")):
                        self.getNextToken()

                        if(self.body()):
                            #verificar se vale a pena fazer o else

                            return True
        return False
    
    #incompleto
    def loopStatement(self):
        #validar se vale a pena fazer o do-while
        if(self.match("here_we_go_again")):
            self.getNextToken()

            if(self.match("(")):
                self.getNextToken()

                if(self.expression()):
                    self.getNextToken()
                    
                    if(self.match(")")):
                        self.getNextToken()

                        #validar como fazer um body diferente para permitir break e continue
                        if(self.body()):
                            return True
        return False

    def printStatement(self):
        if(self.match("amostradinho")):
            self.getNextToken()

            if(self.match("(")):
                self.getNextToken()
                
                if(self.expression()):
                    self.getNextToken()
                    
                    if(self.match(")")):
                        self.getNextToken()

                        
                        if(self.match(";")):
                            return True
        return False
    
    #não testado ainda por causa de identifier
    def readStatement(self):
        if(self.match("casca_de_bala")):
            self.getNextToken()

            if(self.match("(")):
                self.getNextToken()

                if(self.identifier()):
                    self.getNextToken()
                    
                    if(self.match(")")):
                        self.getNextToken()

                        if(self.match(";")):
                            return True
        return False
    
    def returnStatement(self):
        if(self.match("receba")):
            self.getNextToken()

            if(self.expression()):
                self.getNextToken()

                if(self.match(";")):
                    return True

        return False
    
    #não testado ainda por causa de identifier e declarationParameters
    def callOrAssignStatement(self):
        if(self.assignStatement()):
            return True
        elif(self.callFunctionStatement()):
            return True
        
        return False

    #não testado ainda por causa de identifier
    def assignStatement(self):
        if(self.identifier()):
            self.getNextToken()

            if(self.match("=")):
                self.getNextToken()

                if(self.expression()):
                    self.getNextToken()

                    if(self.match(";")):
                        return True
        return False
    
    #incompleto
    def callFunctionStatement(self):
        if(self.identifier()):
            self.getNextToken()

            if(self.match("(")):
                self.getNextToken()

                #finalizar
                # if(self.declarationParameters()):
                #     self.getNextToken()

                #     if(self.match(")")):
                #         self.getNextToken()

                #         if(self.match(";")):
                #             return True
        return False

    # ==================================== EXPRESSÕES =============================================== #
    
    #incompleto
    def expression(self):
        if(self.simpleExpression()):
            
            self.getNextToken()
            
            if(self.assignStatement()):
                self.getNextToken()
                
                if(self.simpleExpression()):
                    return True
            else:
                return True
            return True
        return False

    #incompleto
    def simpleExpression(self):
        self.unaryOperator()
        
        if(self.term()):
            return True
        
        return False

    def unaryOperator(self):
        if(self.match("+")):
            self.getNextToken()
            return True
        elif(self.match("-")):
            self.getNextToken()
            return True
        elif(self.match("!")):
            self.getNextToken()
            return True

        return False
    
    def assignOperator(self):
        if(self.match("==")):
            self.getNextToken()
            return True
        elif(self.match("!=")):
            self.getNextToken()
            return True
        elif(self.match("<")):
            self.getNextToken()
            return True
        elif(self.match("<=")):
            self.getNextToken()
            return True
        elif(self.match(">")):
            self.getNextToken()
            return True
        elif(self.match(">=")):
            self.getNextToken()
            return True
        elif(self.match("AND")):
            self.getNextToken()
            return True
        elif(self.match("OR")):
            self.getNextToken()
            return True

        return False
    
    #incompleto
    def term(self):
        if(self.factor()):
            self.getNextToken()

            while self.match('+') or self.match('-') or self.match('*') or self.match('/'):
                self.getNextToken()
                self.term()

            return True
        return False
    
    #incompleto
    def factor(self):
        if(self.identifier()):
            return True
        elif(self.number()):
            return True
        elif(self.callFunctionStatement()):
            return True
        elif(self.expression()):
            return True
        elif(self.match("real")):
            return True
        elif(self.match("barça")):
            return True

        return False

    # ==================================== NÚMEROS E IDENTIFICADORES =============================================== #
    
    def identifier(self):
        if(self.match("id")):
            return True
        
        return False
    
    def number(self):
        if(self.match('number')):
            return True
        
        return False
    
    def colon(self):
        if(self.match(";")):
            return True
        
        return False
    
    def comment(self):
        if(self.match("//")):
            return True
        
        return False