

jwt     = '@@{calm_jwt}@@'

headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer {}'.format(jwt)}

url = "https://localhost:9440/api/nutanix/v3/vms/@@{id}@@"

resp = urlreq(url, verb='GET', headers=headers, verify=False)

vm_update = json.loads(resp.content)

payload = {

  "metadata":{},

  "spec": {}

}

payload["metadata"]=vm_update["metadata"]

payload["spec"]=vm_update["spec"]

payload["spec"]["description"]="Created by Calm Application @@{calm_application_name}@@"

resp = urlreq(url,params=json.dumps(payload), verb='PUT', headers=headers, verify=False)

