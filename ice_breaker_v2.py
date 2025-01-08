import os
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser

from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

from parsers import FinalResponse, CategoryNotFound, Category


product = "running shoes"

if __name__ == "__main__":
    load_dotenv()
    # print("Hello, World!")
    # print(os.environ["OPENAI_API_KEY"])

    # Promt
    kategory_template = """
    You are an assistant tasked with classifying product information.
    
    Product: {product}

    Do NOT use any other category suggestion exept the "Categories" list below.     
    Categories: [
        "Hunting",
        "Athletics",
        "Aikido",
        "Badminton",
        "Ballet",
        "Fishery",
        "Basketball",
        "Billiards",
        "Riding",
        "Bicycle",
        "Boxing",
        "Bushcraft",
        "Baseball",
        "Ice Hockey",
        "Ice Skating",
        "Bowling",
        "Dive",
        "Fitness",
        "Football",
        "Futsal",
        "Golf",
        "Wrestling",
        "Handball",
        "Hiking, Trekking, Outdoor",
        "Gymnastics and Trampoline",
        "Judo",
        "Camp",
        "Canoe and SUP",
        "Skiing, Snowboarding",
        "Running and Walking",
        "Karate",
        "Cricket",
        "Spade",
        "E-Sports",
        "Ping Pong",
        "Motorcycle",
        "Archery and Target Sports",
        "Orienteering",
        "Padel",
        "Skate, Skateboard, and Scooter",
        "Pickleball",
        "Pilates, Light Fitness Training",
        "Beach Tennis, Speedball",
        "Wind Sports",
        "Surfing",
        "Sporty Child and Physical Education",
        "Squash",
        "Tennis",
        "Climbing and Mountaineering",
        "Volleyball",
        "Windsurfing",
        "Sail",
        "Yoga",
        "Swimming"
    ]

    Find the products category above the list. If the product category is not found, return a warning message.
    
    Provide the result in strict JSON format as shown below and if the product category is not found, return a warning message:
    if the product category is found:
    {{
        "final_output": {{
            "predicted_category": "Category Name",
            "prediction_possibility": 0.95
        }}
    }}

    If the product category is not found:
    {{
        "final_output": {{
            "warning": "product category not found!"
        }}
    }}
    """
    kategory_promt = PromptTemplate(
        input_variables=["product"], template=kategory_template
    )
    # kategory_promt = PromptTemplate(input_variables="product_description", output_variables="category", template=kategory_template)

    # Model
    llm = ChatOpenAI(temperature=0.1, model_name="gpt-4o")
    # llm = ChatOllama(model="llama3.1:8b")

    # output parser
    parser = PydanticOutputParser(pydantic_object=FinalResponse)

    # Chain
    # chain = kategory_promt | llm | StrOutputParser()
    chain = kategory_promt | llm | parser

    # Run
    res = chain.invoke(input={"product": product})
    print(res)

