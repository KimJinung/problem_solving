def solution(ineq, eq, n, m):
    if eq == "!":
        eq = ""

    formula = f"{n} {ineq}{eq} {m}"

    return 1 if eval(formula) else 0
