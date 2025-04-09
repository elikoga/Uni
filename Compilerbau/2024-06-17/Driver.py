import sys
from dataclasses import dataclass

from antlr4 import InputStream, CommonTokenStream
from SimpleLangLexer import SimpleLangLexer
from SimpleLangParser import SimpleLangParser
from SimpleLangVisitor import SimpleLangVisitor


@dataclass
class Program:
    statements: list["Statement"]


class Statement:
    pass


@dataclass
class Assignment(Statement):
    variable: str
    expression: "Expression"


class Expression(Statement):
    pass


@dataclass
class Int(Expression):
    value: int


@dataclass
class Variable(Expression):
    name: str


@dataclass
class MagicFunctionCall(Expression):
    function: str
    parameters: list[Expression]


class VisitorParser(SimpleLangVisitor):
    def visitProgram(self, ctx: SimpleLangParser.ProgramContext):
        statements = []
        for statement in ctx.statement():
            statements.append(self.visit(statement))
        return Program(statements)

    def visitAssignment(self, ctx: SimpleLangParser.AssignmentContext):
        variable = ctx.ID().getText()
        expression = self.visit(ctx.expression())
        return Assignment(variable, expression)

    def visitExpression(self, ctx: SimpleLangParser.ExpressionContext):
        if ctx.INT():
            return Int(int(ctx.INT().getText()))
        if ctx.ID():
            return Variable(ctx.ID().getText())
        return self.visit(ctx.magicFunctionCall())

    def visitMagicFunctionCall(self, ctx: SimpleLangParser.MagicFunctionCallContext):
        function = ctx.ID().getText()
        parameters = self.visit(ctx.parameters())
        return MagicFunctionCall(function, parameters)

    def visitParameters(self, ctx: SimpleLangParser.ParametersContext):
        parameters = []
        for expression in ctx.expression():
            parameters.append(self.visit(expression))
        return parameters


example_program = """
a = 1
b = 2
c = add(a, b)
sum = add(c, 3)
write(sum)
sum
2
abc = 5
"""


def main():
    input_stream = InputStream(example_program)
    lexer = SimpleLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SimpleLangParser(stream)
    tree = parser.program()
    visitor = VisitorParser()
    program = visitor.visit(tree)
    print(program)


if __name__ == "__main__":
    main()
