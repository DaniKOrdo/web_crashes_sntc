import http.client

def connection(web):
    conn = http.client.HTTPSConnection(web)
    try:
        conn.request("HEAD", "/")
        res = conn.getresponse()
        return True
    except:
        return False
    
