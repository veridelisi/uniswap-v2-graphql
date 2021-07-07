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
#I want to see daily transactions amount in uniswap
query = gql('''
query {
  uniswapDayDatas(first:500,orderBy:date,orderDirection:desc) {
    id,
date,
dailyVolumeETH,
dailyVolumeUSD,
dailyVolumeUntracked,
totalVolumeETH,
totalLiquidityETH,
totalVolumeUSD,
totalLiquidityUSD,
txCount


  }
}
''')
response = client.execute(query)
print(response)
