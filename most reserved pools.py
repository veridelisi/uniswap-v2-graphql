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
#I want to see most reserved pools
query = gql('''
query {
  pairs(first: 50, orderBy: trackedReserveETH, orderDirection: desc) {
    id,
token0{name},
token1{name},
trackedReserveETH


  }
}
''')
response = client.execute(query)
print(response)
