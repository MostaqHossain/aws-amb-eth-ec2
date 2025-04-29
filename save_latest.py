import json
from web3 import Web3
from web3.datastructures import AttributeDict  # Import for AttributeDict

# Connect to AWS Managed Ethereum Node
rpc_url = "https://<node-id>.t.ethereum.managedblockchain.us-east-1.amazonaws.com/?billingtoken=<your-billing-token>"
w3 = Web3(Web3.HTTPProvider(rpc_url))

# Function to convert non-serializable objects to string
def hex_to_str(obj):
    if isinstance(obj, bytes):
        return obj.hex()  # Convert bytes (HexBytes) to string
    if isinstance(obj, dict):
        return {key: hex_to_str(value) for key, value in obj.items()}
    if isinstance(obj, list):
        return [hex_to_str(item) for item in obj]
    if isinstance(obj, AttributeDict):  # Convert AttributeDict to normal dict
        return {key: hex_to_str(value) for key, value in obj.items()}
    return obj

# Main script
if w3.is_connected():
    print("Connected to AWS Managed Ethereum Node!")

    # Fetch the latest block number
    latest_block_number = w3.eth.block_number
    print(f"Latest Block Number: {latest_block_number}")

    # Fetch full block details, including full transaction objects
    latest_block = w3.eth.get_block(latest_block_number, full_transactions=True)

    # Convert the block into a serializable format
    latest_block_serializable = hex_to_str(latest_block)

    # Save the block details into a JSON file
    output_file = "latest_block_details.json"
    with open(output_file, "w") as file:
        json.dump(latest_block_serializable, file, indent=4)

    print(f"Latest block details successfully saved to '{output_file}'.")

else:
    print("Failed to connect to Ethereum node.")
