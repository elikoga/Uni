import abc
from dataclasses import dataclass
from typing import Literal, Union

from .LangLexer import LangLexer
from .LangParser import LangParser
from .LangVisitor import LangVisitor


@dataclass
class Program:
    statements: list["Statement"]


class Statement(abc.ABC):
    pass


@dataclass
class LetStatement(Statement):
    variable: str
    type: str
    expression: "Expression"


@dataclass
class Block:
    statements: list[Statement]
    expression: Union["Expression", None]


@dataclass
class LoopExpression(Statement):
    block: Block

@dataclass
class WhileExpression(Statement):
    condition: "Expression"
    block: Block

@dataclass
class IfExpression(Statement):
    condition: "Expression"
    block: Block
    else_block: Block | None


class Expression(Statement):
    pass


@dataclass
class LiteralExpression(Expression):
    value: int | float | str | bool


@dataclass
class VariableExpression(Expression):
    name: str


@dataclass
class FunctionCallExpression(Expression):
    function: str
    parameters: list[Expression]


@dataclass
class NegationExpression(Expression):
    operator: Literal["!", "-"]
    expression: Expression

@dataclass
class BreakExpression(Expression):
    pass


@dataclass
class MathOperatorExpression(Expression):
    operator: Literal["+", "-", "*", "/", "%", "**"]
    left: Expression
    right: Expression


@dataclass
class ComparisonOperatorExpression(Expression):
    operator: Literal["==", "!=", "<", "<=", ">", ">="]
    left: Expression
    right: Expression


@dataclass
class LogicalOperatorExpression(Expression):
    operator: Literal["&&", "||"]
    left: Expression
    right: Expression


@dataclass
class AssignmentOperatorExpression(Expression):
    operator: Literal["=", "+=", "-=", "*=", "/=", "%="]
    left: VariableExpression
    right: Expression


