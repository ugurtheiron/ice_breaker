import os
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from third_parties.linkedin import scrape_linkedin_profile


if __name__ == "__main__":
    load_dotenv()
    # print("Hello, World!")
    # print(os.environ["OPENAI_API_KEY"])

    # Promt
    linkedin_template =  """
    given the Linkedin information {information} about a person I want you to create:
    1. A short summary of the person
    2. two interesting facts about them
    """
    linkedin_template = PromptTemplate(
        input_variables=["information"], template=linkedin_template
    )

    # Model
    llm = ChatOpenAI(temperature=0.1, model_name="gpt-3.5-turbo")

    # Chain
    chain = linkedin_template | llm

    linkedin_data = scrape_linkedin_profile(linkdin_profile_url="https://www.linkedin.com/in/ugur-ozdemir/",mock=True)
    # linkedin_data = scrape_linkedin_profile(linkdin_profile_url="https://www.linkedin.com/in/ayse-karaca-816622135/")

    # Run
    res = chain.invoke(input={"information": linkedin_data})
    print(res.content)

