import boto3
import snappy.utils.constants as Consts
from snappy.utils import helper as Helper

class Instance:

    def __init__(self, json) -> None:

        # Declare empty values 
        self.id = json["InstanceId"]
        self.name = None
        self.private_ip = None
        self.root_volume = None
        self.volumes = None

        # Retrieve instance name
        if "Tags" in json:

            for tag in json["Tags"]:

                if(tag["Key"].lower() == "name"):

                    self.name = tag["Value"]
        
        # Retrieve IP Address
        if "PrivateIpAddress" in json:

            self.private_ip = json["PrivateIpAddress"]


        # Retrieve volume IDs

        # Check if volumes exists before continuing
        if "BlockDeviceMappings" not in json:
            raise Exception(Consts.EXCEPTION_MESSAGE_VOLUMES_NOT_FOUND.format(self.private_ip))

        # Get the root volume device name
        if "RootDeviceName" in json:
            root_volume_device_name = json["RootDeviceName"]

            # Filter the root volume ID
            root_volume_data = next((filter(lambda t: t["DeviceName"] == root_volume_device_name, json["BlockDeviceMappings"])), None)
        
            if root_volume_data is not None:
                self.root_volume = root_volume_data["Ebs"]["VolumeId"]

        # Get all volume IDs
        self.volumes = [volume["Ebs"]["VolumeId"] for volume in json["BlockDeviceMappings"]]

    def snap_root(self, tags_specifications=None) -> str:
        
        # Check if root volume is present
        if self.root_volume is None:
            raise Exception(Consts.EXCEPTION_MESSAGE_ROOT_VOLUME_NOT_FOUND)

        # Create EC2 client 
        client = boto3.client('ec2')

        # Define Mandatory Tags
        mandatory_tags = [Consts.template_snapshot_tag_timestamp(Helper.format_today(), self.name)]
        
        # Reformat tags scpefications
        if tags_specifications != None and tags_specifications != []:
            
            # Add passed tags
            mandatory_tags = mandatory_tags + tags_specifications
            
            formated_tags_specs = [
                {
                    'ResourceType': 'snapshot',
                    'Tags': mandatory_tags
                },
            ]
            
        else:
            formated_tags_specs = [
                {
                    'ResourceType': 'snapshot',
                    'Tags': mandatory_tags
                },
            ]
            
        # Create snapshot
        response = client.create_snapshot(
            Description=Consts.MESSAGE_DESCRIPTION_SNAPSHOT.format(self.name) if self.name != None else Consts.MESSAGE_DESCRIPTION_SNAPSHOT.format(self.private_ip),
            VolumeId=self.root_volume,
            TagSpecifications=formated_tags_specs
        )
        
        # Return the output
        return Consts.template_snapshot_output(response["SnapshotId"], self.name, self.root_volume)

    def snap_all(self, tags_specifications=None):

        # Create EC2 client 
        client = boto3.client('ec2')

        # Reformat tags scpefications
        if tags_specifications != None and tags_specifications != []:
            formated_tags_specs = [
                {
                    'ResourceType': 'snapshot',
                    'Tags': tags_specifications
                },
            ]
        else:
            formated_tags_specs = []

        # Create a snapshot description
        if self.name != None:
            snapshot_description = Consts.MESSAGE_DESCRIPTION_SNAPSHOT.format(self.name)
        else:
            snapshot_description = Consts.MESSAGE_DESCRIPTION_SNAPSHOT.format(self.private_ip)

        # Create snapshots
        response = client.create_snapshots(
            Description=snapshot_description,
            InstanceSpecification={
                'InstanceId': self.id,
                'ExcludeBootVolume': False
            },
            TagSpecifications=formated_tags_specs
        )
        
        # Return the snapshot ID list
        return response["Snapshots"]


            




        