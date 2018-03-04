import ast


def exec_then_eval(code, namespace=None):
    """Exec a code block & return evaluation of the last line"""
    # TODO: make this less brittle.
    if namespace is None:
        namespace or {}

    block = ast.parse(code, mode='exec')
    last = ast.Expression(block.body.pop().value)

    exec(compile(block, '<string>', mode='exec'), namespace)
    return eval(compile(last, '<string>', mode='eval'), namespace)
