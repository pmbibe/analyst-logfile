import json

def main():
    data = open("20191107.txt","r")
    fout = open('list20191107.txt','w')
    data_read = str(data.read()).split("\n")
    ip_list = []
    time_list = []
    for item in data_read:
        ip = item.split("--")[0]
        time = item.split("--")[1]
        ip_list.append(ip)
        time_list.append(time)
#        if ip == "14.183.206.212":
#            print (time)
    l = ip_list
    for team in [ele for ind, ele in enumerate(l,1) if ele not in l[ind:]]:
        print("{}${}".format(team,l.count(team)))
#        fout.write("{}${}".format(team,l.count(team)))
#        fout.write("\n")
main()
