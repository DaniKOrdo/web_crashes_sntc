import http.client

def connection(web):
    conn = http.client.HTTPSConnection(web)
    try:
        print("conn.req " + conn.request("HEAD", "/"))
        conn.request("HEAD", "/")
        
        res = conn.getresponse().status
        print("status:" + res)
        if(res == 200):
            print("bien" + res)
            return True
        else:
            print("caida" + res)
            return False
    except:
        print("MAL")
        return False
    