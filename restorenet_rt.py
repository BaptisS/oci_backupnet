import oci
import json
import os
region = 'eu-paris-1'
network_endpoint = "https://iaas." + region + ".oraclecloud.com"
search_endpoint = "https://search." + region + ".oraclecloud.com"

config = oci.config.from_file()
network_client = oci.core.VirtualNetworkClient(config, service_endpoint=network_endpoint)

with open("testrt.json") as json_file:
    json_data = json.load(json_file)
    oldid = json_data['id']
    route_rules = json_data['route_rules']
    compartment_id = json_data['compartment_id']
    display_name = json_data['display_name']
    defined_tags = json_data['defined_tags']
    freeform_tags = json_data['freeform_tags']
    vcn_id = json_data['vcn_id']

rr =[]
for rule in route_rules:
  rr.append(oci.core.models.RouteRule(
        destination = rule['destination'],
        destination_type = rule['destination_type'],
        network_entity_id = rule['network_entity_id'],
        description = rule['description']))

create_route_table_response = network_client.create_route_table(
    create_route_table_details=oci.core.models.CreateRouteTableDetails(
        compartment_id=compartment_id,
        display_name = display_name,
        freeform_tags = freeform_tags,
        vcn_id = vcn_id,
        route_rules= rr))

print(create_route_table_response.data)
newid = create_route_table_response.data.id
files = [entry for entry in os.scandir() if entry.name.endswith('.json')]
for file in files:
    with open(file, 'r') as f:
        content = f.read().replace(oldid, newid)
    with open(file, 'w') as f:
        f.write(content)
