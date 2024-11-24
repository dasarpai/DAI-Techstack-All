Learner Lab
Environment Overview
Environment Navigation 
Access the AWS Management Console 
Region restriction 
Service usage and other restrictions 
Using the terminal in the browser 
Running AWS CLI commands 
Using the AWS SDK for Python 
Preserving your budget 
Accessing EC2 Instances 
SSH Access to EC2 Instances 
SSH Access from Windows
SSH Access from a Mac

 

Environment Overview
This Learner Lab provides a sandbox environment for ad-hoc exploration of AWS services.

This environment is long-lived. When the session timer runs to 0:00, the session will end, but any data and resources that you created in the AWS account will be retained. If you later launch a new session (for example, the next day), you will find that your work is still in the lab environment. 

Running EC2 instances will be stopped and then automatically restarted the next time you start a session. SageMaker notebook instances will be stopped, but not restarted the next time you start a session. 

 IMPORTANT: Monitor your lab budget in the lab interface above. Whenever you have an active lab session, the latest known remaining budget information will display at the top of this screen. This data comes from AWS Budgets which typically updates every 8 to 12 hours. Therefore the remaining budget that you see may not reflect your most recent account activity.  If you exceed your lab budget your lab account will be disabled and all progress and resources will be lost. Therefore, it is important for you to manage your spending. Read about how to preserve your budget.

 

Environment Navigation
Use the  Readme link above to return to these instructions at any time.

Use the  AWS Details link above to access information about your environment.

 Tip: you can resize this panel at anytime by dragging the bar to the left of these instructions to make it wider or narrower.

Use the  Reset link above if you ever want to reset your AWS account back to the way it was in the beginning, before you ever ran sessions of this lab environment.  Note that it will not reset your budget.  CAUTION: if you choose reset and then choose Yes to confirm that you do want to reset, you will permanently delete everything that you have created or stored in the AWS account.

 

Access the AWS Management Console
At the top of these instructions, choose 
  Start Lab to start the lab session.

The lab session is started and session information is displayed.

A timer above shows the time remaining in the session.

 Tip: You can refresh the session length at any time by choosing Start Lab again before the timer reaches 0:00.

Choose the  Readme link to return to these instructions.

Connect to the AWS Management Console by choosing the AWS link above the terminal window.

You should be connected to the AWS Management Console.

Tip: If a new browser tab does not open, a banner or icon is usually at the top of your browser with the message that your browser is preventing the site from opening pop-up windows. Choose the banner or icon, and then choose Allow pop-ups.

 Tip: if you are interested in interacting with the AWS account programmatically, read the Using the terminal in the browser  section below for details.

 

Region restriction
All service access is limited to the us-east-1 and us-west-2 Regions unless mentioned otherwise in the service details below. If you load a service console page in another AWS Region you will see access error messages.

 

Service usage and other restrictions
The following services can be used. Specific limitations apply as documented.  Services restrictions are subject to change.

