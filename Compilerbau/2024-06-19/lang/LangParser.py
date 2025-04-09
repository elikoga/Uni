# Generated from Lang.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,42,191,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,1,0,5,0,48,8,0,10,0,12,0,51,9,0,1,0,1,0,
        1,1,1,1,1,1,3,1,58,8,1,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,69,
        8,3,1,4,1,4,3,4,73,8,4,1,5,1,5,1,5,1,5,1,5,3,5,80,8,5,3,5,82,8,5,
        1,6,1,6,1,6,1,6,3,6,88,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,3,7,101,8,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,5,7,115,8,7,10,7,12,7,118,9,7,1,8,1,8,4,8,122,8,8,11,8,12,8,123,
        1,8,5,8,127,8,8,10,8,12,8,130,9,8,1,8,3,8,133,8,8,1,8,1,8,1,9,1,
        9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,3,11,149,8,11,
        1,12,1,12,1,13,1,13,1,14,1,14,1,14,1,14,1,14,5,14,160,8,14,10,14,
        12,14,163,9,14,3,14,165,8,14,1,14,1,14,1,15,1,15,1,15,1,15,3,15,
        173,8,15,1,16,1,16,1,16,1,16,1,17,1,17,1,18,1,18,1,19,1,19,1,20,
        1,20,1,21,1,21,1,22,1,22,1,22,0,1,14,23,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,38,40,42,44,0,5,1,0,23,26,1,0,2,7,1,0,
        8,13,1,0,14,15,2,0,16,20,40,40,193,0,49,1,0,0,0,2,57,1,0,0,0,4,59,
        1,0,0,0,6,61,1,0,0,0,8,72,1,0,0,0,10,81,1,0,0,0,12,87,1,0,0,0,14,
        100,1,0,0,0,16,119,1,0,0,0,18,136,1,0,0,0,20,139,1,0,0,0,22,143,
        1,0,0,0,24,150,1,0,0,0,26,152,1,0,0,0,28,154,1,0,0,0,30,172,1,0,
        0,0,32,174,1,0,0,0,34,178,1,0,0,0,36,180,1,0,0,0,38,182,1,0,0,0,
        40,184,1,0,0,0,42,186,1,0,0,0,44,188,1,0,0,0,46,48,3,2,1,0,47,46,
        1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,52,1,0,0,0,
        51,49,1,0,0,0,52,53,5,0,0,1,53,1,1,0,0,0,54,58,3,6,3,0,55,58,3,10,
        5,0,56,58,3,4,2,0,57,54,1,0,0,0,57,55,1,0,0,0,57,56,1,0,0,0,58,3,
        1,0,0,0,59,60,5,22,0,0,60,5,1,0,0,0,61,62,5,28,0,0,62,63,5,41,0,
        0,63,64,5,38,0,0,64,65,3,44,22,0,65,66,5,40,0,0,66,68,3,14,7,0,67,
        69,5,36,0,0,68,67,1,0,0,0,68,69,1,0,0,0,69,7,1,0,0,0,70,73,3,12,
        6,0,71,73,3,14,7,0,72,70,1,0,0,0,72,71,1,0,0,0,73,9,1,0,0,0,74,75,
        3,14,7,0,75,76,5,36,0,0,76,82,1,0,0,0,77,79,3,12,6,0,78,80,5,36,
        0,0,79,78,1,0,0,0,79,80,1,0,0,0,80,82,1,0,0,0,81,74,1,0,0,0,81,77,
        1,0,0,0,82,11,1,0,0,0,83,88,3,16,8,0,84,88,3,18,9,0,85,88,3,20,10,
        0,86,88,3,22,11,0,87,83,1,0,0,0,87,84,1,0,0,0,87,85,1,0,0,0,87,86,
        1,0,0,0,88,13,1,0,0,0,89,90,6,7,-1,0,90,101,3,24,12,0,91,101,3,26,
        13,0,92,101,3,28,14,0,93,101,3,30,15,0,94,101,3,32,16,0,95,101,3,
        42,21,0,96,97,3,26,13,0,97,98,3,40,20,0,98,99,3,14,7,1,99,101,1,
        0,0,0,100,89,1,0,0,0,100,91,1,0,0,0,100,92,1,0,0,0,100,93,1,0,0,
        0,100,94,1,0,0,0,100,95,1,0,0,0,100,96,1,0,0,0,101,116,1,0,0,0,102,
        103,10,4,0,0,103,104,3,34,17,0,104,105,3,14,7,5,105,115,1,0,0,0,
        106,107,10,3,0,0,107,108,3,36,18,0,108,109,3,14,7,4,109,115,1,0,
        0,0,110,111,10,2,0,0,111,112,3,38,19,0,112,113,3,14,7,3,113,115,
        1,0,0,0,114,102,1,0,0,0,114,106,1,0,0,0,114,110,1,0,0,0,115,118,
        1,0,0,0,116,114,1,0,0,0,116,117,1,0,0,0,117,15,1,0,0,0,118,116,1,
        0,0,0,119,132,5,32,0,0,120,122,3,2,1,0,121,120,1,0,0,0,122,123,1,
        0,0,0,123,121,1,0,0,0,123,124,1,0,0,0,124,133,1,0,0,0,125,127,3,
        2,1,0,126,125,1,0,0,0,127,130,1,0,0,0,128,126,1,0,0,0,128,129,1,
        0,0,0,129,131,1,0,0,0,130,128,1,0,0,0,131,133,3,14,7,0,132,121,1,
        0,0,0,132,128,1,0,0,0,133,134,1,0,0,0,134,135,5,33,0,0,135,17,1,
        0,0,0,136,137,5,29,0,0,137,138,3,16,8,0,138,19,1,0,0,0,139,140,5,
        27,0,0,140,141,3,14,7,0,141,142,3,16,8,0,142,21,1,0,0,0,143,144,
        5,30,0,0,144,145,3,8,4,0,145,148,3,16,8,0,146,147,5,31,0,0,147,149,
        3,16,8,0,148,146,1,0,0,0,148,149,1,0,0,0,149,23,1,0,0,0,150,151,
        7,0,0,0,151,25,1,0,0,0,152,153,5,41,0,0,153,27,1,0,0,0,154,155,5,
        41,0,0,155,164,5,34,0,0,156,161,3,8,4,0,157,158,5,37,0,0,158,160,
        3,8,4,0,159,157,1,0,0,0,160,163,1,0,0,0,161,159,1,0,0,0,161,162,
        1,0,0,0,162,165,1,0,0,0,163,161,1,0,0,0,164,156,1,0,0,0,164,165,
        1,0,0,0,165,166,1,0,0,0,166,167,5,35,0,0,167,29,1,0,0,0,168,169,
        5,1,0,0,169,173,3,8,4,0,170,171,5,2,0,0,171,173,3,8,4,0,172,168,
        1,0,0,0,172,170,1,0,0,0,173,31,1,0,0,0,174,175,5,34,0,0,175,176,
        3,8,4,0,176,177,5,35,0,0,177,33,1,0,0,0,178,179,7,1,0,0,179,35,1,
        0,0,0,180,181,7,2,0,0,181,37,1,0,0,0,182,183,7,3,0,0,183,39,1,0,
        0,0,184,185,7,4,0,0,185,41,1,0,0,0,186,187,5,21,0,0,187,43,1,0,0,
        0,188,189,5,42,0,0,189,45,1,0,0,0,17,49,57,68,72,79,81,87,100,114,
        116,123,128,132,148,161,164,172
    ]

