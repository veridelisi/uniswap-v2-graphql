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
#I want to see mints transactions of spesific user
query = gql('''
query {
  mints(first:5, where:{to:"0x5acedba6c402e2682d312a7b4982eda0ccf2d2e3"}, orderBy:timestamp,orderDirection:desc) {
    amount0,
amount1,
liquidity,
transaction{id},
pair{token0{symbol},token1{symbol}},
amountUSD

  }
}
''')
response = client.execute(query)
print(response)
