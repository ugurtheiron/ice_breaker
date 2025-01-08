import os
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

product = """
    tennis ball 
"""

if __name__ == "__main__":
    load_dotenv()
    # print("Hello, World!")
    # print(os.environ["OPENAI_API_KEY"])

    # Promt
    kategory_template = """
    You are an assistant tasked with classifying product {product} information.

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

    Match the product to the most appropriate category.
    write "possiblity" between 0~1.


    if no matching category detected:
    Warning: product category not found!

    Provide the result in a format. Here's an example:

    predicted category: "Category Name"
    """
    kategory_promt = PromptTemplate(
        input_variables=["product"], template=kategory_template
    )
    # kategory_promt = PromptTemplate(input_variables="product_description", output_variables="category", template=kategory_template)

    # Model
    llm = ChatOpenAI(temperature=0.1, model_name="gpt-3.5-turbo")

    # Chain
    chain = kategory_promt | llm

    # Run
    res = chain.invoke(input={"product": product})
    print(res.content)

