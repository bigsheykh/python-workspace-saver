from typing import List, Tuple, Set, Union
import ast
import os
import base64

test_cases = []

def test_case_creator(
    ids: List[str],
    ast_type: ast.stmt,
    test_case_common_body: List[ast.stmt],
    address: str
):
    test_case_body =  test_case_common_body + [ast_type]
    for id in ids:
        test_case_body.append(ast.Assert(test=ast.Compare(
            left=ast.Name(id=id),
            ops=[ast.Eq()],
            comparators=[ast.Subscript(
                value=ast.Name(id="after_shelf"),
                slice=ast.Constant(value=id)
            )]
        )))
    module = ast.Module(body=test_case_body, type_ignores=[])
    test_case_file = open(address, "w")
    test_case_file.write(ast.unparse(module))
    test_case_file.close()

def merge_expr_info(
    info1: Union[Tuple[bool, Set[str]], None],
    info2: Union[Tuple[bool, Set[str]], None]
) -> Tuple[bool, Set[str]]:
    if info1 == None:
        return info2 or (True, set())
    if info2 == None:
        return info1
    if info1[0] and info2[0]:
        return (True, info1[1].union(info2[1]))
    return (False, set())
    

def get_info_expr(ast_type):
    base = (True, set())
    if type(ast_type) in [ast.Lambda, ast.Await, ast.Yield, ast.YieldFrom, ast.IfExp,
                          ast.NamedExpr,
                          ast.ListComp, ast.SetComp, ast.GeneratorExp, ast.DictComp]:
        return (False, set())
    elif type(ast_type) in [ast.JoinedStr, ast.BoolOp, ast.Dict]:
        for value in ast_type.values:
            base = merge_expr_info(base, get_info_expr(value))
        return base
    elif type(ast_type) in [ast.Set, ast.List, ast.Tuple]:
        for value in ast_type.elts:
            base = merge_expr_info(base, get_info_expr(value))
        return base
    elif type(ast_type) == ast.BinOp:
        return merge_expr_info(get_info_expr(ast_type.left), get_info_expr(ast_type.right))
    elif type(ast_type) == ast.Subscript:
        return merge_expr_info(get_info_expr(ast_type.value), get_info_expr(ast_type.slice))
    elif type(ast_type) == ast.UnaryOp:
        return get_info_expr(ast_type.operand)
    elif type(ast_type) in [ast.FormattedValue ,ast.Attribute, ast.Starred, ast.keyword]:
        return get_info_expr(ast_type.value)
    elif type(ast_type) == ast.Constant or ast_type == None:
        return (True, set())
    elif type(ast_type) == ast.Slice:
        return merge_expr_info(
            merge_expr_info(get_info_expr(ast_type.lower), get_info_expr(ast_type.upper)),
            ast_type.step)
    elif type(ast_type) == ast.Compare:
        base = get_info_expr(ast_type.left)
        for value in ast_type.comparators:
            base = merge_expr_info(base, get_info_expr(value))
        return base
    elif type(ast_type) == ast.Name:
        return (True, set([ast_type.id]))
    elif type(ast_type) == ast.Call:
        base = get_info_expr(ast_type.func)
        for value in ast_type.args:
            base = merge_expr_info(base, get_info_expr(value))
        for keyword in ast_type.keywords:
            base = merge_expr_info(base, get_info_expr(keyword))
        return base  # do something later
    # print(ast.dump(ast_type, indent=4))
    raise Exception()


def create_save_workspace_call(
    names: Set[str], ast_type: ast.stmt, is_start: bool
) -> ast.stmt:
    dict_keys = []
    dict_values = []
    for name in names:
        dict_keys.append(ast.Constant(name))
        dict_values.append(ast.Name(id=name, ctx=ast.Load()))
    return ast.Expr(value=ast.Call(func=ast.Name(id="save_workspace"),
                    args=[ast.Constant(ast_type.lineno),
                          ast.Constant(is_start),
                          ast.Dict(keys=dict_keys, values=dict_values)],
                    keywords=[],
                    ))
    return None


def manipulate_assign_or_expr(ast_type: ast.stmt):
    expr_info = get_info_expr(ast_type.value)
    tar_info =  expr_info
    if type(ast_type) == ast.AugAssign or type(ast_type) == ast.AnnAssign:
        tar_info = merge_expr_info(get_info_expr(ast_type.target), tar_info)

    if type(ast_type) == ast.Assign:
        for target in ast_type.targets:
            tar_info = merge_expr_info(get_info_expr(target), tar_info)

    if not tar_info[0] or len(tar_info[1]) == 0:
        return [ast_type]

    test_cases.append({'lineno': ast_type.lineno, 'line': ast_type, 'ids': tar_info[1]})
    return [create_save_workspace_call(expr_info[1], ast_type, is_start=True),
            ast_type,
            create_save_workspace_call(tar_info[1], ast_type, is_start=False)
            ]


