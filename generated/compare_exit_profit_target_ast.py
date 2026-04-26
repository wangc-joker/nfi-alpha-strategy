import ast
from pathlib import Path

orig_path = Path('/host/NostalgiaForInfinity/NostalgiaForInfinityX7.py')
new_path = Path('/host/nfi-alpha-strategy/strategies/nfi_refactor/exits/profit_target.py')

orig_tree = ast.parse(orig_path.read_text(encoding='utf-8'))
new_tree = ast.parse(new_path.read_text(encoding='utf-8'))

class_func = None
for node in ast.walk(orig_tree):
    if isinstance(node, ast.ClassDef) and node.name == 'NostalgiaForInfinityX7':
        for item in node.body:
            if isinstance(item, ast.FunctionDef) and item.name == 'exit_profit_target':
                class_func = item
                break

new_func = None
for node in new_tree.body:
    if isinstance(node, ast.FunctionDef) and node.name == 'exit_profit_target':
        new_func = node
        break

if class_func is None or new_func is None:
    raise SystemExit('missing function')

class Normalize(ast.NodeTransformer):
    def visit_arg(self, node):
        if node.arg in {'self', 'strategy'}:
            node.arg = 'S'
        node.annotation = None
        return node
    def visit_Name(self, node):
        if node.id in {'self', 'strategy'}:
            node.id = 'S'
        return node
    def visit_Attribute(self, node):
        self.generic_visit(node)
        return node
    def visit_FunctionDef(self, node):
        node.returns = None
        self.generic_visit(node)
        return node

for f in (class_func, new_func):
    for n in ast.walk(f):
        for attr in ('lineno','col_offset','end_lineno','end_col_offset'):
            if hasattr(n, attr):
                setattr(n, attr, None)

norm_orig = Normalize().visit(class_func)
norm_new = Normalize().visit(new_func)
ast.fix_missing_locations(norm_orig)
ast.fix_missing_locations(norm_new)

orig_dump = ast.dump(norm_orig, include_attributes=False)
new_dump = ast.dump(norm_new, include_attributes=False)
print('AST_EQUAL=', orig_dump == new_dump)
print('ORIG_ARGS=', [a.arg for a in norm_orig.args.args])
print('NEW_ARGS=', [a.arg for a in norm_new.args.args])
if orig_dump != new_dump:
    import difflib
    for line in difflib.unified_diff(orig_dump.splitlines(), new_dump.splitlines(), lineterm='', n=1):
        print(line[:500])
        break