class LangParser ( Parser ):

    grammarFileName = "Lang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'!'", "'-'", "'+'", "'*'", "'/'", "'%'", 
                     "'**'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'&&'", "'||'", "'+='", "'-='", "'*='", "'/='", "'%='", 
                     "'break'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'while'", "'let'", "'loop'", "'if'", 
                     "'else'", "'{'", "'}'", "'('", "')'", "';'", "','", 
                     "':'", "<INVALID>", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "Comment", "INTEGER", "FLOAT", 
                      "STRING", "BOOLEAN", "WHILE", "LET", "LOOP", "IF", 
                      "ELSE", "LBRACE", "RBRACE", "LPAREN", "RPAREN", "SEMICOLON", 
                      "COMMA", "COLON", "WS", "EQUAL", "IDENTIFIER_LOWERCASE_START", 
                      "IDENTIFIER_CAPITAL_START" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_comment = 2
    RULE_let_statement = 3
    RULE_expression = 4
    RULE_expression_statement = 5
    RULE_expression_with_block = 6
    RULE_expression_without_block = 7
    RULE_block_expression = 8
    RULE_loop_expression = 9
    RULE_while_expression = 10
    RULE_if_expression = 11
    RULE_literal_expression = 12
    RULE_variable_expression = 13
    RULE_function_call_expression = 14
    RULE_negation_expression = 15
    RULE_grouped_expression = 16
    RULE_math_operator = 17
    RULE_comparison_operator = 18
    RULE_logical_operator = 19
    RULE_assignment_operator = 20
    RULE_break_expression = 21
    RULE_type = 22

    ruleNames =  [ "program", "statement", "comment", "let_statement", "expression", 
                   "expression_statement", "expression_with_block", "expression_without_block", 
                   "block_expression", "loop_expression", "while_expression", 
                   "if_expression", "literal_expression", "variable_expression", 
                   "function_call_expression", "negation_expression", "grouped_expression", 
                   "math_operator", "comparison_operator", "logical_operator", 
                   "assignment_operator", "break_expression", "type" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    Comment=22
    INTEGER=23
    FLOAT=24
    STRING=25
    BOOLEAN=26
    WHILE=27
    LET=28
    LOOP=29
    IF=30
    ELSE=31
    LBRACE=32
    RBRACE=33
    LPAREN=34
    RPAREN=35
    SEMICOLON=36
    COMMA=37
    COLON=38
    WS=39
    EQUAL=40
    IDENTIFIER_LOWERCASE_START=41
    IDENTIFIER_CAPITAL_START=42

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(LangParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangParser.StatementContext)
            else:
                return self.getTypedRuleContext(LangParser.StatementContext,i)


        def getRuleIndex(self):
            return LangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = LangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2222643478534) != 0):
                self.state = 46
                self.statement()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 52
            self.match(LangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def let_statement(self):
            return self.getTypedRuleContext(LangParser.Let_statementContext,0)


        def expression_statement(self):
            return self.getTypedRuleContext(LangParser.Expression_statementContext,0)


        def comment(self):
            return self.getTypedRuleContext(LangParser.CommentContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = LangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.let_statement()
                pass
            elif token in [1, 2, 21, 23, 24, 25, 26, 27, 29, 30, 32, 34, 41]:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.expression_statement()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 56
                self.comment()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Comment(self):
            return self.getToken(LangParser.Comment, 0)

        def getRuleIndex(self):
            return LangParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComment" ):
                return visitor.visitComment(self)
            else:
                return visitor.visitChildren(self)




    def comment(self):

        localctx = LangParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(LangParser.Comment)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Let_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET(self):
            return self.getToken(LangParser.LET, 0)

        def IDENTIFIER_LOWERCASE_START(self):
            return self.getToken(LangParser.IDENTIFIER_LOWERCASE_START, 0)

        def COLON(self):
            return self.getToken(LangParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(LangParser.TypeContext,0)


        def EQUAL(self):
            return self.getToken(LangParser.EQUAL, 0)

        def expression_without_block(self):
            return self.getTypedRuleContext(LangParser.Expression_without_blockContext,0)


        def SEMICOLON(self):
            return self.getToken(LangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return LangParser.RULE_let_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLet_statement" ):
                listener.enterLet_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLet_statement" ):
                listener.exitLet_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLet_statement" ):
                return visitor.visitLet_statement(self)
            else:
                return visitor.visitChildren(self)




    def let_statement(self):

        localctx = LangParser.Let_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_let_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(LangParser.LET)
            self.state = 62
            self.match(LangParser.IDENTIFIER_LOWERCASE_START)
            self.state = 63
            self.match(LangParser.COLON)
            self.state = 64
            self.type_()
            self.state = 65
            self.match(LangParser.EQUAL)
            self.state = 66
            self.expression_without_block(0)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 67
                self.match(LangParser.SEMICOLON)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_with_block(self):
            return self.getTypedRuleContext(LangParser.Expression_with_blockContext,0)


        def expression_without_block(self):
            return self.getTypedRuleContext(LangParser.Expression_without_blockContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = LangParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expression)
        try:
            self.state = 72
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27, 29, 30, 32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.expression_with_block()
                pass
            elif token in [1, 2, 21, 23, 24, 25, 26, 34, 41]:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.expression_without_block(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_without_block(self):
            return self.getTypedRuleContext(LangParser.Expression_without_blockContext,0)


        def SEMICOLON(self):
            return self.getToken(LangParser.SEMICOLON, 0)

        def expression_with_block(self):
            return self.getTypedRuleContext(LangParser.Expression_with_blockContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_expression_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression_statement" ):
                listener.enterExpression_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression_statement" ):
                listener.exitExpression_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_statement" ):
                return visitor.visitExpression_statement(self)
            else:
                return visitor.visitChildren(self)




    def expression_statement(self):

        localctx = LangParser.Expression_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expression_statement)
        self._la = 0 # Token type
        try:
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 21, 23, 24, 25, 26, 34, 41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.expression_without_block(0)
                self.state = 75
                self.match(LangParser.SEMICOLON)
                pass
            elif token in [27, 29, 30, 32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.expression_with_block()
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==36:
                    self.state = 78
                    self.match(LangParser.SEMICOLON)


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_with_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_expression(self):
            return self.getTypedRuleContext(LangParser.Block_expressionContext,0)


        def loop_expression(self):
            return self.getTypedRuleContext(LangParser.Loop_expressionContext,0)


        def while_expression(self):
            return self.getTypedRuleContext(LangParser.While_expressionContext,0)


        def if_expression(self):
            return self.getTypedRuleContext(LangParser.If_expressionContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_expression_with_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression_with_block" ):
                listener.enterExpression_with_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression_with_block" ):
                listener.exitExpression_with_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_with_block" ):
                return visitor.visitExpression_with_block(self)
            else:
                return visitor.visitChildren(self)




    def expression_with_block(self):

        localctx = LangParser.Expression_with_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expression_with_block)
        try:
            self.state = 87
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.block_expression()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.loop_expression()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 3)
                self.state = 85
                self.while_expression()
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 4)
                self.state = 86
                self.if_expression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_without_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal_expression(self):
            return self.getTypedRuleContext(LangParser.Literal_expressionContext,0)


        def variable_expression(self):
            return self.getTypedRuleContext(LangParser.Variable_expressionContext,0)


        def function_call_expression(self):
            return self.getTypedRuleContext(LangParser.Function_call_expressionContext,0)


        def negation_expression(self):
            return self.getTypedRuleContext(LangParser.Negation_expressionContext,0)


        def grouped_expression(self):
            return self.getTypedRuleContext(LangParser.Grouped_expressionContext,0)


        def break_expression(self):
            return self.getTypedRuleContext(LangParser.Break_expressionContext,0)


        def assignment_operator(self):
            return self.getTypedRuleContext(LangParser.Assignment_operatorContext,0)


        def expression_without_block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangParser.Expression_without_blockContext)
            else:
                return self.getTypedRuleContext(LangParser.Expression_without_blockContext,i)


        def math_operator(self):
            return self.getTypedRuleContext(LangParser.Math_operatorContext,0)


        def comparison_operator(self):
            return self.getTypedRuleContext(LangParser.Comparison_operatorContext,0)


        def logical_operator(self):
            return self.getTypedRuleContext(LangParser.Logical_operatorContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_expression_without_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression_without_block" ):
                listener.enterExpression_without_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression_without_block" ):
                listener.exitExpression_without_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_without_block" ):
                return visitor.visitExpression_without_block(self)
            else:
                return visitor.visitChildren(self)



    def expression_without_block(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LangParser.Expression_without_blockContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expression_without_block, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 90
                self.literal_expression()
                pass

            elif la_ == 2:
                self.state = 91
                self.variable_expression()
                pass

            elif la_ == 3:
                self.state = 92
                self.function_call_expression()
                pass

            elif la_ == 4:
                self.state = 93
                self.negation_expression()
                pass

            elif la_ == 5:
                self.state = 94
                self.grouped_expression()
                pass

            elif la_ == 6:
                self.state = 95
                self.break_expression()
                pass

            elif la_ == 7:
                self.state = 96
                self.variable_expression()
                self.state = 97
                self.assignment_operator()
                self.state = 98
                self.expression_without_block(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 116
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 114
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = LangParser.Expression_without_blockContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_without_block)
                        self.state = 102
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 103
                        self.math_operator()
                        self.state = 104
                        self.expression_without_block(5)
                        pass

                    elif la_ == 2:
                        localctx = LangParser.Expression_without_blockContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_without_block)
                        self.state = 106
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 107
                        self.comparison_operator()
                        self.state = 108
                        self.expression_without_block(4)
                        pass

                    elif la_ == 3:
                        localctx = LangParser.Expression_without_blockContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_without_block)
                        self.state = 110
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 111
                        self.logical_operator()
                        self.state = 112
                        self.expression_without_block(3)
                        pass

             
                self.state = 118
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Block_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(LangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(LangParser.RBRACE, 0)

        def expression_without_block(self):
            return self.getTypedRuleContext(LangParser.Expression_without_blockContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangParser.StatementContext)
            else:
                return self.getTypedRuleContext(LangParser.StatementContext,i)


        def getRuleIndex(self):
            return LangParser.RULE_block_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_expression" ):
                listener.enterBlock_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_expression" ):
                listener.exitBlock_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_expression" ):
                return visitor.visitBlock_expression(self)
            else:
                return visitor.visitChildren(self)




    def block_expression(self):

        localctx = LangParser.Block_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_block_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(LangParser.LBRACE)
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 121 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 120
                    self.statement()
                    self.state = 123 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2222643478534) != 0)):
                        break

                pass

            elif la_ == 2:
                self.state = 128
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 125
                        self.statement() 
                    self.state = 130
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

                self.state = 131
                self.expression_without_block(0)
                pass


            self.state = 134
            self.match(LangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOOP(self):
            return self.getToken(LangParser.LOOP, 0)

        def block_expression(self):
            return self.getTypedRuleContext(LangParser.Block_expressionContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_loop_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop_expression" ):
                listener.enterLoop_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop_expression" ):
                listener.exitLoop_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_expression" ):
                return visitor.visitLoop_expression(self)
            else:
                return visitor.visitChildren(self)




    def loop_expression(self):

        localctx = LangParser.Loop_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_loop_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(LangParser.LOOP)
            self.state = 137
            self.block_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(LangParser.WHILE, 0)

        def expression_without_block(self):
            return self.getTypedRuleContext(LangParser.Expression_without_blockContext,0)


        def block_expression(self):
            return self.getTypedRuleContext(LangParser.Block_expressionContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_while_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_expression" ):
                listener.enterWhile_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_expression" ):
                listener.exitWhile_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_expression" ):
                return visitor.visitWhile_expression(self)
            else:
                return visitor.visitChildren(self)




    def while_expression(self):

        localctx = LangParser.While_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_while_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(LangParser.WHILE)
            self.state = 140
            self.expression_without_block(0)
            self.state = 141
            self.block_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(LangParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(LangParser.ExpressionContext,0)


        def block_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangParser.Block_expressionContext)
            else:
                return self.getTypedRuleContext(LangParser.Block_expressionContext,i)


        def ELSE(self):
            return self.getToken(LangParser.ELSE, 0)

        def getRuleIndex(self):
            return LangParser.RULE_if_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_expression" ):
                listener.enterIf_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_expression" ):
                listener.exitIf_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_expression" ):
                return visitor.visitIf_expression(self)
            else:
                return visitor.visitChildren(self)




    def if_expression(self):

        localctx = LangParser.If_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_if_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(LangParser.IF)
            self.state = 144
            self.expression()
            self.state = 145
            self.block_expression()
            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 146
                self.match(LangParser.ELSE)
                self.state = 147
                self.block_expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(LangParser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(LangParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(LangParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(LangParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return LangParser.RULE_literal_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral_expression" ):
                listener.enterLiteral_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral_expression" ):
                listener.exitLiteral_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral_expression" ):
                return visitor.visitLiteral_expression(self)
            else:
                return visitor.visitChildren(self)




    def literal_expression(self):

        localctx = LangParser.Literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_literal_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 125829120) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER_LOWERCASE_START(self):
            return self.getToken(LangParser.IDENTIFIER_LOWERCASE_START, 0)

        def getRuleIndex(self):
            return LangParser.RULE_variable_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_expression" ):
                listener.enterVariable_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_expression" ):
                listener.exitVariable_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_expression" ):
                return visitor.visitVariable_expression(self)
            else:
                return visitor.visitChildren(self)




    def variable_expression(self):

        localctx = LangParser.Variable_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_variable_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(LangParser.IDENTIFIER_LOWERCASE_START)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_call_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER_LOWERCASE_START(self):
            return self.getToken(LangParser.IDENTIFIER_LOWERCASE_START, 0)

        def LPAREN(self):
            return self.getToken(LangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(LangParser.RPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LangParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LangParser.COMMA)
            else:
                return self.getToken(LangParser.COMMA, i)

        def getRuleIndex(self):
            return LangParser.RULE_function_call_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call_expression" ):
                listener.enterFunction_call_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call_expression" ):
                listener.exitFunction_call_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call_expression" ):
                return visitor.visitFunction_call_expression(self)
            else:
                return visitor.visitChildren(self)




    def function_call_expression(self):

        localctx = LangParser.Function_call_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_function_call_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(LangParser.IDENTIFIER_LOWERCASE_START)
            self.state = 155
            self.match(LangParser.LPAREN)
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2222370848774) != 0):
                self.state = 156
                self.expression()
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==37:
                    self.state = 157
                    self.match(LangParser.COMMA)
                    self.state = 158
                    self.expression()
                    self.state = 163
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 166
            self.match(LangParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Negation_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(LangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_negation_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegation_expression" ):
                listener.enterNegation_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegation_expression" ):
                listener.exitNegation_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegation_expression" ):
                return visitor.visitNegation_expression(self)
            else:
                return visitor.visitChildren(self)




    def negation_expression(self):

        localctx = LangParser.Negation_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_negation_expression)
        try:
            self.state = 172
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.match(LangParser.T__0)
                self.state = 169
                self.expression()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.match(LangParser.T__1)
                self.state = 171
                self.expression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Grouped_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(LangParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(LangParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(LangParser.RPAREN, 0)

        def getRuleIndex(self):
            return LangParser.RULE_grouped_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGrouped_expression" ):
                listener.enterGrouped_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGrouped_expression" ):
                listener.exitGrouped_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGrouped_expression" ):
                return visitor.visitGrouped_expression(self)
            else:
                return visitor.visitChildren(self)




    def grouped_expression(self):

        localctx = LangParser.Grouped_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_grouped_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(LangParser.LPAREN)
            self.state = 175
            self.expression()
            self.state = 176
            self.match(LangParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Math_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LangParser.RULE_math_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMath_operator" ):
                listener.enterMath_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMath_operator" ):
                listener.exitMath_operator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMath_operator" ):
                return visitor.visitMath_operator(self)
            else:
                return visitor.visitChildren(self)




    def math_operator(self):

        localctx = LangParser.Math_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_math_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 252) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comparison_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LangParser.RULE_comparison_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison_operator" ):
                listener.enterComparison_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison_operator" ):
                listener.exitComparison_operator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison_operator" ):
                return visitor.visitComparison_operator(self)
            else:
                return visitor.visitChildren(self)




    def comparison_operator(self):

        localctx = LangParser.Comparison_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_comparison_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16128) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LangParser.RULE_logical_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogical_operator" ):
                listener.enterLogical_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogical_operator" ):
                listener.exitLogical_operator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_operator" ):
                return visitor.visitLogical_operator(self)
            else:
                return visitor.visitChildren(self)




    def logical_operator(self):

        localctx = LangParser.Logical_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_logical_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            _la = self._input.LA(1)
            if not(_la==14 or _la==15):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(LangParser.EQUAL, 0)

        def getRuleIndex(self):
            return LangParser.RULE_assignment_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_operator" ):
                listener.enterAssignment_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_operator" ):
                listener.exitAssignment_operator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_operator" ):
                return visitor.visitAssignment_operator(self)
            else:
                return visitor.visitChildren(self)




    def assignment_operator(self):

        localctx = LangParser.Assignment_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_assignment_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1099513659392) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LangParser.RULE_break_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreak_expression" ):
                listener.enterBreak_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreak_expression" ):
                listener.exitBreak_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_expression" ):
                return visitor.visitBreak_expression(self)
            else:
                return visitor.visitChildren(self)




    def break_expression(self):

        localctx = LangParser.Break_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_break_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(LangParser.T__20)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER_CAPITAL_START(self):
            return self.getToken(LangParser.IDENTIFIER_CAPITAL_START, 0)

        def getRuleIndex(self):
            return LangParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = LangParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(LangParser.IDENTIFIER_CAPITAL_START)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.expression_without_block_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_without_block_sempred(self, localctx:Expression_without_blockContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




