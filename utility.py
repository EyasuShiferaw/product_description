import os
import re
import json
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
                temperature=1.0
            )
    except Exception as e:
        logger.error(f"Error getting completion for messages.\nException: {e}")
        raise  # Allow @retry to handle the exception
    else:
        logger.info(f"successfully got completion for messages")
        return response.choices[0].message.content

@lru_cache(maxsize=1000)
def extract_with_regex(xml_data: str) -> dict:
    """
    Extracts key elements from a structured XML-like string using regex.

    Args:
        xml_data (str): The structured string containing the data.
    
    Returns:
        dict: A dictionary with extracted elements or None if missing.
    """
    try:
        # Define regex patterns for each key
        tagline_pattern = r"<Tagline>(.*?)</Tagline>"
        refined_text_pattern = r"<RefinedText>(.*?)</RefinedText>"
        features_pattern = r"<ProductFeatures>(.*?)</ProductFeatures>"
        price_pattern = r"<Price>(.*?)</Price>"
        
        # Extract data using regex
        tagline = re.search(tagline_pattern, xml_data, re.DOTALL)
        refined_text = re.search(refined_text_pattern, xml_data, re.DOTALL)
        features = re.search(features_pattern, xml_data, re.DOTALL)
        price = re.search(price_pattern, xml_data, re.DOTALL)
        
        # Process the features list
        features_list = None
        if features:
            features_list = re.findall(r"<Feature>(.*?)</Feature>", features.group(1), re.DOTALL)
        
        # Build the dictionary
        return {
            "tagline": tagline.group(1).strip() if tagline else None,
            "description": refined_text.group(1).strip() if refined_text else None,
            "features": [feature.strip() for feature in features_list] if features_list else None,
            "price": price.group(1).strip() if price else None
        }
    except Exception as e:
        logger.error(f"Error extracting with regex.\nException: {e}")
        raise

@lru_cache(maxsize=100)
def brand_style(path: str, keys: str | list[str]) -> dict:
    """
    Extract the brand communication styles from the given JSON file.
    Args:
        path (str): Path to the JSON file containing brand communication styles.
        keys (str | list): The brand communication style key(s) to look up. 
                           Can be a single key (str) or a list of keys (list).
    
    Returns:
        dict: A dictionary containing the brand style information for the given key(s).
              Contains 'Description', 'Keywords', and 'Tagline' fields for each key.
              Returns an empty dictionary if none of the keys are found.
    """
    logger.info(f"Getting brand styles for key(s): {keys}")

    # Ensure keys is always a list for uniform processing
    if isinstance(keys, str):
        try:
            # Try to parse the string as JSON
            parsed_keys = json.loads(keys)
            if isinstance(parsed_keys, list):
                keys = parsed_keys
            else:
                keys = [keys]
        except json.JSONDecodeError:
            # If parsing fails, treat as a single key string
            keys = [keys]


    with open(path, "r") as file:
        data = json.load(file)
    
    result = {}
    for key in keys:
        key = key.strip()  # Remove any whitespace around the key
        try:
            communication_style = data[key]
            result[key] = communication_style
            logger.info(f"Successfully got brand style for key: {key}")
        except KeyError:
            logger.error(f"Brand communication style '{key}' not found in communication styles")
    
    if not result:
        logger.warning("No matching keys were found.")
    
    return result
