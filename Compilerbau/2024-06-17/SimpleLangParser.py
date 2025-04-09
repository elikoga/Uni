# Generated from SimpleLang.g4 by ANTLR 4.13.0
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
        4,1,7,47,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,5,0,
        14,8,0,10,0,12,0,17,9,0,1,0,1,0,1,1,1,1,3,1,23,8,1,1,2,1,2,1,2,1,
        2,1,3,1,3,1,3,3,3,32,8,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,5,5,42,
        8,5,10,5,12,5,45,9,5,1,5,0,0,6,0,2,4,6,8,10,0,0,45,0,15,1,0,0,0,
        2,22,1,0,0,0,4,24,1,0,0,0,6,31,1,0,0,0,8,33,1,0,0,0,10,38,1,0,0,
        0,12,14,3,2,1,0,13,12,1,0,0,0,14,17,1,0,0,0,15,13,1,0,0,0,15,16,
        1,0,0,0,16,18,1,0,0,0,17,15,1,0,0,0,18,19,5,0,0,1,19,1,1,0,0,0,20,
        23,3,4,2,0,21,23,3,6,3,0,22,20,1,0,0,0,22,21,1,0,0,0,23,3,1,0,0,
        0,24,25,5,6,0,0,25,26,5,1,0,0,26,27,3,6,3,0,27,5,1,0,0,0,28,32,5,
        5,0,0,29,32,5,6,0,0,30,32,3,8,4,0,31,28,1,0,0,0,31,29,1,0,0,0,31,
        30,1,0,0,0,32,7,1,0,0,0,33,34,5,6,0,0,34,35,5,2,0,0,35,36,3,10,5,
        0,36,37,5,3,0,0,37,9,1,0,0,0,38,43,3,6,3,0,39,40,5,4,0,0,40,42,3,
        6,3,0,41,39,1,0,0,0,42,45,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,
        11,1,0,0,0,45,43,1,0,0,0,4,15,22,31,43
    ]

class SimpleLangParser ( Parser ):

    grammarFileName = "SimpleLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "INT", "ID", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_expression = 3
    RULE_magicFunctionCall = 4
    RULE_parameters = 5

    ruleNames =  [ "program", "statement", "assignment", "expression", "magicFunctionCall", 
                   "parameters" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    INT=5
    ID=6
    WS=7

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
            return self.getToken(SimpleLangParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.StatementContext,i)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_program

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

        localctx = SimpleLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5 or _la==6:
                self.state = 12
                self.statement()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 18
            self.match(SimpleLangParser.EOF)
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

        def assignment(self):
            return self.getTypedRuleContext(SimpleLangParser.AssignmentContext,0)


        def expression(self):
            return self.getTypedRuleContext(SimpleLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_statement

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

        localctx = SimpleLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 22
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(SimpleLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = SimpleLangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(SimpleLangParser.ID)
            self.state = 25
            self.match(SimpleLangParser.T__0)
            self.state = 26
            self.expression()
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

        def INT(self):
            return self.getToken(SimpleLangParser.INT, 0)

        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)

        def magicFunctionCall(self):
            return self.getTypedRuleContext(SimpleLangParser.MagicFunctionCallContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_expression

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

        localctx = SimpleLangParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expression)
        try:
            self.state = 31
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.match(SimpleLangParser.INT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.match(SimpleLangParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 30
                self.magicFunctionCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MagicFunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)

        def parameters(self):
            return self.getTypedRuleContext(SimpleLangParser.ParametersContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_magicFunctionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMagicFunctionCall" ):
                listener.enterMagicFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMagicFunctionCall" ):
                listener.exitMagicFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMagicFunctionCall" ):
                return visitor.visitMagicFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def magicFunctionCall(self):

        localctx = SimpleLangParser.MagicFunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_magicFunctionCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(SimpleLangParser.ID)
            self.state = 34
            self.match(SimpleLangParser.T__1)
            self.state = 35
            self.parameters()
            self.state = 36
            self.match(SimpleLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ExpressionContext,i)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameters" ):
                return visitor.visitParameters(self)
            else:
                return visitor.visitChildren(self)




    def parameters(self):

        localctx = SimpleLangParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.expression()
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 39
                self.match(SimpleLangParser.T__3)
                self.state = 40
                self.expression()
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





