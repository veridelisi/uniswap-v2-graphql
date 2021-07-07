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
#I want to see daily mints transactions of spesific user
query = gql('''
query {
  users(where:{id:"0x9ad4a47e223312b4d8b15d514bd1f7fb7ee6ab8b"})

{
  
  id
}
mints(first: 3, orderBy: timestamp, orderDirection: desc) 
{
  
transaction {id},
 to,
 liquidity,
 amount0,
 amount1,
 amountUSD
}

}

''')
response = client.execute(query)
print(response)
