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
#I want to see hourly pool datas
query = gql('''
query {
pairHourDatas(first: 10, orderBy:hourStartUnix orderDirection: desc, where: {pair:"0x94b0a3d511b6ecdb17ebf877278ab030acb0a878"})
{
pair
{

token0{name}
token1{name}
},
hourlyVolumeToken0
hourlyVolumeToken1
hourlyVolumeUSD
reserve0
reserve1
reserveUSD
}
}

''')
response = client.execute(query)
print(response)
