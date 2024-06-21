from elasticsearch import Elasticsearch

# Authenticate from the constructor
client = Elasticsearch(
    "https://localhost:9200",
    ca_certs="/path/to/http_ca.crt",
    basic_auth=("username", "password")
)

# Authenticate via the .options() method:
client.options(
    basic_auth=("username", "password")
).indices.get(index="*")

# You can persist the authenticated client to use
# later or use for multiple API calls:
auth_client = client.options(api_key="api_key")
for i in range(10):
    auth_client.index(
        index="example-index",
        document={"field": i}
    )
