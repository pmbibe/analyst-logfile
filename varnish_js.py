import json
import ast
import gc


class process():
    def host(abc):
        host = str(abc["host"])
        return host
    def client_ip(abc):
        client_ip = str(abc["client_ip"])
        return client_ip
    def time_write_log(abc):
        time_write_log = str(abc["time_write_log"])
        return time_write_log
    def bytes_sent_client(abc):
        bytes_sent_client = str (abc["bytes_sent_client"])
        return bytes_sent_client
    def request_time_tmp(abc):
        request_time_tmp = str (abc["request_time_tmp"]) 
        return request_time_tmp
    def varnish_handling(abc):
        varnish_handling = abc["varnish_handling"]
        return varnish_handling
    def uri(abc):
        uri = abc["uri"]
        return uri
    def response(abc):
        response = abc["response"]
        return response
    def user_agent(abc) :
        user_agent = abc["user_agent"]
        return user_agent

def main():
 
    client_IP = []

    Host = []
    time_RL = []
    byte_SC = []
    Request_tm = []
    fout = open('20191107.txt','a+')
    i = 0
    for i in range(1):
        gc.collect()
        data_f = open('output/result%d.txt'%(i),'r')
        data = data_f.read()
        hi = data.split("\n")
        for item in hi:
            try:
                ok = json.loads(item)
                a = str(process.host(ok))
                b = process.client_ip(ok)
                c = str(process.time_write_log(ok).split("T")[1])
                d = process.bytes_sent_client(ok)
                e = int(process.request_time_tmp(ok))
                uri = process.uri(ok)
                user_agent = process.user_agent(ok)
                response = process.response(ok)
                varnish_handling = process.varnish_handling(ok)
#        if  e > 6000000 and varnish_handling =="hit":
#                if b == '14.183.206.212' and e > 6000000:
#                if e > 6000000:
#               print (str(b) + "--" + c.split("+")[0] + "--" + varnish_handling + "--" + str(e))
#                fout.write(str(b) + "--" + c.split("+")[0] + "--" + varnish_handling + "--" + str(e))
#                fout.write("\n")
#                       print (uri + "-" + str(e) + "-" + c.split("+")[0])
#               print (user_agent)
#client_IP.append(b)
#               Host.append(c)
#        l = client_IP
#       for team in [ele for ind, ele in enumerate(l,1) if ele not in l[ind:]]:
#           print("IP: {} Counter: {}".format(team,l.count(team)))
            except:
                pass
        print (i)
        data_f.close()

        

main()

