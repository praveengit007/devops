import boto3
xyz=boto3.client ("ec2")

xyz.start_instances(
    InstanceIds=["i-01abf19c7ce7ade83", ]
)
