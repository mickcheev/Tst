import requests
from dataclasses import dataclass

from bs4 import BeautifulSoup


@dataclass
class SampleTest:
    input_text: str
    output_text: str

def download_cf_task(link: str) -> str:
    req = requests.get(link)
    if req.status_code != 200:
        raise Exception('Invalid url adress')
    else:
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

