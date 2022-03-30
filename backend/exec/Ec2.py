import boto3


class Ec2:
    def __init__(self, aws_access_key_id: str, aws_secret_access_key: str):
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.ec2 = boto3.client(
            "ec2",
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key,
            region_name="us-east-1",
        )
        self.ec2_resource = boto3.resource(
            "ec2",
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key,
            region_name="us-east-1",
        )

    def create_key_pair(self, key_pair_name: str):
        response = self.ec2.create_key_pair(KeyName=key_pair_name)
        return response

    def delete_key_pair(self, key_pair_name: str):
        response = self.ec2.delete_key_pair(KeyName=key_pair_name)
        return response

    def create_security_group(self, security_group_name: str):
        response = self.ec2.create_security_group(
            GroupName=security_group_name,
            Description="Security group generated by GCC",
        )
        self.ec2.authorize_security_group_ingress(
            GroupId=response["GroupId"],
            IpPermissions=[
                {
                    "IpProtocol": "tcp",
                    "FromPort": 0,
                    "ToPort": 65535,
                    "IpRanges": [{"CidrIp": "0.0.0.0/0"}],
                },
            ],
        )
        return response

    def delete_security_group(self, security_group_id: str):
        response = self.ec2.delete_security_group(GroupId=security_group_id)
        return response

    def create_instance(self, key_pair_name: str, security_group_id: str):
        response = self.ec2.run_instances(
            ImageId="ami-09e67e426f25ce0d7",
            MinCount=1,
            MaxCount=1,
            InstanceType="t2.micro",
            KeyName=key_pair_name,
            SecurityGroupIds=[security_group_id],
        )
        return response

    def terminate_instance(self, instance_id: str):
        response = self.ec2.terminate_instances(InstanceIds=[instance_id])
        return response