class ASTBuilder(LangVisitor):
    def visitProgram(self, ctx: LangParser.ProgramContext):
        # statements = [self.visit(statement) for statement in ctx.statement()]
        statements = []
        for statement in ctx.statement():
            print(f"{statement=}")
            print(f"{self.visit(statement)=}")
            if isinstance(statement.children[0], LangParser.CommentContext):
                continue
            statements.append(self.visit(statement))
        return Program(statements)

    def visitLet_statement(self, ctx: LangParser.Let_statementContext):
        variable = ctx.IDENTIFIER_LOWERCASE_START().getText()
        type_ = ctx.type_().getText()
        expression = self.visit(ctx.expression_without_block())
        return LetStatement(variable, type_, expression)

    def visitBlock_expression(self, ctx: LangParser.Block_expressionContext):
        statements = [self.visit(statement) for statement in ctx.statement()]
        # expression = self.visit(ctx.expression_without_block())
        expression = (
            self.visit(ctx.expression_without_block())
            if ctx.expression_without_block()
            else None
        )
        return Block(statements, expression)

    def visitLoop_expression(self, ctx: LangParser.Loop_expressionContext):
        block = self.visit(ctx.block_expression())
        return LoopExpression(block)

    def visitWhile_expression(self, ctx: LangParser.While_expressionContext):
        condition = self.visit(ctx.expression_without_block())
        block = self.visit(ctx.block_expression())
        return WhileExpression(condition, block)

    def visitIf_expression(self, ctx: LangParser.If_expressionContext):
        condition = self.visit(ctx.expression())
        block = self.visit(ctx.block_expression(0))
        else_block = self.visit(ctx.block_expression(1)) if ctx.ELSE() else None
        return IfExpression(condition, block, else_block)

    def visitLiteral_expression(self, ctx: LangParser.Literal_expressionContext):
        value = ctx.INTEGER() and int(ctx.INTEGER().getText())
        value = (ctx.FLOAT() and float(ctx.FLOAT().getText())) or value
        value = (ctx.STRING() and ctx.STRING().getText()) or value
        value = (ctx.BOOLEAN() and ctx.BOOLEAN().getText() == "true") or value
        return LiteralExpression(value)

    def visitVariable_expression(self, ctx: LangParser.Variable_expressionContext):
        return VariableExpression(ctx.IDENTIFIER_LOWERCASE_START().getText())

    def visitStatement(self, ctx: LangParser.StatementContext):
        print(f"{ctx.children[0]=}")
        ret = super().visitStatement(ctx)
        print(f"cc{ret=}")
        return ret

    def visitExpression_statement(self, ctx: LangParser.Expression_statementContext):
        print(f"bb{ctx.children[0]=}")
        # ret = self.visitChildren(ctx)
        ret = self.visit(ctx.children[0])
        print(f"bb{ret=}")
        return ret

    def visitFunction_call_expression(
        self, ctx: LangParser.Function_call_expressionContext
    ):
        function = ctx.IDENTIFIER_LOWERCASE_START().getText()
        parameters = [self.visit(expression) for expression in ctx.expression()]
        fc = FunctionCallExpression(function, parameters)
        print(f"{fc=}")
        return fc
        return FunctionCallExpression(function, parameters)

    def visitNegation_expression(self, ctx: LangParser.Negation_expressionContext):
        operator = ctx.getChild(0).getText()
        expression = self.visit(ctx.expression())
        return NegationExpression(operator, expression)

    def visitExpression_without_block(
        self, ctx: LangParser.Expression_without_blockContext
    ):
        print(f"{ctx.children=}")
        # if only one child, return it
        if len(ctx.children) == 1:
            print(f"aa{ctx.getChild(0)=}")
            ret = self.visit(ctx.getChild(0))
            print(f"aa{ret=}")
            return ret
        print(f"DD{ctx.children=}")

        if ctx.math_operator():
            left = self.visit(ctx.expression_without_block(0))
            right = self.visit(ctx.expression_without_block(1))
            operator = ctx.math_operator().getText()
            return MathOperatorExpression(operator, left, right)
        if ctx.comparison_operator():
            left = self.visit(ctx.expression_without_block(0))
            right = self.visit(ctx.expression_without_block(1))
            operator = ctx.comparison_operator().getText()
            return ComparisonOperatorExpression(operator, left, right)
        if ctx.logical_operator():
            left = self.visit(ctx.expression_without_block(0))
            right = self.visit(ctx.expression_without_block(1))
            operator = ctx.logical_operator().getText()
            return LogicalOperatorExpression(operator, left, right)
        if ctx.assignment_operator():
            left = self.visit(ctx.variable_expression())
            right = self.visit(ctx.expression_without_block(0))
            operator = ctx.assignment_operator().getText()
            return AssignmentOperatorExpression(operator, left, right)
        raise RuntimeError("Unknown expression type")

    def visitGrouped_expression(self, ctx: LangParser.Grouped_expressionContext):
        return self.visit(ctx.expression())

    def visitBreak_expression(self, ctx: LangParser.Break_expressionContext):
        return BreakExpression()


GAMEBOY_FRAMEWORK_PATH = "/home/elikoga/Dev/Uni/Compilerbau/Assembler/framework.asm"


class GameBoyAssembly:
    def __init__(self):
        self.instructions = []

    def add_instruction(self, instruction):
        self.instructions.append(instruction)

    def __str__(self):
        # return '\n'.join(self.instructions)
        # gameboy assembly needs a header
        return f"""
.include "{GAMEBOY_FRAMEWORK_PATH}"
.section "main"
main:
""" + '\n'.join(self.instructions) + """
.ends
        """


@dataclass
class Symbol:
    name: str
    type: str
    next_symbol: Union["Symbol", None] = None
    shadowed_symbol: Union["Symbol", None] = None

class MagicFunction:
    """
    ======= CALLING CONVENTION =======
Arguments must be passed via registers in the following order:
8-bit arguments: A, C, B, E, D, L, H
16-bit arguments: HL, DE, BC

The result of a procedure can be found in the following register:
8-bit result: A
16-bit result: HL

The contents of register A and all registers passed as arguments might get destroyed by the procedure being called.
All other registers are guaranteed to be the same after the call.
"""
    def __init__(self, name, parameters):
        self.name = name
        self.parameters = parameters