Amazon API Gateway
This service can assume the LabRole IAM role.
AWS App Mesh
Application Auto Scaling
This service can assume the LabRole IAM role.
AWS AppSync
Amazon Athena
This service can assume the LabRole IAM role.
Amazon Aurora
AWS Backup
AWS Batch
This service can assume the LabRole IAM role.
AWS Certificate Manager (ACM)
AWS Cloud9
This service can assume the LabRole IAM role.
Supported Instance types: nano, micro, small, medium, large, and c4.xlarge.
Tip: When creating a new Cloud9 instance with the New EC2 instance environment type, in Network settings choose Secure Shell (SSH).
AWS CloudFormation
This service can assume the LabRole IAM role.
Amazon CloudFront
This service can assume the LabRole IAM role.
Amazon CloudSearch
AWS CloudShell
AWS CloudTrail
This service can assume the LabRole IAM role.
You can create a CloudTrail, but you cannot enable CloudWatch logging for the trail.
Amazon CloudWatch
AWS CodeCommit
This service can assume the LabRole IAM role.
AWS CodeDeploy
This service can assume the LabRole IAM role.
Amazon Comprehend
This service can assume the LabRole IAM role.
AWS Config
AWS Cost and Usage Report
AWS Cost Explorer
AWS Data Pipeline
This service can assume the LabRole IAM role.
Tip: If you see a warning that data pipeline:GetAccountLimits cannot be performed, you can ignore it. Also, when creating a pipeline, choose LabRole as the pipeline role and if applicable, choose LabInstanceProfile as the EC2 instance role.
AWS DeepComposer
AWS DeepLens
AWS DeepRacer
This service can assume the LabRole IAM role.
AWS Directory Service
Amazon DynamoDB
This service can assume the LabRole IAM role.
Amazon EC2 Auto Scaling
This service can assume the LabRole IAM role.
Supported Instance types: nano, micro, small, medium, and large.
Read the Concurrently running instances limits details documented in the EC2 service details below to be aware of further restrictions.
Recommendation: size to your actual need to avoid using up your cost budget.
AWS Elastic Beanstalk
This service can assume the LabRole IAM role.
To create an application: choose Create Application, give it an application name,  choose a platform, then choose Configure more options. Scroll down to the Security panel and choose Edit. For Service role, choose LabRole. If the environment is in the us-east-1 AWS Region, for EC2 key pair, choose vockey and for IAM instance profile, choose LabInstanceProfile. Choose Save, then choose Create app.
Supported Instance types: nano, micro, small, medium, and large. If you attempt to launch a larger instance type, it will be terminated.
Amazon Elastic Block Store (EBS)
Maximum volume size is 100GB
PIOPs not supported
Amazon Elastic Compute Cloud (EC2)
This service can assume the LabRole IAM role.

Supported AMIs: 

AMI available in us-east-1 or us-west-2. For example, Quick Start AMIs, My AMIs, and Community AMIs. 
AWS Marketplace AMIs are not supported. AMIs such as MacOS that must launch as a dedicated instance or on a dedicated host are also not supported. 
Recommendation: To launch an instance with a guest OS of Microsoft Windows, Amazon Linux, or one of many other popular Linux distributions, choose "Launch Instances", then choose from the ones available in the "Quick Start" tab.
Supported Instance types: nano, micro, small, medium, and large.

On-Demand instances only

Concurrently running instances limits per supported region: 

Maximum of 9 concurrently running EC2 instances, regardless of instance size. If you attempt to launch more, the excess instances will be terminated (and 9 will be left running).

Note: Service such as EMR, Cloud9, Elastic Beanstalk may also launch EC2 instances. The 9 concurrent running EC2 instances limit applies across all services that create instances visible in the EC2 console.

Maximum of 32 vCPU used by concurrently running instances, regardless of instance size or instance count. For example, t2.micro instances use 1 vCPU each, so you could run up to 32 of them in us-west-2 (but still only 9 of them in us-east-1 because of the other limitation listed above)

Note: The maximum 32 vCPU limit also applies across all services that create instances visible in the EC2 console.

Caution: Any attempt to have 20 or more concurrently running instances (regardless of size), will result in immediate deactivation of the AWS account and all resources in the account will be immediately deleted.

Recommendation: size to your actual need to avoid using up your cost budget.
EBS volumes - sizes up to 100 GB and type must be General Purpose SSD (gp2, gp3 ) cold HDD (sc1), or standard.

Key pairs - If you are creating an EC2 instance in any AWS Region other than us-east-1, the vockey key pair will not be available. In such cases, you should create a new key pair and download it when creating the EC2 instance. Then use the new key pair to connect to that instance.

A role named LabRole and an instance profile named LabInstanceProfile have been pre-created for you. You can attach the role (via the instance profile) to an EC2 instance when you want to access an EC2 instance (terminal in the browser) using AWS Systems Manager Session Manager. The role also grants permissions to any applications running on the instance to access many other AWS services from the instance.

Tips: 

When your session ends, the lab environment may place any running instances into a 'stopped' state. 
When you start a new session, the lab environment will start all instances that were previously stopped by you or stopped by the lab environment when the lab session ended. 
Instances that have been stopped and started again will be assigned a new IPv4 public IP address unless you have an elastic IP address associated with the instance.
Recommendations: 

