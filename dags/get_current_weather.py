import requests
import json, time
from datetime import datetime

def main():
    base_url = 'http://api.weatherapi.com/v1/current.json'

    params = {
        'key':'c59e017c4d4348ae81a112456240707',
        'q':'Philippines',
        'aqi':'no'
    }
    n = 0
    while n < 3:
        response = requests.get(url=base_url,params=params)
        response = response.json()

        current_time = response['location']['localtime']
        current_time = datetime.strptime(current_time, '%Y-%m-%d %H:%M')
        current_time = current_time.strftime("%Y%m%d%H%M")

        filepath = 'resources\source\weather_' + current_time + '.json'

        response = str(json.dumps(response, indent=4))

        with open(filepath,"w") as outfile:
            outfile.write(response)
        outfile.close()
        print(n)
        n = n + 1
        print(n)
        if n < 3:
            time.sleep(5)

if __name__ == '__main__': 
    main()


