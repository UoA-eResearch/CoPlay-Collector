# This file defines your configuration
#subnet = "192.168.20.1/24" # To scan an IP range
ips = ["192.168.20.26"] # An alternative to skip the scan, if your IPs are known

# Database config
host = "api-proxy.auckland-cer.cloud.edu.au"
user = "quest"
password = "quest"
database = "quest"

# Desired installed apps and versions. Set to [] to disable this check
apps = [
    {
        "packageName": "nz.ac.auckland.eresearch.prx_fishtank",
        "versionName": "4.0.0"
    }
]