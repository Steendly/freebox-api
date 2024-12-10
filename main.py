import requests
from pprint import pprint

api_url = "http://mafreebox.freebox.fr/"
api_version = "v8"
freebox_info = requests.get(api_url + "/api_version").json()
api_url = "https://" + freebox_info["api_domain"] + ":" + f"{freebox_info["https_port"]}" + freebox_info["api_base_url"] + api_version
print("API base url : " + api_url)

pprint(requests.get(api_url + "/login", verify="server.pem").json())
