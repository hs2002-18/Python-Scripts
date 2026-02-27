import boto3
from botocore.exceptions import ClientError

# Create EC2 client
ec2 = boto3.client('ec2', region_name='ap-south-1')

# Function to list all EC2 instances and their state
def list_instances():
    try:
        response = ec2.describe_instances()
        instances = []
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                instance_state = instance['State']['Name']
                print(f"Instance ID: {instance_id} | State: {instance_state}")
                instances.append(instance_id)
        if not instances:
            print("No instances found.")
        return instances
    except ClientError as e:
        print(f"Error listing instances: {e}")

# Function to stop an EC2 instance
def stop_instances(instance_id):
    try:
        ec2.stop_instances(InstanceIds=[instance_id])
        print(f"Stopping instance: {instance_id}")
    except ClientError as e:
        print(f"Error stopping instance: {e}")

# Function to create an EC2 instance
def create_instance():
    try:
        key_name = input("Enter your key name: ")
        response = ec2.run_instances(
            ImageId='ami-019715e0d74f695be',  
            InstanceType='t3.micro',          
            MinCount=1,
            MaxCount=1,
            KeyName=key_name,
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [{'Key': 'Name', 'Value': 'PythonCreatedInstance'}]
                }
            ]
        )
        instance_id = response['Instances'][0]['InstanceId']
        print(f"Created new instance with ID: {instance_id}")
    except ClientError as e:
        print(f"Error creating instance: {e}")

# Main function
def main_menu():
    while True:
        print("\n===== EC2 Manager =====")
        print("1. List Instances")
        print("2. Stop Instance")
        print("3. Create Instance")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            list_instances()  
        elif choice == '2':
            instance_id = input("Enter Instance ID to stop: ")
            stop_instances(instance_id)
        elif choice == '3':
            create_instance()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
