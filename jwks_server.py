# jwks_server.py
import asyncio
from flask import Flask, jsonify
import logging
from key_management import get_all_keys
from auth import token_required

# Configure logging for the JWKS server
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/.well-known/jwks.json', methods=['GET'])
@token_required
def jwks_endpoint():
    """
    RESTful endpoint that returns JWKS (JSON Web Key Set).
    Utilizes asynchronous processing to fetch keys without blocking.
    """
    # Run the blocking key retrieval function asynchronously
    keys = asyncio.run(async_get_keys())
    return jsonify({"keys": keys})

async def async_get_keys():
    return await asyncio.to_thread(get_all_keys)

if __name__ == '__main__':
    # Run Flask with threading enabled for concurrent request handling
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)
