import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkdin_profile_url: str, mock: bool = False):
    """
    scrape information from LinkedIn profiles,
    Manually scrape the information from LinkedIn profiles.
    """

    if mock:
        # Path to the JSON file
        file_path = "third_parties\linkedin_profiles\linkedin_call.json"

        # Read the JSON file
        with open(file_path, "r") as file:
            data = json.load(file)

    else:
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        header_dic = {"Authorization": f'Bearer {os.getenv("PROXYCURL_API_KEY")}'}
        params = {
            'linkedin_profile_url': linkdin_profile_url,
            'extra': 'include',
            'personal_contact_number': 'include',
            'personal_email': 'include',
            'inferred_salary': 'include',
            'skills': 'include',
            'use_cache': 'if-present',
            'fallback_to_cache': 'on-error',
        }
        response = requests.get(
            api_endpoint, 
            headers=header_dic, 
            params=params,
            timeout=10,
        )
        data = response.json()

    return data

if __name__ == "__main__":
    print(scrape_linkedin_profile("https://www.linkedin.com/in/ugur-ozdemir/", mock=True))