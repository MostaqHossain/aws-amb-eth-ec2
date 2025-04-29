
# 🔗 Ethereum Data Fetching via AWS Managed Blockchain (AMB)

## 📘 Project Overview

This project demonstrates how to securely connect to an **Ethereum node hosted on AWS Managed Blockchain (AMB)**, fetch the latest block details (including full transactions), and save the data as a JSON file for analysis. It also supports simple data analytics from the command line.

---

## 🎯 Motivation

- To **explore real-time Ethereum blockchain data** using a managed service.
- Demonstrate the setup of a **secure and scalable Ethereum node** using AWS AMB.
- Provide a **lightweight, script-based solution** for Ethereum data analysis and monitoring.

---

## 🌐 Scope of Work

- Create an Ethereum node using AWS Managed Blockchain.
- Generate and use a **secure billing token and RPC URL**.
- Connect using `web3.py` and fetch the latest block and transactions.
- Save and analyze the block data in CLI environment.
- Visualize the process in documentation/presentation format.

---

## 📁 Project Structure

```
aws-eth-block-fetcher/
│
├── web3_conn.py               # Basic connectivity test to Ethereum node
├── fetch_latest.py            # Fetch and print the latest block info
├── save_latest.py             # Save full block + transactions as JSON
├── data_analysis.py           # CLI-based analysis of transaction data
├── latest_block_details.json  # Sample output file (latest block)
├── flowchart.png              # Flow diagram showing architecture
├── requirements.txt           # Python dependencies
└── README.md                  # This documentation
```

---

## ⚙️ Getting Started

### ✅ Prerequisites

- AWS account with permissions to use **Managed Blockchain (Ethereum)**
- A working Ethereum node created via AWS Console
- Billing Token and RPC Endpoint
- Python 3.7 or newer

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/aws-eth-block-fetcher.git
cd aws-eth-block-fetcher

# Optional: Use virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### `requirements.txt`

```
web3
```

---

## 🔐 Secure RPC URL Setup

Avoid hardcoding secrets in your scripts. Use environment variables or a config file.  
Update the RPC URL format as follows:

```python
rpc_url = "https://<node-id>.t.ethereum.managedblockchain.us-east-1.amazonaws.com/?billingtoken=<your-billing-token>"
```

---

## 🚀 Usage

### 1. Check Node Connectivity

```bash
python web3_conn.py
```

### 2. Fetch Latest Block Details

```bash
python fetch_latest.py
```

### 3. Save Full Block and Transactions to JSON

```bash
python save_latest.py
```

This will generate a file named `latest_block_details.json`.

### 4. Analyze the Data in Terminal

```bash
python data_analysis.py
```

Outputs:

- Block number and hash
- Transaction count
- Average gas used and gas price
- List of `from` and `to` addresses

---

## 🧠 Flow Diagram

The interaction between components is illustrated in `flowchart.png`.  
You may include it in documentation or presentations to explain the flow:

- AWS Managed Blockchain Ethereum Node  
- Python Client (via EC2 or local machine)  
- JSON output and analytics pipeline

---

## 📈 Example Analytics Output

```bash
Connected to Ethereum Node!
Latest Block: 20412901
Transaction Count: 123
Average Gas Used: 21000
Most Active From Address: 0xabc...
```

---

## 💡 Future Work

- Real-time streaming using WebSocket (Infura or native)
- Integration with AWS Lambda for automation
- Build a dashboard (e.g., Streamlit, Dash) to visualize blocks

---

## 📚 References

- [AWS AMB Ethereum](https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/get-started.html)
- [Web3.py Documentation](https://web3py.readthedocs.io/)
- [Ethereum JSON-RPC](https://ethereum.org/en/developers/docs/apis/json-rpc/)
- [Secure Secrets with Python](https://12factor.net/config)

---

## 🙋 Contact

**S M Mostaq Hossain**  
📧 Email: shossain42@tntech.edu  
🔗 [LinkedIn]([https://www.linkedin.com/in/your-profile](https://www.linkedin.com/in/mostaqhossain10/))

---

## 📄 License

This project is open-sourced under the **MIT License**.
