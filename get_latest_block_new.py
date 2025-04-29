from web3 import Web3

# Connect to AWS Managed Ethereum Node
rpc_url = "https://<node-id>.t.ethereum.managedblockchain.us-east-1.amazonaws.com/?billingtoken=<your-billing-token>"
w3 = Web3(Web3.HTTPProvider(rpc_url))

# Check connection
if w3.is_connected():
    print("Connected to AWS Managed Ethereum Node!")

    # Get the latest block number
    latest_block_number = w3.eth.block_number
    print(f"Latest Block Number: {latest_block_number}")

    # Get full details of the latest block
    latest_block = w3.eth.get_block(latest_block_number, full_transactions=True)

    # Print the block details
    print("\nLatest Block Details:")
    print(f"Block Hash: {latest_block['hash'].hex()}")
    print(f"Parent Hash: {latest_block['parentHash'].hex()}")
    print(f"Timestamp: {latest_block['timestamp']}")
    print(f"Gas Used: {latest_block['gasUsed']}")
    print(f"Transaction Count: {len(latest_block['transactions'])}")
else:
    print("Failed to connect to Ethereum node")
