from collections import namedtuple

# Set the object type "Question" as a Named Tuple, enabling us to call it section by section in the main program
Question = namedtuple("Question", "question choices correct")

# Create the Question objects and ensure each one has a different variable name so they can be referenced by the Opponent objects
# All the questions that belong to the Solutions Architect Associate Course
saa_questions =  [

    # Question 7 from practice test
    Question("""An application saves the logs to an S3 bucket. A user wants to keep the logs for one month for
troubleshooting purposes, and then purge the logs.

What feature will enable this?""", 
    # The possible answers
    [
        "Adding a bucket policy on the S3 bucket.", 
        "Configuring lifecycle configuration rules on the S3 bucket.", 
        "Creating an IAM policy for the S3 bucket.", 
        "Enabling CORS on the S3 bucket."
    ], 
    # The correct answer
    "b"), 

    # Question 3 from practice test
    Question("""Company salespeople upload their sales figures daily. A Solutions Architect needs a durable storage
solution for these documents that also protects against users accidentally deleting important
documents.

Which action will protect against unintended user actions?""", 
    # The possible answers
    [
        "Store data in an EBS volume and create snapshots once a week.", 
        "Store data in an S3 bucket and enable versioning.", 
        "Store data in two S3 buckets in different AWS regions.", 
        "Store data on EC2 instance storage."], 
    # The correct answer
    "b"),

    # Question 5 from practice test
    Question("""A Solutions Architect is designing a critical business application with a relational database that runs
on an EC2 instance. It requires a single EBS volume that can support up to 16,000 IOPS.

Which Amazon EBS volume type can meet the performance requirements of this application?""", 
    # The possible answers
    [
        "EBS Provisioned IOPS SSD", 
        "EBS Throughput Optimized HDD", 
        "EBS General Purpose SSD", 
        "EBS Cold HDD"
    ], 
    # The correct answer
    "a"),

    # Question 8 from practice test
    Question("""An application running on EC2 instances processes sensitive information stored on Amazon S3. The
information is accessed over the Internet. The security team is concerned that the Internet
connectivity to Amazon S3 is a security risk.

Which solution will resolve the security concern?""", 
    # The possible answers
    [
        "Access the data through an Internet Gateway.", 
        "Access the data through a VPN connection.", 
        "Access the data through a NAT Gateway.", 
        "Access the data through a VPC endpoint for Amazon S3."], 
        # The correct answer
        "d"),

    # Question 4 from practice test
    Question("""An application requires a highly available relational database with an initial storage capacity of 8 TB.
The database will grow by 8 GB every day. To support expected traffic, at least eight read replicas will
be required to handle database reads.

Which option will meet these requirements?""", 
    # The possible answers
    [
        "DynamoDB", 
        "Amazon S3", 
        "Amazon Aurora", 
        "Amazon Redshift"], 
        # The correct answer
        "c"),  

    # Question 6 from practice test
    Question("""A web application allows customers to upload orders to an S3 bucket. The resulting Amazon S3
events trigger a Lambda function that inserts a message to an SQS queue. A single EC2 instance
reads messages from the queue, processes them, and stores them in an DynamoDB table partitioned
by unique order ID. Next month traffic is expected to increase by a factor of 10 and a Solutions
Architect is reviewing the architecture for possible scaling problems.

Which component is MOST likely to need re-architecting to be able to scale to accommodate the new traffic?""", 
    # The possible answers
    [
        "Lambda function", 
        "SQS queue", 
        "EC2 instance", 
        "DynamoDB table"], 
        # The correct answer
        "c"),

    # Question 1 from practice test
    Question("""A company is storing an access key (access key ID and secret access key) in a text file on a custom
AMI. The company uses the access key to access DynamoDB tables from instances created from the
AMI. The security team has mandated a more secure solution.

Which solution will meet the security team’s mandate?""", 
    # The possible answers
    [
        "Put the access key in an S3 bucket, and retrieve the access key on boot from the instance.", 
        "Pass the access key to the instances through instance user data.", 
        "Obtain the access key from a key server launched in a private subnet.", 
        "Create an IAM role with permissions to access the table, and launch all instances with the new role."], 
        # The correct answer
        "d"),

    # Question 10 from practice test
    Question("""A Solutions Architect is designing an online shopping application running in a VPC on EC2 instances
behind an ELB Application Load Balancer. The instances run in an Auto Scaling group across
multiple Availability Zones. The application tier must read and write data to a customer managed
database cluster. There should be no access to the database from the Internet, but the cluster must
be able to obtain software patches from the Internet.

Which VPC design meets these requirements?""", 
    # The possible answers
    [
        "Public subnets for both the application tier and the database cluster", 
        "Public subnets for the application tier, and private subnets for the database cluster", 
        "Public subnets for the application tier and NAT Gateway, and private subnets for the database cluster", 
        "Public subnets for the application tier, and private subnets for the database cluster and NAT Gateway"], 
        # The correct answer
        "c")   
]