import requests
import time
import sys
import os
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def main(TOKEN,user_icon_dir):
    url = "https://slack.com/api/users.list"
    headers = {"Authorization": "Bearer {}".format(TOKEN)}
    session = requests.Session()
    session.mount(
            "https://slack.com/",
            HTTPAdapter(max_retries=Retry(total=5, backoff_factor=3)),
        )
    response = session.get(url, headers=headers, timeout=3)
    for i, member in enumerate(response.json()['members']):
        if((member['name'] in ['slackbot']) or (member['is_bot'] == True)):
            continue
        else:
            image512px_url = member['profile']['image_512']
            print(i + 1, image512px_url)
            response = requests.get(image512px_url)
            response.raise_for_status()
            filename = f"./{user_icon_dir}/{member['id']}.jpg"
            with open(filename, 'wb') as f:
                f.write(response.content)
            time.sleep(1)
    print('end')


if __name__ == '__main__':
    if(len(sys.argv)<2):
        token = input('TOKEN : ')
    else:
        token = sys.argv[1]

    user_icon_dir = "user_icon"
    if not os.path.exists(user_icon_dir):
        # ディレクトリが存在しない場合、ディレクトリを作成する
        os.makedirs(user_icon_dir)

    main(token,user_icon_dir)
