from index import create_app
from wsgicors import CORS

app = CORS(create_app(), headers="*", methods="*", origin="*", maxage="86400")
