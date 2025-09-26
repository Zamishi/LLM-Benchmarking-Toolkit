from sympy import sympify, solve, Eq

def solve_expression(text):
    try:
        s = text.replace("^", "**")
        if "=" in s:
            lhs, rhs = s.split("=", 1)
            expr = Eq(sympify(lhs), sympify(rhs))
            sol = solve(expr)
        else:
            expr = sympify(s)
            sol = solve(expr)
        return sol
    except:
        return None
