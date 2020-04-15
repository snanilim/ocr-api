import requests
from bs4 import BeautifulSoup



def scrapNidSite(url, nid, dob):
    try:
        headers = {
            'Set-Cookie': 'laravel_session=eyJpdiI6Ikh6VmV4VkZhZW1KQlNyTDlxMFd2TUE9PSIsInZhbHVlIjoiODRJVzlPd2EzbE9YNVErY2VXRjZpc1k4dE5HcUN2eUhidmJXYXJsOXJFVDJVS2dqblJPMzJXc09DeG04Z3lYVSIsIm1hYyI6IjliMmRlOTUxZmJkNDQ4YjMyOWU5MzNmMTAxM2NiMjg1YmJjOTY5YmQwOTUyMzZmZTNiMzQwYzNmYTM0NGY4MWEifQ%3D%3D'
        }
        payload = {
            'nid': nid,
            'dob': dob
        }

        with requests.Session() as session:
            res = session.get(url)

            soup = BeautifulSoup(res.text, "html.parser")
            token = soup.select_one('input[name="_token"]')['value']
            payload['_token'] = token
            
            response = session.post(url, data=payload, headers=headers)
            # print('response', response)
            soup = BeautifulSoup(response.text, "html.parser")
            # print('soup', soup)

            all_data = {}

            field_ids = [ 'nid', 'dob', 'name', 'occupation', 'bangla_name', 'father', 'mother', 'blood', 'gender', 'present', 'parmanent' ]

            for fid in field_ids:
                value = soup.find(id=fid)
                value = value.get_text()
                all_data[fid] = value


            # print('all_data', all_data)
            return all_data
    except Exception as error:
        print('scrapNidSite', error)
        return error