To preserve your lab budget, stop any running EC2 instances before you are done using the account for the day (and terminate them if not longer needed). 
Be aware of all instances you keep in the account between sessions because they will run (and cut into your budget) when you start the lab again unless you remember to turn stop them manually after starting the lab.
Amazon Elastic Container Registry (ECR)
The LabRole IAM role has read-only access to this service and as a console user you have write access to this service.
Amazon Elastic Container Service (ECS)
Supported Instance types: nano, micro, small, medium, and large.

To avoid permissions errors, be sure to set LabRole as the role to use wherever you are prompted to specify a role. For example, as the task role and task execution role when creating a task definition.

Tip: If you see a message when creating a cluster that the ECS service linked role could not be assumed, choose the back button and then try again. This sometimes happens if the service linked role does not yet exist in your account.

 

Amazon Elastic File System (EFS)
This service can assume the LabRole IAM role.
Amazon Elastic Inference
Amazon Elastic Kubernetes Service (EKS)
This service can assume the LabRole IAM role.
Supported Instance types: nano, micro, small, medium, and large.
Elastic Load Balancing (ELB)
This service can assume the LabRole IAM role.
Amazon Elastic MapReduce (EMR)
This service can assume the LabRole IAM role.

Supported Instance types: nano, micro, small, medium, and large. If you attempt to launch a larger instance type, it will be terminated. 

Tip: If you have any trouble successfully launching a cluster, try using the m4.large instance type. 
Maximum of 32 vCPU used by concurrently running EC2 instances in an AWS Region. Note that you are also limited to launching no more than nine (9) instances (of any size) in a Region at once.

Amazon ElastiCache
Amazon EventBridge
AWS Fargate
This service can assume the LabRole IAM role.
Amazon Forecast
This service can assume the LabRole IAM role.
AWS Glue
This service can assume the LabRole IAM role.
AWS Glue DataBrew
This service can assume the LabRole IAM role.
Amazon GuardDuty
AWS Health
AWS Identity and Access Management (IAM)
Extremely limited access. You cannot create users or groups. You cannot create roles, except that you can create service-linked roles.

Service role creation is generally permitted. If the service needs to create a role for you, you may need to retry role creation if it fails the first time.

A role named LabRole has been pre-created for you. This role is designed to be used when you want to attach a role to a resource in an AWS service. It grants many AWS services access to other AWS services and has permissions very similar to the permissions you have as a user in the console.  

