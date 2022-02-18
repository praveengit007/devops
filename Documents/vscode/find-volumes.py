import boto3
xyz = boto3.client("ec2")
volume_resp = xyz.describe_volumes()
for volume in volume_resp['Volumes']:
    if volume['State']== 'available':
        print(volume["VolumeId"])
        print(volume["Size"])
        # delete volumes now
xyz.delete_volume(VolumeId= volume["VolumeId"])