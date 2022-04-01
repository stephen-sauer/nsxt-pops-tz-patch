Clone of the NSX-T PowerOps CLI - Used for Patch testing

Not an April's Fool: Udocs_logical_switches.py updated to take into account an issue related to "replication-mode" when hitting a VLAN LS/Segment. 


### Build & Run
To run NSX-T PowerOps:

1. From /home/powerops git clone the repo (following will clone the master branch of NSX-T PowerOps):
    * `git clone https://github.com/stephen-sauer/nsxt-pops-tz-patch`

2. Modify the config.yml with all the relevant information (NSX IP or FQDN, cert path, output folder for XLS files)
    
3. Source 'run_powerops' from /home/powerops/nsx-powerops (source ./run_powerops) 

### License 
NSX Power Operations

Copyright 2020 VMware, Inc.  All rights reserved                

The MIT license (the ìLicenseî) set forth below applies to all parts of the NSX Power Operations project.  You may not use this file except in compliance with the License.†

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

### Notice
NSX Power Operations

Copyright (c) 2020 VMware, Inc. All Rights Reserved. 

This product is licensed to you under the MIT license (the "License").  You may not use this product except in compliance with the MIT License.  

This product may include a number of subcomponents with separate copyright notices and license terms. Your use of these subcomponents is subject to the terms and conditions of the subcomponent's license, as noted in the LICENSE file. 

### Contact Info
Dominic Foley (dfoley@vmware.com) and Stephen Sauer (sauers@vmware.com)
