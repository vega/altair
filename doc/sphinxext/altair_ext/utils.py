import ast

def exec_then_eval(code, _globals=None, _locals=None):
    """Exec a code block & return evaluation of the last line"""
    # TODO: make this less brittle.
    _globals = _globals or {}
    _locals = _locals or {}

    block = ast.parse(code, mode='exec')
    last = ast.Expression(block.body.pop().value)

    exec(compile(block, '<string>', mode='exec'), _globals, _locals)
    return eval(compile(last, '<string>', mode='eval'), _globals, _locals)


def strip_vl_extension(filename):
    """Strip the vega-lite extension (either vl.json or json) from filename"""
    for ext in ['.vl.json', '.json']:
        if filename.endswith(ext):
            return filename[:-len(ext)]
    else:
        return filename
