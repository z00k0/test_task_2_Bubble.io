import os

from dotenv import load_dotenv
import requests

load_dotenv()

TOKEN = os.getenv('TOKEN')

company_id = "1650273372915x513529303645328100"
program_id = "1657278177011x992254828667994100"
user_data = {
    'id': "user12345",
    'completed_triggers': {
        '1657192011065x484248349166796800': True,
        '1657280847810x779969418519380000': True,
        '1657192562998x995619309758709800': True,
        '1658403761659x374192272556949500': True
    }
}

base_url = 'https://instapai-bubble.bubbleapps.io/version-test/api/1.1/obj/'
headers = {
    'Authorization': f'Bearer {TOKEN}'
}


def find_user_level(company_id, program_id, user_data):
    completed_triggers_list = [
        trigger for trigger in user_data['completed_triggers'] if user_data['completed_triggers'][trigger] is True
    ]
    r = requests.get(url=f'{base_url}programs/{program_id}', headers=headers).json()
    levels = r['response']['levels']
    for level in levels:
        r = requests.get(url=f'{base_url}levels/{level}', headers=headers).json()
        boosters = r['response']['boosters']
        for booster in boosters:
            r = requests.get(url=f'{base_url}boosters/{booster}', headers=headers).json()
            trigger = r['response']['trigger']
            if trigger not in completed_triggers_list:
                return level
    return 'All levels completed'


completed_level = find_user_level(company_id, program_id, user_data)

print(completed_level)