MAGIC_FUNCTIONS = {
    "printByte": MagicFunction("printByte", ["A"]),
    "printSignedByte": MagicFunction("printSignedByte", ["A"]),
    "printBCD": MagicFunction("printBCD", ["A"]),
    "printWord": MagicFunction("printWord", ["HL"]),
    "printSignedWord": MagicFunction("printSignedWord", ["HL"]),
    "printChar": MagicFunction("printChar", ["A"]),
    "printBool": MagicFunction("printBool", ["A"]),
    "printString": MagicFunction("printString", ["HL"]),
    "printStringLn": MagicFunction("printStringLn", ["HL"]),
    "printByteArray": MagicFunction("printByteArray", ["HL", "BC"]),
    "printSignedByteArray": MagicFunction("printSignedByteArray", ["HL", "BC"]),
    "printBCDarray": MagicFunction("printBCDarray", ["HL", "BC"]),
    "printWordArray": MagicFunction("printWordArray", ["HL", "BC"]),
    "printSignedWordArray": MagicFunction("printSignedWordArray", ["HL", "BC"]),
    "printCharArray": MagicFunction("printCharArray", ["HL", "BC"]),
    "printBoolArray": MagicFunction("printBoolArray", ["HL", "BC"]),
    "printFixed": MagicFunction("printFixed", ["HL"]),
    "printFixedArray": MagicFunction("printFixedArray", ["HL", "BC"]),

    "setTile": MagicFunction("setTile", ["A", "C", "B"]),
}

class SymbolTable:
    def __init__(self):
        self.identifiers = {}  # name -> numeric id
        self.curr_nesting_level = 0
        self.symbols_by_id = {}  # numeric id -> Symbol
        self.symbols_by_nl = {}  # nesting level -> Symbol
        self.stack_offsets = [{}]  # list of (id -> offset) mappings

    def open_scope(self):
        self.curr_nesting_level += 1
        self.stack_offsets.append({})
        self.symbols_by_nl[self.curr_nesting_level] = None

    def close_scope(self):
        while self.symbols_by_nl[self.curr_nesting_level]:
            # remove reference to symbol from identifiers
            symbol = self.symbols_by_nl[self.curr_nesting_level]
            symbol_id = self.identifiers[symbol.name]
            self.symbols_by_id[symbol_id] = symbol.shadowed_symbol
            self.symbols_by_nl[self.curr_nesting_level] = symbol.next_symbol
        self.curr_nesting_level -= 1
        # get sum of stack offsets
        stack_offset = 0
        for offset in self.stack_offsets[-1].values():
            stack_offset += offset
        self.stack_offsets.pop()
        return stack_offset

    def enter_symbol(self, name, symbol_type):
        symbol = Symbol(name, symbol_type)
        if not name in self.identifiers:
            self.identifiers[name] = len(self.identifiers)
        symbol_id = self.identifiers[name]
        # walk through linked list of symbols at nesting level
        if self.curr_nesting_level not in self.symbols_by_nl:
            self.symbols_by_nl[self.curr_nesting_level] = symbol
        else:
            pre_symbol = self.symbols_by_nl[self.curr_nesting_level]
            should_insert = True
            while pre_symbol:
                if not pre_symbol.next_symbol:
                    # check if pre_symbol is before or after the new symbol
                    if self.identifiers[pre_symbol.name] < symbol_id:
                        break # normal case
                    if self.identifiers[pre_symbol.name] == symbol_id:
                        raise ValueError(
                            f"Symbol with name {name} already exists in current scope at nesting level {self.curr_nesting_level}"
                        )
                    symbol.next_symbol = pre_symbol
                    self.symbols_by_nl[self.curr_nesting_level] = symbol
                    should_insert = False
                    break
                next_symbol = pre_symbol.next_symbol
                # search for the right id to insert the symbol
                if self.identifiers[next_symbol.name] == symbol_id:
                    raise ValueError(
                        f"Symbol with name {name} already exists in current scope at nesting level {self.curr_nesting_level}"
                    )
                if self.identifiers[next_symbol.name] > symbol_id:
                    break
                if not next_symbol:
                    break
                pre_symbol = next_symbol
            else:
                self.symbols_by_nl[self.curr_nesting_level] = symbol
                should_insert = False
            # insert symbol
            if should_insert:
                symbol.next_symbol = pre_symbol.next_symbol
                pre_symbol.next_symbol = symbol
        # now: insert symbol into symbols_by_id
        if symbol_id in self.symbols_by_id:
            symbol.shadowed_symbol = self.symbols_by_id[symbol_id]
        self.symbols_by_id[symbol_id] = symbol

        self.stack_offsets[-1][symbol_id] = len(self.stack_offsets[-1])

    def lookup_symbol(self, name):
        if name in self.identifiers:
            symbol_id = self.identifiers[name]

            # find which nesting level the symbol is in
            for nl in range(self.curr_nesting_level, -1, -1):
                def find_symbol():
                    s = self.symbols_by_nl[nl]
                    while s:
                        if s.name == name:
                            return s
                        s = s.next_symbol
                    return None
                symbol = find_symbol()
                if symbol:
                    assert symbol is self.symbols_by_id[symbol_id]
                    # collect all higher stack offsets
                    so = 0
                    for i in range(self.curr_nesting_level, nl, -1):
                        so += sum(self.stack_offsets[i].values())
                    return symbol, self.stack_offsets[nl][symbol_id] + so
        return None

    def current_nl_stack_size(self):
        return len(self.stack_offsets[-1])

    def create_new_name(self):
        idx = len(self.identifiers)
        while f"tmp_{idx}" in self.identifiers:
            idx += 1
        print(f"Creating new name tmp_{idx}")
        return f"tmp_{idx}"

