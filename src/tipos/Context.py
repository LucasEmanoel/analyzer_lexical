from typing import List, Optional

from tipos import Tipo, Token
from tipos import Identifier, Nature, Context
from tipos.SymbolTable import SymbolTable

class Context:
    def __init__(self, identifier: str, parent=None):
        self.identifier = identifier
        self.alias = None
        self.symbol_table = SymbolTable()
        
        self.lexer_counter = 0
        self.parser_counter = 0
        
        self.subcontexts:   List[Context] = [] 
        self.parent:        Context = parent 
        self.nature:        Nature = None

    def add_subcontext(self, subcontext_name: str) -> Optional[Context]:
        new_subcontext = Context(subcontext_name, parent=self)
        self.lexer_counter += 1
        self.subcontexts.append(new_subcontext)
        return new_subcontext

    def get_subcontext(self, identifier: str) -> Optional[Context]:
        for sub in self.subcontexts:
            if identifier in sub.identifier:
                return sub
        return None

    def add_reg(self, reg: Identifier, isDeclaration: bool) -> Optional[Identifier]:
        if isDeclaration:
            register = self.symbol_table.lookup(reg.nome)
        else:
            register = self.lookupByName(reg.nome)

        if(register == None):
            return self.symbol_table.add(reg)
        else:
            return register
    
    def setType(self, token: Token, newType: Tipo) -> bool:
        register = self.symbol_table.lookup(token.lexema)
        
        if(register == None):
            return False
        
        register.tipo = newType

    # def lookup(self, token: Token) -> Optional[Identifier]:
    #     if not token:
    #         return None
        
    #     registro = self.symbol_table.lookup(token.lexema)
        
    #     # não é o mesmo token, ou seja, foi criado antes
    #     if registro and registro.cod != token.indice_tabela:
    #         return registro

    #     if self.parent:
    #         return self.parent.lookup(token)  
        
    #     return None
    
    def lookupByName(self, lexema) -> Optional[Identifier]:
        registro = self.symbol_table.lookup(lexema)
        
        if registro:
            return registro

        if self.parent:
            return self.parent.lookupByName(lexema)  
        
        return None

    def list_symbols(self):
        print(f"Contexto: {self.identifier}")
        self.symbol_table.list()
        
        for subcontext in self.subcontexts:
            subcontext.list_symbols()
            
    def generate_unique_name(self, base_name):
      unique_name = f"{self.lexer_counter}_{base_name}"
      return unique_name
  
    def context_hierarchy(self, context, depth=0):
        indent = "    " * depth
        print(f"{indent} -> {context.identifier}")
        for subcontext in context.subcontexts:
            self.context_hierarchy(subcontext, depth + 1)
            
    def __str__(self):
        if not self.parent:
            return f"Identifier(nome={self.alias}, identificador='{self.identifier}', pai={self.parent.identifier})"
        return f"Identifier(nome={self.alias}, identificador='{self.identifier}', pai={self.parent.identifier})"