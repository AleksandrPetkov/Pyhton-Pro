get_order_tuple = lambda data: list(map(tuple, [[x[0], round(x[-1] * x[-2] + 10, 2)] if x[-1] * x[-2] < 100 else [x[0], round(x[-1] * x[-2], 2)] for x in data]))
