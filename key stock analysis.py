def p2b(assets, liabilities, price, shares):
    bookvalue = assets - liabilities
    bookvalue_pershare = bookvalue / shares
    x = price / bookvalue_pershare
    print(bookvalue, bookvalue_pershare, x)
    if x < 1:
        return print(f"Price/Earnings = {x}. \n Book Value = {bookvalue}. \n Book Value/Share = {bookvalue_pershare} \n"
                     f"Undervalued")
    elif x > 1:
        return print(f"Price/Earnings = {x}. \n Book Value = {bookvalue}. \n Book Value/Share = {bookvalue_pershare} \n"
                     f"Overvalued")
    else:
        return print(f"Price/Earnings = {x}. \n Book Value = {bookvalue}. \n Book Value/Share = {bookvalue_pershare} \n"
                     f"Equally Valued")


def eps(net_income, preferred_dividends, total_outstanding_shares):
    x = (net_income - preferred_dividends) / total_outstanding_shares
    return x


def eps_growth_rate(initial_eps, final_eps):
    x = ((final_eps - initial_eps) / initial_eps) * 100
    return x


def p2e(price, eps):
    x = price / eps
    if x <= 20:
        return print(f"Price to Earnings = {x} \n Lower value than average")
    else:
        return print(f"Price to earnings = {x} \n Higher value than average")


def d2e(debt, shareholder_equity):
    x = debt / shareholder_equity
    if x < 0.3:
        return print(f"Debt to Equity = {x} \n Very low debt, consider if industry is low growth")
    elif 0.3 < x < 2:
        return print(f"Debt to Equity = {x} \n Healthy mix of debt to equity")
    else:
        return print(f"Debt to Equity = {x} \n Higher than average debt, consider if industry has high fixed assets")


