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
#I want to see daily transactions of spesific token
query = gql('''
query {
  tokenDayDatas(orderBy: date,orderDirection:desc,where:{token:"0x7fc66500c84a76ad7e9c93437bfc5ac33e2ddae9"}) {
    id,
date,
priceUSD,
totalLiquidityToken,
totalLiquidityUSD,
totalLiquidityETH,
dailyVolumeToken,
dailyVolumeUSD

  }
}
''')
response = client.execute(query)
print(response)
