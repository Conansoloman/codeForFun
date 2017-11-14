import pandas as pd

goog_df = pd.read_html('https://finance.google.com/finance/historical?q=GOOG')

print goog_df
