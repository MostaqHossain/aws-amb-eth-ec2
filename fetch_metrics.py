import boto3
from datetime import datetime, timedelta

# Create a CloudWatch client in your region
cloudwatch = boto3.client('cloudwatch', region_name='us-east-1')  # Availability Zone us-east-1a → region is us-east-1

# Your node details
network_id = 'your ethereum network id'
node_id = 'your node id'

# Fetch CPU and Memory Utilization
response = cloudwatch.get_metric_data(
    MetricDataQueries=[
        {
            'Id': 'cpuUtilization',
            'MetricStat': {
                'Metric': {
                    'Namespace': 'AWS/ManagedBlockchain',
                    'MetricName': 'CPUUtilization',
                    'Dimensions': [
                        {'Name': 'NetworkId', 'Value': network_id},
                        {'Name': 'NodeId', 'Value': node_id},
                    ],
                },
                'Period': 300,  # 5 minutes
                'Stat': 'Average',
            },
            'ReturnData': True,
        },
        {
            'Id': 'memoryUtilization',
            'MetricStat': {
                'Metric': {
                    'Namespace': 'AWS/ManagedBlockchain',
                    'MetricName': 'MemoryUtilization',
                    'Dimensions': [
                        {'Name': 'NetworkId', 'Value': network_id},
                        {'Name': 'NodeId', 'Value': node_id},
                    ],
                },
                'Period': 300,
                'Stat': 'Average',
            },
            'ReturnData': True,
        }
    ],
    StartTime=datetime.utcnow() - timedelta(hours=1),
    EndTime=datetime.utcnow(),
)

# Print the fetched metrics
for result in response['MetricDataResults']:
    print(f"{result['Id']}: {result['Values']}")
