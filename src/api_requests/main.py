from operator import attrgetter
import requests

url = 'https://api.github.com/search/repositories'

query_string = '?q=sort=stars&order=asc&page=2'


def main():
    print('hello')
    response = requests.get(url + query_string)
    print(f"Response status code is: {response.status_code}")
    response_json = response.json()
    response_items = response_json['items']
    # prsorted(response_item[0].keys()))
    fields_to_print = ('name', 'owner', 'html_url', 'score', 'stargazers_count')

    pers = []

    def predicate(x):
        if x in fields_to_print:
            return True
        return False

    for item in response_items:
        per = dict.fromkeys(fields_to_print, '')
        for field in fields_to_print:
            value = item[field]
            if type(value) is dict:
                value = list(value.items())[0]
            per[field] = value
        pers.append(per)
    sorted_pers = sorted(pers, key=lambda x: x['stargazers_count'], reverse=True)
    print(*(per for per in sorted_pers), sep='\n')


if __name__ == '__main__':
    main()
