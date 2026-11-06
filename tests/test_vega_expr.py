from tools.vega_expr import RAW, SOFTBREAK, TEXT, TYPE, VegaExprDef


def test_split_signature_tokens_handles_embedded_open_bracket() -> None:
    expr_def = VegaExprDef("quantileUniform", ())

    tokens = expr_def._split_markers("probability[")

    assert list(tokens) == ["probability", "["]


def test_parameters_handle_mistune_3_3_signature_tokens() -> None:
    expr_def = VegaExprDef(
        "quantileUniform",
        (
            {TYPE: SOFTBREAK},
            {TYPE: TEXT, RAW: "quantileUniform"},
            {TYPE: TEXT, RAW: "(probability[, "},
            {TYPE: TEXT, RAW: "min"},
            {TYPE: TEXT, RAW: ", "},
            {TYPE: TEXT, RAW: "max"},
            {TYPE: TEXT, RAW: "]) "},
            {TYPE: SOFTBREAK},
        ),
    ).with_parameters()

    assert [(p.name, p.required) for p in expr_def.parameters] == [
        ("probability", True),
        ("min", False),
        ("max", False),
    ]
