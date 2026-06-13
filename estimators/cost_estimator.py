def estimate_cost(
    tokens,
    model_cost
):
    return (
        tokens / 1_000_000
    ) * model_cost