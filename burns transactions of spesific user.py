pip install gql


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
#I want to see burns transactions of spesific user
query = gql('''
query {
  burns(first:2, where:{sender:"0x1ae4e247eb47bf8a2f126b34e67c4df2aab5a024"}, orderBy:timestamp,orderDirection:desc) {
    amount0,
amount1,
transaction{id},
pair{token0{symbol},token1{symbol}},
amountUSD

  }
}
''')
response = client.execute(query)
print(response)
