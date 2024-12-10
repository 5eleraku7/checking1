from curl_cffi import requests

print(f'Claim Nodepay Multiple Account {nodetoken}') 
nodetoken = 'userAll.txt'

def claim():
    try:
        no = input('1:daily\n15:7days\n16:14days\n17:21days\n18:28days\nnomer claim: ').strip()
        with open(nodetoken, 'r') as file:
            local_data = file.read().splitlines()
            for tokenlist in local_data:
                url = f"https://api.nodepay.org/api/mission/complete-mission?"
                headers = {
                    "Authorization": f"Bearer {tokenlist}",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
                    "Content-Type": "application/json",
                    "Origin": "https://app.nodepay.ai",
                    "Referer": "https://app.nodepay.ai/"
                }
                
                data = {
                    "mission_id":no
                }

                response = requests.post(url, headers=headers, json=data, impersonate="chrome110")
                is_success = response.json().get('success')
                if is_success == True:
                    print(f'Claim Reward Success!')
                    print(response.json())
                else:
                    print(f'Reward Already Claimed! Or Something Wrong!')
    except requests.exceptions.RequestException as e:
        print(f"Error : {e}")
    
claim()
