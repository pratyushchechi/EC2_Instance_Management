# EC2 Instance Management with Python and Boto3

## Project Overview

This project provides a Python script that allows you to manage your AWS EC2 instances. You can start, stop, and SSH into an EC2 instance using a command-line interface. The script uses the Boto3 library to interact with AWS services.

## Features

- **Start EC2 Instance**: Start an EC2 instance if it's not already running.
- **Stop EC2 Instance**: Stop an EC2 instance if it's currently running.
- **SSH into EC2 Instance**: SSH into the EC2 instance after starting it or at a later time.
- **Instance Status Check**: The script checks the current state of the instance before taking any action to avoid unnecessary operations.

## Requirements

- Python 3.x
- Boto3 library
- Paramiko library
- AWS Credentials with appropriate permissions
- An EC2 instance with an associated key pair for SSH access

## Setup Instructions

1. **Install Required Python Packages:**

   ```bash
   pip install boto3 paramiko

2. **Configure AWS Credentials:**

- Make sure your AWS credentials are configured. You can configure them using the AWS CLI or by setting them directly in the script.

## **Edit the Script:**

- Replace the placeholder values in the script with your actual AWS credentials, region, instance ID, and SSH key path.

## **Running the Script:**

- To start, stop, or SSH into the instance, simply run the script using Python:
  - python ubuntu_server.py

## **Follow the on-screen prompts to manage your EC2 instance.**

## Code Explanation
## **Check Instance Status:**

- def check_instance_status():
    instance = ec2.Instance(instance_id)
    instance.load()
    return instance.state['Name']
This function checks the current status of the EC2 instance (e.g., running, stopped) to determine the next steps.

## Start Instance
- def start_instance():
    status = check_instance_status()
    if status == 'running':
        print(f'Instance {instance_id} is already running.')
    else:
        instance = ec2.Instance(instance_id)
        response = instance.start()
        print(f'Starting instance {instance_id}...')
        instance.wait_until_running()
        print(f'Instance {instance_id} is now running.')

- This function starts the instance if it is not already running.

## Stop Instance
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
- This function stops the instance if it is currently running.

## SSH into Instance

- def ssh_into_instance():
    instance = ec2.Instance(instance_id)
    public_ip = instance.public_ip_address
    print(f'SSH into instance at {public_ip}...')
    ssh_command = r'ssh -i "your_key.pem" ubuntu@ec2-your-public-ip.compute-1.amazonaws.com'
    os.system(ssh_command)
This function uses the Paramiko library to SSH into the instance.

## Usage
1. **Start the Instance:**
    - Run the script and choose the start option.**

2. **SSH into the Instance:**

  - After starting, you will be prompted to SSH into the instance. 
  - If you choose no, you can SSH into it later by running the script again and choosing the ssh option.

3. **Stop the Instance:**

    -When you are done working on the instance, run the script and choose the stop option.


## Conclusion
This script automates the basic management of an AWS EC2 instance, making it easier to start, stop, and connect to your instances. It's a practical tool for anyone working with AWS infrastructure regularly.

