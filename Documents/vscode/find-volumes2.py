import boto3
xyz=boto3.client('ec2')
Volume_resp= xyz.describe_volumes( 
    Filters= [
        {
            'Name': 'status',
            'Values': ['available']
        }
    ],
)
    #looping with vol
for vol in Volume_resp['Volumes']:
     print(vol['VolumeId'])
     print(vol['Size'])
     # delete volume with Id
xyz.delete_volume (VolumeId = vol["VolumeId"])