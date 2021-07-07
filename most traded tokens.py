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
#I want to see most traded tokens.
query = gql('''
query {

uniswapFactories
{
# factory address
id

# pair info
pairCount

# total volume from genesis to today
totalVolumeUSD
totalVolumeETH

# total liquidity
totalLiquidityUSD
totalLiquidityETH

# transactions
txCount
}
}
''')
response = client.execute(query)

print(response)
