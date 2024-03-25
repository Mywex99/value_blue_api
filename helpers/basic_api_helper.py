import json
import logging
import re

import httpx


class BasicHTTPApi:
    def __init__(self, url):
        self.base_url = url

    def call_api(self, url, **parameters) -> (int, dict):
        """
        Base GET request
        :param url:
        :param params:
        :return:
        """
        with httpx.Client() as client:
            sanitized_url = re.sub(r"(X-RapidAPI-Key)=.*&(password)=.*",
                                   r"\1=***&\2=***", url)

            logging.info(f'Trying to call: "{sanitized_url}"')

            headers = None
            if 'headers' in parameters:
                headers = parameters['headers']
            
            params = None
            if 'parameters' in parameters:
                params = parameters['parameters']

            response = client.get(url, headers=headers, params=params, timeout=None)
            if response.status_code >= 400:
                logging.info(f'Error message: {response.text}')
                result = response.text
            elif response.headers["content-type"].strip().startswith(
                    "text/plain"):
                print(response.headers["content-type"])
                result = response.text
            else:
                result = json.loads(response.text)
            return response.status_code, result

    def call_api_post(self, url, payload, headers=None) -> (int, dict):
        """
        Base POST request
        :param url:
        :param payload:
        :param headers:
        :return:
        """
        with httpx.Client() as client:
            sanitized_url = re.sub(r"(X-RapidAPI-Key)=.*&(password)=.*",
                                   r"\1=***&\2=***", url)

            data_str = json.dumps(payload)

            sanitized_payload = re.sub(r'(?<="X-RapidAPI-Key": ")[^"]*|(?<="password": ")[^"]*', '***', data_str)

            logging.info(f'Trying to call: "{sanitized_url} with payload: {sanitized_payload}"') # noqa

            if isinstance(payload, list) or isinstance(payload, dict):
                payload = json.dumps(payload)

            response = client.post(url, data=payload, headers=headers,
                                   timeout=None)
            if response.status_code >= 400:
                logging.info(f'Error message: {response.text}')
                result = response.text
            else:
                result = json.loads(response.text)
            return response.status_code, result
