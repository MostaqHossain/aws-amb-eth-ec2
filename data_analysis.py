from web3 import Web3

# Connect to AWS Managed Ethereum Node
rpc_url = "https://<node-id>.t.ethereum.managedblockchain.us-east-1.amazonaws.com/?billingtoken=<your-billing-token>"

w3 = Web3(Web3.HTTPProvider(rpc_url))

# Ensure connected
if w3.is_connected():
    print("Connected to AWS Managed Ethereum Node!")

    # Get the latest block number
    latest_block_number = w3.eth.block_number
    print(f"Latest Block Number: {latest_block_number}")

    # Data lists to store block number, transaction count, and gas used
    block_numbers = []
    transaction_counts = []
    gas_used = []

    # Analyze the last 10 blocks
    for block_number in range(latest_block_number, latest_block_number - 10, -1):
        block = w3.eth.get_block(block_number, full_transactions=True)

        # Store block number, transaction count, and gas used
        block_numbers.append(block_number)
        transaction_counts.append(len(block['transactions']))
        gas_used.append(block['gasUsed'])

    # Display analysis data in the command line
    print("\nTransaction Count and Gas Used per Block (Last 10 Blocks):\n")
    print(f"{'Block Number':<15}{'Transaction Count':<20}{'Gas Used':<20}")
    print("-" * 55)

    for i in range(len(block_numbers)):
        print(f"{block_numbers[i]:<15}{transaction_counts[i]:<20}{gas_used[i]:<20}")

    # Optionally: Display Average Gas Used and Average Transaction Count
    avg_transaction_count = sum(transaction_counts) / len(transaction_counts)
    avg_gas_used = sum(gas_used) / len(gas_used)

    print("\nAverage Transaction Count per Block:", avg_transaction_count)
    print("Average Gas Used per Block:", avg_gas_used)

else:
    print("Failed to connect to Ethereum node")

