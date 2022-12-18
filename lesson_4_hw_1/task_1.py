order = list(map(lambda x: (x[0], round(x[-1] * x[-2] + 10, 2)) if x[-1] * x[-2] < 100 else (x[0], round(x[-1] * x[-2], 2)), data))
