import manageritm

manageritm_addr = "localhost"
manageritm_port = "8000"

# create a manageritm client
mc = manageritm.client.ManagerITMClient(f'http://{manageritm_addr}:{manageritm_port}')
proxy_details = mc.client()

print(f"proxy port: {proxy_details['port']}")
print(f"proxy webport: {proxy_details['webport']}")

# start a proxy server
mc.proxy_start()

# set your application to use the proxy
#  host: "localhost"
#  port: f"{proxy_details['port']}"

# do some work...

# stop the proxy server
mc.proxy_stop()
