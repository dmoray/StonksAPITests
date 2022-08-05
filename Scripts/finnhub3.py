import finnhub
import pandas as pd
from pandas.io.json import json_normalize
 

# Setup client
finnhub_client = finnhub.Client(api_key="sandbox_cblo5v2ad3ib03etqs20")

# Stock candles
res = finnhub_client.company_revenue_estimates('PGR', freq='quarterly')
result = json_normalize(res, 'data', [ 'period','numberAnalysts','revenueAvg', 'revenueHigh','revenueLow'],errors='ignore')
print(result)
#df = pd.DataFrame(res)
#df.to_csv("finnhub_test1.csv")
print('END')