@dataclass
class Type:
    size: int

DEFAULT_TYPE_TABLE = {
    "Byte": Type(1),
}

class GameBoyAssemblyGenerator:
    def __init__(self, ast: Program, type_table = DEFAULT_TYPE_TABLE, symbol_table = SymbolTable()):
        self.ast = ast
        self.gameboy_assembly = GameBoyAssembly()
        self.symbol_table = symbol_table
        self.type_table = type_table
        self.label_counter = 0
        self.loop_label_stack = []

    def new_label(self):
        self.label_counter += 1
        return f"LABEL_{self.label_counter}"

    def generate(self):
        print(f"Generating assembly for {self.ast}")
        self.visit(self.ast)
        return self.gameboy_assembly

    def visit(self, node):
        if isinstance(node, Program):
            return self.visit_program(node)
        if isinstance(node, LetStatement):
            return self.visit_let_statement(node)
        if isinstance(node, Block):
            return self.visit_block(node)
        if isinstance(node, LoopExpression):
            return self.visit_loop_expression(node)
        if isinstance(node, WhileExpression):
            return self.visit_while_expression(node)
        if isinstance(node, IfExpression):
            return self.visit_if_expression(node)
        if isinstance(node, LiteralExpression):
            return self.visit_literal_expression(node)
        if isinstance(node, VariableExpression):
            return self.visit_variable_expression(node)
        if isinstance(node, FunctionCallExpression):
            return self.visit_function_call_expression(node)
        if isinstance(node, NegationExpression):
            return self.visit_negation_expression(node)
        if isinstance(node, BreakExpression):
            return self.visit_break_expression(node)
        if isinstance(node, MathOperatorExpression):
            return self.visit_math_operator_expression(node)
        if isinstance(node, ComparisonOperatorExpression):
            return self.visit_comparison_operator_expression(node)
        if isinstance(node, LogicalOperatorExpression):
            return self.visit_logical_operator_expression(node)
        if isinstance(node, AssignmentOperatorExpression):
            return self.visit_assignment_operator_expression(node)
        raise RuntimeError(f"Node type {type(node)} not supported")

    def visit_program(self, node: Program):
        for statement in node.statements:
            print(f"Visiting statement {statement}")
            self.visit(statement)

    def visit_let_statement(self, node: LetStatement):
        self.symbol_table.enter_symbol(node.variable, node.type)
        # look up size of type in type table and allocate space on stack
        symbol_type = self.type_table[node.type]
        self.gameboy_assembly.add_instruction(f"add SP, -{symbol_type.size}")
        self.evaluate_expression_and_store_in_variable(node.variable, node.expression)

    def evaluate_expression_and_store_in_variable(
        self, variable: str, expression: Expression
    ):
        if isinstance(expression, LiteralExpression):
            self.gameboy_assembly.add_instruction(f"ld a, {expression.value}")
            self.gameboy_assembly.add_instruction(
                f"ld HL, {self.get_variable_name(variable)}"
            )
            self.gameboy_assembly.add_instruction(
                f"ld (HL), a"
            )
        elif isinstance(expression, VariableExpression):
            self.gameboy_assembly.add_instruction(f"ld HL, {self.get_variable_name(expression.name)}")
            self.gameboy_assembly.add_instruction(f"ld a, (HL)")
            self.gameboy_assembly.add_instruction(
                f"ld HL, {self.get_variable_name(variable)}"
            )
            self.gameboy_assembly.add_instruction(
                f"ld (HL), a"
            )
        elif isinstance(expression, MathOperatorExpression):
            # get new symbols for left and right
            left_name = self.symbol_table.create_new_name()
            self.symbol_table.enter_symbol(left_name, "Byte")
            self.gameboy_assembly.add_instruction(f"add SP, -1")
            self.evaluate_expression_and_store_in_variable(left_name, expression.left)
            right_name = self.symbol_table.create_new_name()
            self.symbol_table.enter_symbol(right_name, "Byte")
            self.gameboy_assembly.add_instruction(f"add SP, -1")
            self.evaluate_expression_and_store_in_variable(right_name, expression.right)
            # perform operation
            if expression.operator == "+":
                self.gameboy_assembly.add_instruction(
                    f"ld HL, {self.get_variable_name(left_name)}"
                )
                self.gameboy_assembly.add_instruction(
                    f"ld a, (HL)"
                )
                self.gameboy_assembly.add_instruction(
                    f"ld HL, {self.get_variable_name(right_name)}"
                )
                self.gameboy_assembly.add_instruction(
                    f"add a, (HL)"
                )
                self.gameboy_assembly.add_instruction(
                    f"ld HL, {self.get_variable_name(variable)}"
                )
                self.gameboy_assembly.add_instruction(
                    f"ld (HL), a"
                )

        else:
            raise RuntimeError(f"Expression type {type(expression)} not supported")

    def get_variable_name(self, variable):
        # looks at the symbol table to find the right position in the stack
        r = self.symbol_table.lookup_symbol(variable)
        if not r:
            raise RuntimeError(f"Variable {variable} not found")
        symbol, offset = r
        inv_offset = self.symbol_table.current_nl_stack_size() - offset - 1
        if inv_offset == 0:
            return "SP+0"
        return f"SP+{inv_offset}"

    def visit_block(self, node):
        self.symbol_table.open_scope()
        for statement in node.statements:
            self.visit(statement)
        so = self.symbol_table.close_scope()
        self.gameboy_assembly.add_instruction(f"add SP, {so}")

    def visit_loop_expression(self, node: LoopExpression):
        label = self.new_label()
        end_label = self.new_label()
        self.loop_label_stack.append(end_label)
        self.gameboy_assembly.add_instruction(f"{label}:")
        self.visit(node.block)
        self.gameboy_assembly.add_instruction(f"jp {label}")
        self.gameboy_assembly.add_instruction(f"{end_label}:")
        self.loop_label_stack.pop()


    def visit_break_expression(self, node: BreakExpression):
        if not self.loop_label_stack:
            raise RuntimeError("Break statement outside of loop")
        self.gameboy_assembly.add_instruction(f"jp {self.loop_label_stack[-1]}")


    def visit_if_expression(self, node):
        # evaluate condition
        self.evaluate_expression_and_store_in_register(node.condition, "A")
        # if false, jump to else block
        if node.else_block:
            else_label = self.new_label()
            end_label = self.new_label()
            self.gameboy_assembly.add_instruction(f"cp 0")
            self.gameboy_assembly.add_instruction(f"jr Z, {else_label}")
            self.symbol_table.open_scope()
            self.visit(node.block)
            so = self.symbol_table.close_scope()
            self.gameboy_assembly.add_instruction(f"add SP, {so}")
            self.gameboy_assembly.add_instruction(f"jr {end_label}")
            self.gameboy_assembly.add_instruction(f"{else_label}:")
            self.symbol_table.open_scope()
            self.visit(node.else_block)
            so = self.symbol_table.close_scope()
            self.gameboy_assembly.add_instruction(f"add SP, {so}")
            self.gameboy_assembly.add_instruction(f"{end_label}:")
        else:
            end_label = self.new_label()
            self.gameboy_assembly.add_instruction(f"cp 0")
            self.gameboy_assembly.add_instruction(f"jr Z, {end_label}")
            self.symbol_table.open_scope()
            self.visit(node.block)
            so = self.symbol_table.close_scope()
            self.gameboy_assembly.add_instruction(f"add SP, {so}")
            self.gameboy_assembly.add_instruction(f"{end_label}:")

    def visit_literal_expression(self, node):
        raise NotImplementedError

    def visit_variable_expression(self, node):
        raise NotImplementedError

    def visit_function_call_expression(self, node):
        # for all parameters, evaluate and store in registers
        magic_function = MAGIC_FUNCTIONS[node.function]
        for i, parameter in enumerate(node.parameters):
            self.evaluate_expression_and_store_in_register(parameter, magic_function.parameters[i])
        # call function
        self.gameboy_assembly.add_instruction(f"call {magic_function.name}")

    def evaluate_expression_and_store_in_register(self, expression, register):
        if isinstance(expression, LiteralExpression):
            self.gameboy_assembly.add_instruction(f"ld a, {expression.value}")
            self.gameboy_assembly.add_instruction(f"ld {register}, a")
        elif isinstance(expression, VariableExpression):
            self.gameboy_assembly.add_instruction(f"ld HL, {self.get_variable_name(expression.name)}")
            self.gameboy_assembly.add_instruction(f"ld a, (HL)")
            self.gameboy_assembly.add_instruction(f"ld {register}, a")
        elif isinstance(expression, ComparisonOperatorExpression):
            # get new symbols for left and right
            left_name = self.symbol_table.create_new_name()
            self.symbol_table.enter_symbol(left_name, "Byte")
            self.gameboy_assembly.add_instruction(f"add SP, -1")
            self.evaluate_expression_and_store_in_variable(left_name, expression.left)
            right_name = self.symbol_table.create_new_name()
            self.symbol_table.enter_symbol(right_name, "Byte")
            self.gameboy_assembly.add_instruction(f"add SP, -1")
            self.evaluate_expression_and_store_in_variable(right_name, expression.right)
            # perform operation
            if expression.operator == "==":
                self.gameboy_assembly.add_instruction(
                    f"ld HL, {self.get_variable_name(left_name)}"
                )
                self.gameboy_assembly.add_instruction(
                    f"ld a, (HL)"
                )
                self.gameboy_assembly.add_instruction(
                    f"ld HL, {self.get_variable_name(right_name)}"
                )
                self.gameboy_assembly.add_instruction(
                    f"cp (HL)"
                )
                # now: if Z is set, the values are equal
                # using jr Z, label
                same_label = self.new_label()
                end_label = self.new_label()
                self.gameboy_assembly.add_instruction(f"jr Z, {same_label}")
                self.gameboy_assembly.add_instruction(f"ld {register}, 0")
                self.gameboy_assembly.add_instruction(f"jr {end_label}")
                self.gameboy_assembly.add_instruction(f"{same_label}:")
                self.gameboy_assembly.add_instruction(f"ld {register}, 1")
                self.gameboy_assembly.add_instruction(f"{end_label}:")
        else:
            raise RuntimeError(f"Expression type {type(expression)} not supported")

    def visit_negation_expression(self, node):
        raise NotImplementedError

    def visit_math_operator_expression(self, node):
        raise NotImplementedError

    def visit_comparison_operator_expression(self, node):
        raise NotImplementedError

    def visit_logical_operator_expression(self, node):
        raise NotImplementedError

    def visit_assignment_operator_expression(self, node: AssignmentOperatorExpression):
        self.evaluate_expression_and_store_in_variable(node.left.name, node.right)

    def visit_while_expression(self, node: WhileExpression):
        # transform node from while condition block to loop { if condition break block }
        new_node = LoopExpression(
            Block(
                statements=[
                    IfExpression(
                        condition=node.condition,
                        block=Block(
                            statements=[
                                BreakExpression()
                            ],
                            expression=None
                        ),
                        else_block=None
                    )
                ]+node.block.statements,
                expression=None
            )
        )
        self.visit(new_node)