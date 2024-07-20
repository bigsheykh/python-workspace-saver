from typing import List, Tuple, Set, Union
import ast
import astunparse
file_name = "/home/amirreza/Documents/Sharif/last/trace_test/poe_ai_generated/first.py"
# file_name = "/home/amirreza/Documents/Sharif/last/trace_test/testing_ground/robotframework-master/src/robot/libdocpkg/consoleviewer.py"
# file_name = "/home/amirreza/Documents/Sharif/last/trace_test/testing_ground/import_shelve.py"
# file_name = "/home/amirreza/Documents/Sharif/last/trace_test/testing_ground/robotframework-master/src/robot/pythonpathsetter.py"
source = open(file_name).read()
a = ast.parse(source=source, filename=file_name, type_comments=True)
f1 = open("original.txt", "w")
f1.write(ast.unparse(a))
f1.close()
a.body.insert(0,ast.Import([ast.alias("workspace_saver")])) 

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
    extention_name: str = str(is_start) + "_" + str(ast_type.lineno)
    dict_keys = []
    dict_values = []
    for name in names:
        dict_keys.append(ast.Constant(name))
        dict_values.append(ast.Name(id=name, ctx=ast.Load()))
    return ast.Expr(value=ast.Call(func=ast.Name(id="save_workspace"),
                    args=[ast.Constant(extention_name), ast.Dict(keys=dict_keys, values=dict_values)],
                    keywords=[],
                    # lineno=ast_type.lineno + (1 if is_start else -1)
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

    # print(ast.dump(ast_type, indent=4))
    # print(ast.unparse(ast_type))
    # print(expr_info)
    # print(tar_info)
    # print()
    # print()
    if not tar_info[0] or len(tar_info[1]) == 0:
        return [ast_type]
    # return [ast_type]

    return [create_save_workspace_call(expr_info[1], ast_type, is_start=False),
            ast_type,
            create_save_workspace_call(tar_info[1], ast_type, is_start=True)
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



    # print(ast.dump(x))
new_a = manipulate_stmt(a)
ast.fix_missing_locations(new_a)
# new_a = manipulate(a)
f2 = open("new.txt", "w")
# f2.write(ast.dump(new_a, indent=4))
f2.write(ast.unparse(new_a))
f2.close()

# f2 = open("old.txt", "w")
# # f2.write(ast.dump(new_a, indent=4))
# f2.write(ast.unparse(a))
# f2.close()
