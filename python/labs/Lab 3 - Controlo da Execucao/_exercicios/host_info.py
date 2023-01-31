
import sys
import re
import ipaddress
from socket import gethostbyname_ex, gethostbyaddr, gaierror, herror


class NetworkError(Exception):
    """
    Any network error, like "host not found", timeouts, etc.
    """
    pass


def get_host_info(server_addr):
    """
    Returns the server ip and hostname for server_addr. This param may
    either be an IP address, in which case this function tries to query
    its hostname, or vice-versa.
    This functions raises a ValueError exception if the host name in
    server_addr is ill-formed, and raises NetworkError if we can't get
    an IP address for that host name.
    """
    try:
        ipaddress.ip_address(server_addr)
    except ValueError:
        # server_addr not a valid ip address, then it might be a 
        # valid hostname
        if not is_valid_hostname(server_addr):
            raise ValueError("Invalid hostname: %s" % (server_addr))
        server_name = server_addr
        try:
            # gethostbyname_ex returns the following tuple: 
            # (hostname, aliaslist, ipaddrlist)
            server_ip = gethostbyname_ex(server_name)[2][0]
        except gaierror:            
            raise NetworkError("Unknown server: %s." % server_name)
    else:  
        # server_addr is a valid ip address, get the hostname
        # if possible
        server_ip = server_addr
        try:
            # returns a tuple like gethostbyname_ex
            server_name = gethostbyaddr(server_ip)[0]
        except herror as ex:
            server_name = ''
    return server_ip, server_name   


def is_valid_hostname(hostname):
    """
    From: http://stackoverflow.com/questions/2532053/validate-a-hostname-string
    See also: https://en.wikipedia.org/wiki/Hostname (and the RFC 
    referenced there)
    """
    if len(hostname) > 255:
        return False
    if hostname[-1] == ".":
        # strip exactly one dot from the right, if present
        hostname = hostname[:-1]
    allowed = re.compile("(?!-)[A-Z\d-]{1,63}(?<!-)$", re.IGNORECASE)
    return all(allowed.match(x) for x in hostname.split("."))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Utilização: host_info <host_ip or host_name>", file=sys.stderr)
    else:
        server_addr = sys.argv[1]
        try:            
            print(get_host_info(server_addr))
        except (ValueError, NetworkError) as ex:
            print(ex, file=sys.stderr)