Example use: attach the LabRole via the instance profile named LabInstanceProfile to an EC2 instance for terminal in the browser access to an EC2 instance guest OS using AWS Systems Manager Session Manager.
Another example: Attach the LabRole to a Lambda function so that the Lambda function can access S3, CloudWatch, RDS, or some other service.
Another example: Attach the LabRole to a SageMaker notebook instance so that the instance can access files in an S3 bucket.
AWS IAM Access Analyzer
Amazon Inspector
AWS IoT 1-Click
AWS IoT Analytics
This service can assume the LabRole IAM role.
AWS IoT Core
This service can assume the LabRole IAM role.
AWS IoT Greengrass
Amazon Kendra
This service can assume the LabRole IAM role.
AWS Key Management Service (KMS)
This service can assume the LabRole IAM role.
Amazon Kinesis
If attempting to create a Kineses Data Analytics Studio notebook, choose "Create with custom settings" and then choose LabRole in the IAM settings area. 
If attempting to create a Kinesis Delivery Stream, choose "Advance settings" and then choose to use the existing LabRole.
Amazon Kinesis Video Streams
AWS Lambda
Tip: Attach the existing LabRole to any function that you create if that function will need permissions to interact with other AWS services.
Amazon Lex
This service can assume the LabRole IAM role.
Amazon Machine Learning (Amazon ML)
AWS Marketplace Subscriptions
Extremely limited read-only access.
AWS Mobile Hub
Amazon Neptune
Supported instance types: nano, micro, small, and medium (Tip: choose Burstable classes to find these).
Supported storage types: EBS volumes - size up to 100 GB and type General Purpose SSD (gp2). PIOPS storage types are not supported.
On-Demand DB instance class types only.
Enhanced monitoring is not supported (you must uncheck this default setting in the Additional configuration / Monitoring panel).
Tip: to preserve your lab budget, stop any running Neptune instances before you are done using the account for the day (or terminate them if not longer needed). 
AWS OpsWorks
Amazon Personalize
This service can assume the LabRole IAM role.
Amazon Polly
Amazon QuickSight
This service can assume the LabRole IAM role.
Tip: When creating the account, choose Enterprise. Ignore the warning  "This IAM user or role may not have all the correct permissions...". For authentication method, choose "Use IAM federated identities & QuickSight-managed users", and for IAM role, choose existing role named LabRole.
Amazon Redshift
This service can assume the LabRole IAM role.
Supported instance type: dc2.large
Supported cluster size: maximum two instances
Amazon Rekognition
This service can assume the LabRole IAM role.
Amazon Relational Database Service (RDS)
This service can assume the LabRole IAM role.
Supported database engines: Amazon Aurora, Oracle, Microsoft SQL, MySQL, PostgreSQL and MariaDB. Note: if you are creating an RDS instance using a CloudFormation template, be sure to specify the engine type using lower-case letters.
Supported instance types: nano, micro, small, and medium (Tip: choose Burstable classes to find these).
Supported storage types: EBS volumes - size up to 100 GB and type General Purpose SSD (gp2). PIOPS storage types are not supported.
On-Demand DB instance class types only.
Enhanced monitoring is not supported (you must uncheck this default setting in the Additional configuration / Monitoring panel).
Tip: to preserve your lab budget, stop any running RDS instances before you are done using the account for the day (or terminate them if not longer needed). 
Caution: When a lab sessions ends, the lab environment may not stop an RDS instance or cluster that you leave running. Also, even if you do stop an RDS instance, if you leave it stopped for seven days, AWS will start it again automatically, which will increase the cost impact.
AWS Resource Groups & Tag Editor
This service can assume the LabRole IAM role.
AWS RoboMaker
This service can assume the LabRole IAM role.
Supported Instance types for development environments: nano, micro, small, medium, large, and c4.xlarge only.
Amazon Route 53
You cannot register a domain.
Amazon SageMaker
This service can assume the LabRole IAM role.

You can create SageMaker Notebook instances. 

Supported notebook instance types: medium, large, and xlarge only.
GPU instance types are not supported.
There is limited support for SageMaker Studio features.

Note: To launch SageMaker Studio, choose Launch SageMaker Studio. Accept the default user profile, and specify LabRole as the execution role, then choose Submit.  You will receive two not authorized messages because we cannot give you iam:CreateRole access in Learner Labs. However, the SageMaker Domain will still be created and you can still access SageMaker Studio after a few minutes if you navigate to the SageMaker Control panel, and from the Launch app menu next to the user you created, choose Studio. This will open SageMaker Studio. From this screen, you can open resources such as a Python 3 Notebook, Python 3 Console, or Image terminal.
Supported instance types: medium, large, and xlarge only.
Some SageMaker JumpStart projects require more access permissions than we can grant in Learner Labs.
There is limited support for SageMaker Canvas features.

In the Setup SageMaker Domain screen, choose Quick setup, and in the User profile panel choose LabRole as the role to use.  Also, be sure to turn off the Enable SageMaker Canvas permissions. You will observe numerous AccessDeniedException warning, because we cannot give you iam:CreateRole access in Learner Labs. However, the SageMaker Domain will still be created and should be able to access SageMaker Canvas after a few minutes if you choose the Canvas link under Control panel in the SageMaker left side menu. 
Tips: 

