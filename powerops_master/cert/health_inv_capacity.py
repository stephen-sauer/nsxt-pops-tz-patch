#############################################################################################################################################################################################
#                                                                                                                                                                                           #
# NSX-T Power Operations                                                                                                                                                                    #
#                                                                                                                                                                                           #
# Copyright 2020 VMware, Inc.  All rights reserved				                                                                                                                            #
#                                                                                                                                                                                           #
# The MIT license (the “License”) set forth below applies to all parts of the NSX Power Operations project.  You may not use this file except in compliance with the License.               #
#                                                                                                                                                                                           #
# MIT License                                                                                                                                                                               #
#                                                                                                                                                                                           #
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"),                                        #
# to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,                                        #
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:                                                #
#                                                                                                                                                                                           #
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.                                                            #
#                                                                                                                                                                                           #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,                                       #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,                             #
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.                                #
#                                                                                                                                                                                           #
# *--------------------------------------------------------------------------------------* #                                                                                                #
# **************************************************************************************** #                                                                                                #
#   VMware NSX-T PowerOps by @dominicfoley & @stephensauer                                 #                                                                                                #
#   A day 2 operations tool for helping to document and healthcheck an NSX-T environment   #                                                                                                #
# **************************************************************************************** #                                                                                                #
# *--------------------------------------------------------------------------------------* #                                                                                                #
#                                                                                                                                                                                           #
#############################################################################################################################################################################################

import requests
import urllib3
from _cert import Crt, Key, headers, nsx_mgr

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def main():
    session = requests.session()
    session.verify = False
    session.cert = (Crt, Key)

    ########### SECTION FOR REPORTING ON NSX-T MANAGER CAPACITY NETWORKING ###########
    nsx_inv_cap_url = '/api/v1/capacity/usage?category=inventory'
    nsx_inv_cap_json = requests.get(nsx_mgr + str(nsx_inv_cap_url), headers=headers, cert=(Crt, Key), verify=session.verify).json()

    print('')
    print('------------------------------------ NSX INVENTORY CAPACITY -----------------------------------')
    print('|  Name                                                 | Current  | Max Supported | Usage %  |')
    print('-----------------------------------------------------------------------------------------------')

    data = nsx_inv_cap_json['capacity_usage']
    cap_inv = len(data)
    for n in range(cap_inv):
        print('{:<60s}{:>4d}{:>12d}{:>15.1f}'.format(data[n]['display_name'],data[n]['current_usage_count'],data[n]['max_supported_count'],data[n]['current_usage_percentage']))
    print('-----------------------------------------------------------------------------------------------')
    print('')

if __name__ == "__main__":
    main()
