from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

sample_transport=RequestsHTTPTransport(
    url='https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2',
    verify=True,
    retries=5,
)
client = Client(
    transport=sample_transport
)
#I want to see pools daily amounts
query = gql('''
query {
  pairDayDatas(first:5, orderBy: date, orderDirection:desc)
  {
    token0{name},
    token1{name},
    dailyVolumeToken0,
    dailyVolumeToken1,
    reserve0,
    reserve1,
    reserveUSD,
    dailyVolumeUSD,
    dailyTxns
  }
}

''')
response = client.execute(query)
print(response)