When your session ends, the lab environment may place any running SageMaker notebook instances into a 'stopped' state. Stopped SageMaker notebook instances will not be automatically restarted when you start a new session.
To preserve your lab budget when using SageMaker Canvas, logout of the session when you are done working with it. 
AWS Secrets Manager
This service can assume the LabRole IAM role.
AWS Security Hub
AWS Security Token Service (STS)
AWS Serverless Application Repository (SAR)
AWS Service Catalog
This service can assume the LabRole IAM role.
Amazon Simple Notification Service (SNS)
This service can assume the LabRole IAM role.
Amazon Simple Queue Service (SQS)
This service can assume the LabRole IAM role.
Amazon Simple Storage Service (S3)
This service can assume the LabRole IAM role.
Amazon Simple Storage Service Glacier (S3 Glacier)
You cannot create a vault lock
Amazon Simple Workflow Service (SWF)
AWS Step Functions
AWS Storage Gateway
AWS Systems Manager (SSM)
A role named LabRole and an instance profile named LabInstanceProfile have been pre-created for you. You can attach the role (via the instance profile) to an EC2 instance when you want to access an EC2 instance (terminal in the browser) using AWS Systems Manager Session Manager.
Amazon Textract
Amazon Timestream
Amazon Transcribe
This service can assume the LabRole IAM role.
AWS Trusted Advisor
Amazon Virtual Private Cloud (Amazon VPC)
AWS WAF - Web Application Firewall
AWS Well-Architected Tool
AWS X-Ray
Accessing a Terminal in the browser
AWS CloudShell is an AWS service that provides a terminal in the browser. You can access it in the AWS Management Console, at the top of the screen, by choosing the AWS CloudShell icon (highlighted in red in the screen capture below).

cloudshell icon

Other ways to access a terminal in the browser:

Launch an AWS Cloud9 instance, which provides a full IDE, including a terminal. 
Launch an EC2 instance to which you have attached the LabInstanceProfile (which attaches the LabRole IAM role) and then connect to the terminal on it using EC2 Instance Connect.
Further tips:

AWS CloudShell, AWS Cloud9 instances, and EC2 instances of type Amazon Linux 2 have the AWS CLI client already installed. 
AWS CloudShell and AWS Cloud9 instances have AWS account credentials pre-configured in the environment.
 

Running AWS CLI commands
Here is an example AWS CLI command to try running in a terminal. If you have created any EC2 instances in the default account Region, running this command will provide information about them:

aws ec2 describe-instances
See the AWS CLI Command Reference documentation for details on how to use the AWS CLI.

 

Using the AWS SDK for Python
AWS CloudShell also has Python 3 installed with the boto3 library available. You can use it to run AWS Python SDK code. For example:

$ python3
>>> import boto3
>>> ec2 = boto3.client('ec2', region_name='us-east-1')  
>>> ec2.describe_regions()
>>> exit()

See the documentation for details on how to use the AWS SDK for Python.

 

Preserving your budget
Remember,  if you exceed your lab budget your lab account will be disabled and all progress and resources will be lost. Details on how to monitor your budget are provided above.

Suggestions to avoid overspending:

Launch only the number of instances you need, sized to your requirements.

Typically, it is compute-type resources that you leave running that most quickly use up your budget. Turn these off when no longer needed, or better yet, delete them.

Example compute-type resources:

EC2, RDS, Cloud9, NAT Gateway or SageMaker instances
EMR, ECS or EKS clusters
Elastic Beanstalk applications
Use the AWS Simple Monthly Calculator or  AWS Pricing Calculator to estimate cost.  

For example, the estimate shown in the screenshot below calculated the cost of running the following resources for a month:

One t3.medium size Linux EC2 instance running 6 hours per day for a month in the us-east-1 Region.

One db.t2.small size MySQL RDS database with 20GB of storage, left running for a month in the us-east-1 Region.

One NAT Gateway left running, processing 1GB per month in the us-east-1 Region

cost estimate

Pricing is subject to change. The calculation above is only an example from a point in time in the past.

Additional suggestions for how to reduce cost:

Discover what resources exist in your account using the Tag Editor feature.

Note: This tool does not find all resource types, but it can locate many types.

Open the Resource Groups & Tag Editor console and choose Tag Editor.

For Regions, choose us-east-1 and us-west-2 and for Resource types, choose All supported resource types. Finally, choose Search resources.

Give the search a moment to complete. You will see a large number of warnings appear at the top of the screen, indicating that you do not have permissions to view certain resources. You can ignore these warnings.

Scroll down to the Resource search results panel to see the resources that were found.

Some of the resources already existed in your account when you started the lab and they will not use up a significant amount of your budget.  These include IAM resources, two Lambda functions, a number of security groups and other VPC-related resources.
However, you may notice other resources in the search results that are resources you created, and perhaps no longer need.
Build your solutions using CloudFormation templates.

