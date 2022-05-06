import requests

def connection(web):
    web_https = 'http://' + web
    # print(web_https)

    try:
        # print("try")
        response = requests.get(web_https)
    except:
        # print("Error")
        return -10
    
    # print("post exception")
    # print(response.status_code)
    
    return response.status_code
 