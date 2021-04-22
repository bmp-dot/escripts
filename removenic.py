###################### DECLARE VARIABLES ######################

uri = "https://localhost:9440/api/nutanix/v3"
vm_uuid = "@@{id}@@"

# establish credentials

username = '@@{Creds_PrismCentral.username}@@'
username_secret = '@@{Creds_PrismCentral.secret}@@'


###################### DO NOT MODIFY BELOW HERE ######################
#
######################     DEFINE FUNCTIONS     ######################

# define the function 'rest_call'
# this encapsulates the api call.
def rest_call(url, method, payload="", username=username, username_secret=username_secret):

# we put the accept statement in here to ensure that we will only accept it in json.
    headers = {
        'Content-type': 'application/json',
        'Accept': 'application/json'
    }

    if payload:
        resp = urlreq(
            url,
            verb=method,
            params=json.dumps(payload),
            auth="BASIC",
            user=username,
            passwd=username_secret,
            headers=headers,
            verify=False
        )
    else:
        resp = urlreq(
            url,
            verb=method,
            auth="BASIC",
            user=username,
            passwd=username_secret,
            headers=headers,
            verify=False
        )
# put in a try\catch block to ensure that we have json returned
    if resp.ok:
        try:
            return json.loads(resp.content)
        except:
            return resp.content
    else:
        print("Request failed")
        print("Headers: {}".format(headers))
        print("Payload: {}".format(json.dumps(payload)))
        print('Status code: {}'.format(resp.status_code))
        print('Response: {}'.format(json.dumps(
            json.loads(resp.content), indent=4)))
        exit(1)

######################## GET VM SPEC ########################
url = "{}/vms/{}".format(
    uri,
    vm_uuid
)
# Define the method (get\put\post, etc)
method = 'GET'

# create a variable - use the function 'rest_call' to populate the function.
response = rest_call(url=url, method=method)

######################## Change\update the  VM SPEC ########################
# delete 'status' element from json response
del response['status']


# delete NIC position 1
del response['spec']['resources']['nic_list'][1]

# set the method
method = 'PUT'
# create the 'payload' object from the updated 'response' object
payload = response

# 
response = rest_call(url=url, method=method, payload=payload)
print(response)