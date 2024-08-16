import os

import boto3
import time
import paramiko

# Initialize a session using your AWS credentials
session = boto3.Session(
    aws_access_key_id='',
    aws_secret_access_key='',
    region_name=''
)

# Initialize the EC2 resource
ec2 = session.resource('ec2')

# Replace 'INSTANCE_ID' with your actual EC2 instance ID
instance_id = ''

# ADD 'your_key_path with the path to your ssh
ssh_key_path = ""

#ADD user you use to ssh into your instance
ssh_username = ''


# Function to check the instance status
def check_instance_status():
    instance = ec2.Instance(instance_id)
    instance.load()
    return instance.state['Name']


# Start the instance
def start_instance():
    status = check_instance_status()
    if status == 'running':
        print(f'Instance {instance_id} is already running.')
    else:
        instance = ec2.Instance(instance_id)
        response = instance.start()
        print(f'Starting instance {instance_id}...')

        # wait until the instance is running state
        instance.wait_until_running()
        instance.load()
        print(f'Instance {instance_id} is now running.')
        time.sleep(30)


    # Stop the instance
def stop_instance():
    status = check_instance_status()
    if status == 'stopped':
        print(f'Instance {instance_id} is already stopped.')
    else:
        instance = ec2.Instance(instance_id)
        response = instance.stop()
        print(f'Stopping instance {instance_id}...')
        instance.wait_until_stopped()
        print(f'Instance {instance_id} is now stopped.')


# SSH into the instance
def ssh_into_instance():
    instance = ec2.Instance(instance_id)
    public_ip = instance.public_ip_address
    print(f'SSH into instance at {public_ip}...')
    ssh_command = r''
    os.system(ssh_command)

#Main logic
def main():
    status = check_instance_status()
    print(f'The current status of the instance {instance_id} is: {status}')
    action = input("Enter 'start' to start the instance or 'stop' to stop the instance: ").lower()

    if action == 'start':
        start_instance()
        if check_instance_status() == 'running':
            ssh_option = input("Do you want to SSH into the instance now? (yes/no): ").lower()
            if ssh_option == 'yes':
                ssh_into_instance()
            else:
                print('Instance is running. You can SSH later if needed. Don\'t forget to stop it when done.')
    elif action == 'stop':
        stop_instance()
    elif action == 'ssh':
        if status == 'running':
            ssh_into_instance()
        else:
            print('Instance is not running. Start the instance first to SSH into it.')
    else:
        print("Invalid action. Please enter 'start', 'stop', or 'ssh'.")

if __name__ == "__main__":
    main()