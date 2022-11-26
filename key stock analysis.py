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


def finder(container):
    import re
    str(container)
    # Define the empty lists and dictionary for use
    x = 0
    y = 0
    value_list = []
    title_list = []
    title_val = {}

    # While loop based off of 'title' variable so iterates until it gets to final title. Values always come after title.
    last_instance = container.rfind("title=")
    while x < last_instance:
        search_point = container[x:]
        # Find the first title and then isolate the actual 'title' using splice and regex
        title_loc = search_point.find("title=")
        title = search_point[title_loc:(title_loc + 75)]
        # Regex function is simple but the specificity in the splice allows it to be so, thus easier to read
        title = (re.findall(r'"(.*?)"', title))
        # The only failure in the simple regex is getting 'Va(m)' put into the list.
        if 'Va(m)' in title:
            title.pop()
        # Depending on the length of the title itself sometimes the regex will grab it again due to Yahoo making it a
        # button on the finance statement. EXPERIMENT WITH .SEARCH() FUNCTION!!
        if len(title) > 1:
            title.pop()
        title_list.extend(title)

        # Repeat the process to get the value that comes after the title. Need to find a way to get ALL variables
        # following the title (the year after year). Expanding the search_point would be a place to start.
        val_loc = search_point.find('data-test="fin-col"')
        val = search_point[val_loc:(val_loc + 80)]
        val = re.findall(r"<span>(.*?)</span>", val)
        # If the value is empty there will literally be nothing in the html so needs a placeholder for dict to work
        # correctly
        if len(val) < 1:
            val.extend('-')
        value_list.extend(val)
        # 1,000 here isn't arbitrary, it is approx the minimum to get past the "fin-col" values
        x = x + (title_loc + 1000)

    # Creating the dict would be fewer lines with a pop function but this method keeps the lists intact.
    # Value list here is arbitrary.
    for i in value_list:
        title_val[title_list[y]] = value_list[y]
        y += 1
    return title_val

