import oci
import json
region = 'eu-paris-1'
network_endpoint = "https://iaas." + region + ".oraclecloud.com"
search_endpoint = "https://search." + region + ".oraclecloud.com"

config = oci.config.from_file()
network_client = oci.core.VirtualNetworkClient(config, service_endpoint=network_endpoint)


with open("test.json") as json_file:
    json_data = json.load(json_file)
    cidr_blocks = json_data['cidr_blocks']
    cidr_block = json_data['cidr_block']
    compartment_id = json_data['compartment_id']
    ipv6_private_cidr_blocks = json_data['ipv6_private_cidr_blocks']
    display_name = json_data['display_name']
    dns_label = json_data['dns_label']
    freeform_tags = json_data['freeform_tags']

create_vcn_response = network_client.create_vcn(
    create_vcn_details=oci.core.models.CreateVcnDetails(
        compartment_id=compartment_id,
        cidr_blocks=cidr_blocks,
        ipv6_private_cidr_blocks=ipv6_private_cidr_blocks,
        display_name=display_name,
        dns_label=dns_label,
        freeform_tags=freeform_tags))

# Get the data from response
print(create_vcn_response.data)