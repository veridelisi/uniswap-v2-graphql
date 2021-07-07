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
query = gql('''
query {
  pair(id: "0x94b0a3d511b6ecdb17ebf877278ab030acb0a878") {
    token0{name},
    token1{name},
    reserve0,
reserve1,
reserveUSD,
trackedReserveETH
  }
}
''')
response = client.execute(query)
print(response)
