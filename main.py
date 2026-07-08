import src.otx_py

client = src.otx_py.OTXClient(
    api_key="81eae5c1e61bb0501d7ebe9d1217227602dbcadb5222d407361e7f2e6376e565"
)

print(client.search_users(query="test", page=1, limit=20))
