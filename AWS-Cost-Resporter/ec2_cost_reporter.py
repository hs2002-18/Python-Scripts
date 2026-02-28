import boto3
import csv
from botocore.exceptions import ClientError
from datetime import datetime

#Change region as per-requirment
REGION = 'ap-south-1'

#Simple Pricing Values (example not accurate)
#This will be updated to use AWS CLI in next version
INSTANCE_PRICING = {
    "t2.micro": 0.0116,
    "t2.small": 0.023,
    "t3.micro": 0.0104,
    "t3.small": 0.0208
}

#Function that will estimate monthly cost when instances are runing for 24hrs
def estimate_monthly_cost(instance_type):
    hourly_price = INSTANCE_PRICING.get(instance_type, 0)
    return round(hourly_price*24*30, 2)

#Function that generates report in a .csv file with all the EC2 instance fields that are specified
def generate_report():
    ec2 = boto3.client('ec2', region_name = REGION)
    try:
        response = ec2.describe_instances()
        instances = []
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                instance_type = instance['InstanceType']
                instance_state = instance['State']['Name']
                launch_time = instance['LaunchTime']
                monthly_cost = estimate_monthly_cost(instance_type)
                instances.append([instance_id, instance_type, instance_state, launch_time, monthly_cost])

        with open('instance_report.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                "Instance ID",
                "Instance Type",
                "State",
                "Launch Time",
                "Estimated Monthly Cost ($)"
            ])
            writer.writerows(instances)
        print("Report generated successfully.")
    except ClientError as e:
        print(f"Error generating report: {e}")

if __name__ == "__main__":
    generate_report()