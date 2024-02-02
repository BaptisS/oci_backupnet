import oci
import json
import os
region = 'eu-paris-1'
network_endpoint = "https://iaas." + region + ".oraclecloud.com"
search_endpoint = "https://search." + region + ".oraclecloud.com"

config = oci.config.from_file()
network_client = oci.core.VirtualNetworkClient(config, service_endpoint=network_endpoint)

with open("testigw.json", 'r') as json_file:
    json_data = json.load(json_file)
    oldid = json_data['id']
    compartment_id = json_data['compartment_id']
    display_name = json_data['display_name']
    defined_tags = json_data['defined_tags']
    freeform_tags = json_data['freeform_tags']
    vcn_id = json_data['vcn_id']
    route_table_id = json_data['route_table_id']
    is_enabled = json_data['is_enabled']


create_internet_gateway_response = network_client.create_internet_gateway(
    create_internet_gateway_details=oci.core.models.CreateInternetGatewayDetails(
        compartment_id=compartment_id,
        display_name = display_name,
        freeform_tags = freeform_tags,
        vcn_id = vcn_id,
        route_table_id=route_table_id,
        is_enabled=is_enabled))

# Get the data from response
print(create_internet_gateway_response.data)
newid = create_internet_gateway_response.data.id

#update files with new resource ocid
files = [entry for entry in os.scandir() if entry.name.endswith('.json')]

for file in files:
    with open(file, 'r') as f:
        content = f.read().replace(oldid, newid)
    with open(file, 'w') as f:
        f.write(content)
