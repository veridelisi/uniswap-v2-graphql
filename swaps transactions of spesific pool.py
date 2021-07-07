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
#I want to see swaps transactions of spesific pool
query = gql('''
query {
  swaps(orderBy: timestamp, orderDirection: desc, where:{ pair: "0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852" }) {
    amount0Out,
amount0In,
transaction{id},
pair{token0{symbol},token1{symbol}},
amount1In,
amount1Out,
amountUSD
  }
}
''')
response = client.execute(query)
print(response)
