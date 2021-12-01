import requests

def email_breach(email, api, output):
    try:
        header= {"X-Key": f"{api}"}
        r=requests.get(f"https://api.binaryedge.io/v2/query/dataleaks/email/{email}", headers=header)
        data=r.json()
        with open(output, 'a') as file:
            print("Email to look for in the breaches :", data['query'])
            file.writelines("Email to look for in the breaches : %s\n" %(data['query']))
            print("Number of sources where breach happened :", data['total'])
            file.writelines("Number of sources where breach happened : %s\n" %(data['total']))
            for i in range(0, len(data['events'])):
                print("Source :",data['events'][i])
                file.writelines("Source :%s\n" %(data['events'][i]))
            

    except Exception as e:
        print(e)


def domain_breach(domain, api, output):
    try:
        header= {"X-Key": f"{api}"}
        r=requests.get(f"https://api.binaryedge.io/v2/query/dataleaks/organization/{domain}", headers=header)
        data=r.json()
        with open(output, 'a') as file:
            print("Domain to look for in the breaches :", data['query'])
            file.writelines("Domain to look for in the breaches : %s\n" %(data['query']))
            print("Number of sources where breach happened :", data['total'])
            file.writelines("Number of sources where breach happened : %s\n" %(data['total']))
            for i in range(0, len(data['groups'])):
                print("Source :",data['groups'][i]['leak'])
                file.writelines("Source :%s\n" %(data['groups'][i]['leak']))
            

    except Exception as e:
        print(e)


        
        
