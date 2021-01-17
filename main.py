import requests
import datetime
token = "7asdafa8f6a43a4f6e"
username = "lazyminds0499"
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)  # this will give us a response  data from the api

graph_id = "graph1"
graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
graph_config = {
    "id": graph_id,
    "name": "working hours",
    "unit": "min",
    "type": "int",
    "color": "momiji",
}
headers = {
    "X-USER-TOKEN": token
}

# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(graph_response.text)

pixela_post_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}"
# today = datetime.datetime.now()
today = datetime.datetime(year=2020, month=12, day=29)
post_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "300",
}
print(today.strftime("%Y%m%d"))
# post_response = requests.post(url=pixela_post_endpoint, json=post_config, headers=headers)
# print(post_response.text)

update_endpoint = f"{pixela_post_endpoint}/{today.strftime('%Y%m%d')}"

update_config = {
    "quantity": "400"
}
# update_response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(update_response.text)
delete_response = requests.delete(url=update_endpoint, headers=headers)
print(delete_response.text)