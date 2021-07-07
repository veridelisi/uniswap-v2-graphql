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
#I want to see swaps transactions of spesific user
query = gql('''
query {
  swaps(first:5, where:{to:"0xee1F07F88934C2811E3DcAbdf438d975C3d62cd3"}, orderBy:timestamp,orderDirection:desc) {
    amount0In,
amount1In,
amount0Out,
amount1Out,
pair{token0{symbol},token1{symbol}},
amountUSD

  }
}
''')
response = client.execute(query)
print(response)
