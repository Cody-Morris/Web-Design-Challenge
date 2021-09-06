import pandas as pd

pd.read_csv('cities.csv').to_html('table.html',index=False, classes='table table-stripped')