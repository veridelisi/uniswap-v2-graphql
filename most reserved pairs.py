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
#I want to see most reserved pairs
query = gql('''
query {
  pairs(first:5, orderBy:trackedReserveETH, orderDirection:desc) {
    reserve0,
reserve1,
token0{name},
token1{name},
reserve0,
reserve1,
totalSupply,
reserveETH,
token0Price,
token1Price,
volumeToken0,
volumeToken1,
volumeUSD,
txCount,
liquidityProviderCount,
reserveUSD,
trackedReserveETH,

  }
}
''')
response = client.execute(query)
print(response)
