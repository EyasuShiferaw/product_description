import os
import logging
import aisuite as ai
from dotenv import load_dotenv
from functools import lru_cache
import xml.etree.ElementTree as ET
from tenacity import retry, stop_after_attempt, wait_exponential


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__) 

# Load environment variables from .env file
load_dotenv()



@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=15))
def get_completion(messages: list[dict]) -> str:
    """ Generate a completion for the given messages and model.
    
    Args:
        messages (list): A list of messages, where each message is a dictionary with the following keys:
            - role: The role of the sender of the message, e.g. "user" or "system".
            - content: The text of the message.
        model (str): The model to use to generate the completion.
    
    Returns:
        str: The generated completion.
    """
    logger.info(f"Getting completion for messages:")
    client = ai.Client()
    client.configure({"openai" : {
  "api_key": os.environ.get("API_KEY"),
}})
    response = None
    model = "openai:gpt-4o"
    try:
        logger.info("Trying to get completion for messages")
        response = client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0.75
            )
    except Exception as e:
        logger.error(f"Error getting completion for messages.\nException: {e}")
        raise  # Allow @retry to handle the exception
    else:
        logger.info(f"successfully got completion for messages")
        return response.choices[0].message.content
    

  
def get_xml_data(xml_data: str) -> str:
    """ Remove any unnecessary data from the given XML data.
    
    Args:
        xml_data (str): The XML data to remove unnecessary data from.
    
    Returns:
        str: The cleaned XML data.
    """

    start_tag = "<DescriptionComponent>"
    end_tag = "</DescriptionComponent>"

    try:
        start_index = xml_data.index(start_tag)
        end_index = xml_data.index(end_tag) + len(end_tag)
        xml_string = xml_data[start_index:end_index]
    except Exception as e:
        logger.error(f"Error cleaning XML data.\nException: {e}")
        raise
    else:
        logger.info(f"Successfully cleaned XML data")
        return xml_string

def parse_xml(xml_string: str) -> list[dict]:
    """ Parse the XML string into a list of dictionaries.
    
    Args:
        xml_string (str): The XML string to parse.
    
    Returns:
        list[dict]: A list of dictionaries, where each dictionary contains the following keys:
            - StrategyName: The name of the strategy.
            - Headlines: A list of headlines.
            - Description: The description of the strategy.
            - Explanation: The explanation of the strategy. 
    """
    try:
        tree = ET.fromstring(xml_string)
       
    except Exception as e:
        logger.error(f"Error parsing XML string.\nException: {e}")
        raise
    else:
        parsed_dict = {
            "tagline": tree.find("Tagline").text if tree.find("Tagline") is not None else None,
            "description": tree.find("RefinedText").text if tree.find("RefinedText") is not None else None,
            "features": [
                feature.text for feature in tree.find("ProductFeatures").findall("Feature")
            ] if tree.find("ProductFeatures") is not None else None,
            "price": tree.find("Price").text if tree.find("Price") is not None else None,
        }
        logger.info(f"Successfully parsed XML string")
        return parsed_dict

def pipeline_for_xml_parse(xml_data: str) -> list[dict]:
    """ A pipeline for parsing XML data.

    Args:
        xml_data (str): The XML data to parse.
    
    Returns:
        list[dict]: A list of dictionaries, where each dictionary contains the following keys:
            - StrategyName: The name of the strategy.
            - Headlines: A list of headlines.
            - Description: The description of the strategy.
            - Explanation: The explanation of the strategy.
    """
    logger.info(f"Parsing XML string")  
    product_description = []
    try:
        cleaned_xml_data = get_xml_data(xml_data)
        product_description = parse_xml(cleaned_xml_data)
    except Exception as e:
        logger.error(f"Error in pipeline for XML parse.\nException: {e}")
        raise
    else:
        logger.info(f"Successfully parsed XML data")
        return product_description

    