import requests
from dataclasses import dataclass

from bs4 import BeautifulSoup

from . import exceptions

@dataclass
class SampleTest:
    input_text: str
    output_text: str


def handle_http_status(status_code: int, link: str):
    match status_code:
        case 404 | 400:
            raise exceptions.invalid_link_exception(link)
        case 403 | 401:
            raise exceptions.no_access_exception()
        case 500:
            raise exceptions.server_error_exception()


def check_hostname(link: str):
    hostnames = ['codeforces.com']

    current_hostname = link.split('https://')[1].split('/')[0]

    if current_hostname not in hostnames:
        raise exceptions.invalid_hostname_exception(current_hostname)


def download_cf_task(link: str) -> str: 
    check_hostname(link)
    req = requests.get(link)
    handle_http_status(req.status_code, link)

    return req.text


def parse_cf_task_tests(content: str) -> list[SampleTest]:
    soup = BeautifulSoup(content, features="html5lib")
    samples_tags = soup.find_all('div', class_='sample-test')
    result_samples = []

    for sample in samples_tags:
        input_ = sample.find('div', class_='input').find('pre').string
        output = sample.find('div', class_='output').find('pre').string
        result_samples.append(SampleTest(input_text=input_, output_text=output)) 

    return result_samples


def write_samples(url_link: str): 
    samples = parse_cf_task_tests(content=download_cf_task(url_link))
    final_content = ''

    for sample_test in samples:
        final_content += sample_test.input_text + '\n'
        final_content += sample_test.output_text + '\n'


    with open('samples.txt', 'w') as file:
        file.write(final_content)


