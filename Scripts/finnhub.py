
import finnhub
import pandas as pd

#token="cblo5v2ad3ib03etqs1g"
token="sandbox_cblo5v2ad3ib03etqs20"
finnhub_client = finnhub.Client(api_key="sandbox_cblo5v2ad3ib03etqs20")

print('START')
#print(finnhub_client.symbol_lookup('apple'))
#rint(finnhub_client.company_profile(symbol='AAPL'))
# print(finnhub_client.company_executive('AAPL'))
# print(finnhub_client.general_news('general', min_id=0))
#print(finnhub_client.company_news('AAPL', _from="2020-06-01", to="2020-06-10"))
#print(finnhub_client.news_sentiment('AAPL'))
#print(finnhub_client.company_peers('AAPL'))
#print(finnhub_client.company_basic_financials('AAPL', 'all'))
#print(finnhub_client.ownership('AAPL', limit=5))
#print(finnhub_client.financials('AAPL', 'bs', 'annual'))
res = finnhub_client.stock_revenue_breakdown('PGR')
df = pd.DataFrame(res.json())
df.to_csv("finnhub_test.csv")
print('END')