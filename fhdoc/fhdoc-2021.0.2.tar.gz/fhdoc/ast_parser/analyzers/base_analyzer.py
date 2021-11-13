"""
Base AST analyzer.
"""
import ast
from typing import TYPE_CHECKING, List, Text

if TYPE_CHECKING:  # pragma: no cover
	from fhdoc.ast_parser.node_records.argument_record import (
		ArgumentRecord,
		ExpressionRecord,
	)
	from fhdoc.ast_parser.node_records.attribute_record import AttributeRecord
	from fhdoc.ast_parser.node_records.class_record import ClassRecord
	from fhdoc.ast_parser.node_records.function_record import FunctionRecord
	from fhdoc.ast_parser.node_records.import_record import ImportRecord


class BaseAnalyzer(ast.NodeVisitor):
	"""
	Base AST analyzer.

	Has lists for all objects for different analyzers.
	"""

	def __init__(self):
		# type: () -> None
		self.related_names = []  # type: List[Text]
