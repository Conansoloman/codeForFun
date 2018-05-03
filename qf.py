# import pandas as pd
#
# goog_df = pd.read_html('https://finance.google.com/finance/historical?q=GOOG')
#
# print goog_df


# def f(x, act=None):
#     if act is not None:
#         return act(x)
#     else:
#         return x
#
#
# def add(x):
#     return x + x
#
#
# print(f(2))
# print(f(2, act=add))


class A:
    def __init__(self):
        self.a = 5

class B(A):
    def __init__(self):
        A.__init__(self)

a = B()
print(a.a)
