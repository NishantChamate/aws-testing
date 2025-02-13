# Deploying a Scalable Calculator Service on AWS EC2 with Logging and Containerization

## Introduction

The objective of this project is to develop and deploy a scalable calculator service on AWS EC2 that performs four basic arithmetic operations: addition, subtraction, multiplication, and division. The solution incorporates logging, containerization, and automated deployment to ensure maintainability and scalability.

By the end of this documentation, you will:
- Launch and configure an AWS EC2 instance.
- Deploy a Python-based calculator application.
- Implement a logging system.
- Containerize the application using Docker.
- Create an Amazon Machine Image (AMI) for easy deployment.
- Perform testing and validation.

## Prerequisites

Before beginning, ensure you have:
- An active AWS account.
- AWS CLI installed and configured.
- Docker installed on your local machine.
- Basic knowledge of Python, Docker, and AWS EC2.
- A terminal or command-line interface for executing commands.

## Setting Up an EC2 Micro Instance

### Step 1: Log in to AWS
- Navigate to the AWS Console and log in.
- Click on **Services** in the top menu.
- Select **EC2** from the list.

### Step 2: Launch an EC2 Instance
- Click **Launch Instance**.
- Choose **Amazon Linux 2 AMI** (recommended for compatibility with Docker).
- Select **t2.micro** as the instance type (eligible for free tier).
- Click **Next: Configure Instance Details**.

### Step 3: Configure Instance Details
- Leave the default settings (one instance, no additional settings needed).
- Click **Next: Add Storage**.
- Keep the default 8 GB SSD volume.
- Click **Next: Add Tags**.
- Add a tag with Key: **Name** and Value: **Calculator-Instance**.
- Click **Next: Configure Security Group**.

### Step 4: Configure Security Groups
- Create a new security group named **CalculatorSG**.
- Add the following inbound rules:
  - **SSH (port 22)** - My IP (for secure access).
  - **HTTP (port 80)** - Anywhere (for web-based interaction if needed).
- Click **Review and Launch**.

### Step 5: Launch the Instance
- Click **Launch**.
- Choose **Create a new key pair**, name it **calculator-key**, and download it.
- Click **Launch Instance**.

### Step 6: Connect to the Instance
Use the following SSH command to access your instance:
```bash
ssh -i calculator-key.pem ec2-user@your-ec2-public-ip
