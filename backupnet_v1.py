import oci

# Config and Client Init
config = oci.config.from_file()
search_client = oci.resource_search.ResourceSearchClient(config)
network_client = oci.core.VirtualNetworkClient(config)
# Search query 
resources_query = f"query vcn,subnet,securitylist,networksecuritygroup,servicegateway,internetgateway,natgateway,routetable,Drg,DrgAttachment,DrgRouteDistribution,DrgRouteTable,VirtualCircuit,RemotePeeringConnection,LocalPeeringGateway,Ipv6 resources"
resources_search_details = oci.resource_search.models.StructuredSearchDetails(query=resources_query)
resources_search_response = search_client.search_resources(resources_search_details)
# Get Resource's details
for resource in resources_search_response.data.items:
        if resource.resource_type.lower() == "vcn" : 
         resdetail = network_client.get_vcn(vcn_id=resource.identifier).data
        elif resource.resource_type.lower() == "subnet" : 
         resdetail = network_client.get_subnet(subnet_id=resource.identifier).data
        elif resource.resource_type.lower() == "securitylist" : 
         resdetail = network_client.get_security_list(security_list_id=resource.identifier).data
        elif resource.resource_type.lower() == "networksecuritygroup" : 
         resdetail = network_client.get_network_security_group(network_security_group_id=resource.identifier).data
        elif resource.resource_type.lower() == "servicegateway" : 
         resdetail = network_client.get_service_gateway(service_gateway_id=resource.identifier).data
        elif resource.resource_type.lower() == "internetgateway" : 
         resdetail = network_client.get_internet_gateway(ig_id=resource.identifier).data
        elif resource.resource_type.lower() == "natgateway" : 
         resdetail = network_client.get_nat_gateway(nat_gateway_id=resource.identifier).data
        elif resource.resource_type.lower() == "routetable" : 
         resdetail = network_client.get_route_table(rt_id=resource.identifier).data
        elif resource.resource_type == "Drg" : 
         resdetail = network_client.get_drg(drg_id=resource.identifier).data
        elif resource.resource_type == "DrgAttachment" : 
         resdetail = network_client.get_drg_attachment(drg_attachment_id=resource.identifier).data
        elif resource.resource_type == "DrgRouteDistribution" : 
         resdetail = network_client.get_drg_route_distribution(drg_route_distribution_id=resource.identifier).data
        elif resource.resource_type == "DrgRouteTable" : 
         resdetail = network_client.get_drg_route_table(drg_route_table_id=resource.identifier).data
        elif resource.resource_type == "VirtualCircuit" : 
         resdetail = network_client.get_virtual_circuit(virtual_circuit_id=resource.identifier).data
        elif resource.resource_type == "RemotePeeringConnection" : 
         resdetail = network_client.get_remote_peering_connection(remote_peering_connection_id=resource.identifier).data
        elif resource.resource_type == "LocalPeeringGateway" : 
         resdetail = network_client.get_local_peering_gateway(local_peering_gateway_id=resource.identifier).data
        elif resource.resource_type == "Ipv6" : 
         resdetail = network_client.get_ipv6(ipv6_id=resource.identifier).data
        # Write output to files
        with open(f"{resource.compartment_id}_{resource.resource_type}_{resource.display_name}.json", "w") as f:
          print(f"{resdetail}", file=f)

