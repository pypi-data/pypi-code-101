import re

def has_errors(previous_instances, retrieved_instances):
    
    # Check if some instances were not retrieved
    return len(previous_instances) != len(retrieved_instances)

def retrieve_failed_instances(previous_instances, retrieved_instances):
    
    # Organize previous instances
    previous_ip_addresses, previous_hostnames = organize_instances(previous_instances)
    
    # Get retrieved instances
    retrieved_ip_addresses = [instance.private_ip for instance in retrieved_instances]
    retrieved_hostnames = [instance.name for instance in retrieved_instances]
    
    return (
        [ip for ip in previous_ip_addresses if ip not in retrieved_ip_addresses] + 
        [hostname for hostname in previous_hostnames if hostname not in retrieved_hostnames]
    )

def is_an_ip_address(data):
    # Checks whether a given string
    # has ip address format
    pat = re.match("^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", data)
    return bool(pat)

def organize_instances(instances_raw):
    # Return ip_addresses, hostnames
    return [ip for ip in instances_raw if is_an_ip_address(ip)], [hostname for hostname in instances_raw if not is_an_ip_address(hostname)]