def manipulate_body(ast_body: List[ast.AST]) -> List[ast.AST]:
    new_body: List[ast.AST] = []

    for x in ast_body:
        manipulated = manipulate_stmt(x)
        if type(manipulated) == type([]):
            print(ast.unparse(x))
            new_body += manipulated
            # print(manipulated)
            print(ast.dump(manipulated[0], indent=4))
            print(ast.unparse(manipulated[0]))
        else:
            new_body.append(manipulated)
    return new_body


def manipulate_stmt(ast_type: ast.stmt):
    if type(ast_type) == ast.Match:
        for i in range(len(ast_type.cases)):
            manipulate_stmt(ast_type.cases[i])
        return ast_type

    if type(ast_type) in [ast.Assign, ast.Expr, ast.AugAssign, ast.AnnAssign]:
        return manipulate_assign_or_expr(ast_type)

    if hasattr(ast_type, "body"):
        ast_type.body = manipulate_body(ast_type.body)
        
    if hasattr(ast_type, "orelse"):
        ast_type.orelse = manipulate_body(ast_type.orelse)
    
    if type(ast_type) in [ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef,
                    ast.Module, ast.For, ast.AsyncFor, ast.While, ast.With,
                    ast.AsyncWith, ast.match_case, ast.Try, ast.TryStar,
                    ast.If, ast.IfExp] :
        
        return ast_type

    if type(ast_type) in [ast.Import, ast.ImportFrom, ast.Return, ast.Delete,
                   ast.Assert, ast.Raise, ast.Pass, ast.Continue, ast.Break,
                   ast.Global, ast.Nonlocal]:
        return ast_type

    print(type(ast_type))
    raise Exception()


file_name = "/home/amirreza/Documents/Sharif/last/trace_test/poe_ai_generated/first.py"
# file_name = "/home/amirreza/Documents/Sharif/last/trace_test/poe_ai_generated/third.py"
# file_name = "/home/amirreza/Documents/Sharif/last/trace_test/testing_ground/robotframework-master/src/robot/libdocpkg/consoleviewer.py"
# file_name = "/home/amirreza/Documents/Sharif/last/trace_test/testing_ground/import_shelve.py"
# file_name = "/home/amirreza/Documents/Sharif/last/trace_test/testing_ground/robotframework-master/src/robot/pythonpathsetter.py"
source = open(file_name).read()
a = ast.parse(source=source, filename=file_name, type_comments=True)
f1 = open("original.py", "w")
f1.write(ast.unparse(a))
f1.close()
workspace_file_name = "/home/amirreza/Documents/Sharif/last/trace_test/testing_ground/workspace-saver.py"

source_of_workspace = open(workspace_file_name).read()
workspace_body = ast.parse(source=source_of_workspace, filename=file_name, type_comments=True).body


new_a = manipulate_stmt(a)
new_a.body = workspace_body + new_a.body
ast.fix_missing_locations(new_a)
# new_a = manipulate(a)
f2 = open("new.py", "w")
# f2.write(ast.dump(new_a, indent=4))
f2.write(ast.unparse(new_a))
f2.close()



source_body = ast.parse(source=source, filename=file_name, type_comments=True).body

shelf_opener_file_name = "/home/amirreza/Documents/Sharif/last/trace_test/testing_ground/shelf-opener.py"

source_of_shelf_opener = open(shelf_opener_file_name).read()
shelf_opener_body = ast.parse(source=source_of_shelf_opener,
                              filename=shelf_opener_file_name,
                              type_comments=True).body

test_case_common_body = [stmt for stmt in source_body if type(stmt) in [
    ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef, ast.Import, ast.ImportFrom
]] + shelf_opener_body

source_address = os.path.abspath("new.py")

os.makedirs("/tmp/python-workspace/", exist_ok=True)
dir_name = base64.b64encode(source_address.encode()).decode()
os.makedirs(f"/tmp/python-workspace/{dir_name}", exist_ok=True)
for test_case in test_cases:
    line_number = test_case["lineno"]
    directory_address = f"/tmp/python-workspace/{dir_name}/{line_number}"
    os.makedirs(directory_address, exist_ok=True)
    test_case_creator(ids=test_case["ids"],
                      ast_type=test_case["line"],
                      test_case_common_body=test_case_common_body,
                      address=f"{directory_address}/test_case.py")

# f2 = open("old.py", "w")
# # f2.write(ast.dump(new_a, indent=4))
# f2.write(ast.unparse(a))
# f2.close()
