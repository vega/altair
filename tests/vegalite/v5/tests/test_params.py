"""Tests for variable parameters and selection parameters"""

import pandas as pd

import altair.vegalite.v5 as alt


def test_variable_param():
    data = pd.DataFrame([{"a": "A", "b": 28}])

    rad_slider = alt.binding_range(min=0, max=20, step=1)
    rad_var = alt.param(bind=rad_slider, value=0, name="paramName")

    c = (
        alt.Chart(data)
        .mark_bar(cornerRadius=rad_var)
        .encode(
            x="a:N",
            y="b:Q",
        )
        .add_params(rad_var)
    )

    dct = c.to_dict()

    mark_dict = {"type": "bar", "cornerRadius": {"expr": "paramName"}}
    param_list = [
        {
            "name": "paramName",
            "bind": {"input": "range", "max": 20, "min": 0, "step": 1},
            "value": 0,
        }
    ]

    assert dct["mark"] == mark_dict
    assert dct["params"] == param_list


def test_param_expr():
    height_var = alt.param(name="height")
    inner_var = height_var / 2
    tick_var = (3 * height_var) / 4

    inner_str = inner_var._to_expr().replace(" ", "")
    inner_ans = "(height/2)"

    tick_str = tick_var._to_expr().replace(" ", "")
    tick_ans = "((3*height)/4)"

    assert height_var._to_expr() == "height"
    assert inner_str == inner_ans
    assert tick_str == tick_ans

    data = pd.DataFrame({"r1": [310, 0], "r2": [270, 0], "r3": [125, 225]})

    c1 = alt.Chart(data).mark_bar(size=height_var).encode(x="r1")

    c2 = alt.Chart(data).mark_bar(size=inner_var).encode(x="r2")

    c3 = alt.Chart(data).mark_tick(size=tick_var).encode(x="r3")

    c = (c1 + c2 + c3).add_params(height_var)

    dct = c.to_dict()

    ans_set = {v._to_expr() for v in [height_var, inner_var, tick_var]}
    expr_set = {d["mark"]["size"]["expr"] for d in dct["layer"]}

    assert ans_set == expr_set