You can use the service to create a stack that creates multiple resources across AWS services. Then, when you don't need the resources anymore, delete the stack (which will delete all the resources it created). You can always, use the same template to create a new stack to create the resources again during your next session.
Access AWS Trusted Advisor and review the cost optimization results. The service can help you to identify EC2 instances with low utilization rates, idle RDS instances or Classic Load Balancers, under utilized EBS volumes, and other conditions that can help you save the money remaining in your lab budget.

 

Accessing EC2 Instances
When launching EC2 instances in the default us-east-1 Region in this environment, choose the option to use the existing key pair named vockey at the time of launch.  Then:

Choose the  AWS Details link above these instructions.

If you are using a Windows desktop or laptop, choose the Download PPK button and save the labsuser.ppk file. You can use this file to connect via SSH to a Linux EC2 instance or Windows EC2 instance, typically using a tool such as PuTTY.
If you are using a MacOS desktop or laptop, choose the Download PEM button and save the labsuser.pem file. You can use this file to connect via SSH to a Linux EC2 instance or Windows EC2 instance, typically using a terminal window.
To connect via Remote Desktop to a Windows EC2 instance:

In the EC2 Console, choose Instances and choose the instance you want to connect to
From the Actions menu choose Get Windows Password
Next to Key Pair Path choose Browse.
Browse to and select the labsuser.pem file you downloaded earlier.
Choose Decrypt Password.
The connection information will now display, including the instance's Public DNS, Administrator user name, and the decrypted password.
Use a Remote Desktop Protocol (RDP) client to connect to the desktop of the EC2 instance using these connection details.
To connect using SSH to a Linux instance, see the next section.
SSH access to an EC2 Instance you launch
The steps below describe how to use the SSH key to connect to your instance.

Tip: Assuming you launched the instance with the vockey key pair, and that you have opened TCP port 22 in the instance's security group, you can also SSH to an EC2 instance by using the terminal to the side of these instructions. The terminal already has the key pair available to it. Simply enter the command ssh -i ~/.ssh/labsuser.pem ec2-user@<public-ip> where <public-ip> is the actual IPv4 public address of the instance.

 Windows Users: Using SSH to Connect
 These instructions are for Windows users only.

Download needed software.

You will use PuTTY to SSH to Amazon EC2 instances. If you do not have PuTTY installed on your computer, download it here.
Open putty.exe

Configure PuTTY to not timeout:

Choose Connection
Set Seconds between keepalives to 30
This allows you to keep the PuTTY session open for a longer period of time.

Configure your PuTTY session:

Choose Session
Host Name (or IP address): Copy and paste the IPv4 Public IP address for the instance. To find it, return to the EC2 Console and choose Instances. Check the box next to the instance and in the Description tab copy the IPv4 Public IP value.
Back in PuTTy, in the Connection list, expand  SSH
Choose Auth (don't expand it)
Choose Browse
Browse to and select the .ppk file that you downloaded
Choose Open to select it
Choose Open
Choose Yes, to trust the host and connect to it.

When prompted login as, enter: ec2-user

This will connect you to the EC2 instance.

 

macOS  and Linux  Users - Using SSH to Connect
These instructions are for Mac/Linux users only.

Read through the two bullet points in this step before you start to complete the actions, because you will not be able see these instructions when the AWS Details panel is open.

Choose the  AWS Details link above these instructions.

Choose the Download PEM button and save the labsuser.pem file.

Typically your browser will save it to the Downloads directory.

Open a terminal window, and change directory cd to the directory where the .pem file was downloaded.

For example, run this command, if it was saved to your Downloads directory:

cd ~/Downloads
Change the permissions on the key to be read only, by running this command:

chmod 400 labsuser.pem
Return to the AWS Management Console, and in the EC2 service, choose Instances.

Check the box next to the instance you want to connect to.

In the Description tab, copy the IPv4 Public IP value.

Return to the terminal window and run this command (replace <public-ip> with the actual public IP address you copied):

ssh -i <filename>.pem ec2-user@<public-ip>
Type yes when prompted to allow a first connection to this remote SSH server.

Because you are using a key pair for authentication, you will not be prompted for a password.

 

© 2022 Amazon Web Services, Inc. and its affiliates. All rights reserved. This work may not be reproduced or redistributed, in whole or in part, without prior written permission from Amazon Web Services, Inc. Commercial copying, lending, or selling is prohibited.