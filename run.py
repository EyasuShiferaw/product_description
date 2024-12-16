import os
import logging
from pathlib import Path
from para2pdf import generate_pdf
from agents import ProductDescriptionGenerator
from utility import extract_with_regex, brand_style

from dotenv import load_dotenv

load_dotenv()


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__) 


def main():

    # Get the directory of the current script (run.py)
    script_dir = Path(__file__).parent
    json_path = script_dir / 'brand_communication.json'
    
    price = os.environ.get('price', 'default_value')
    key_features = os.environ.get('key_features', 'default_value')
    product_name = os.environ.get('product_name', 'default_value')
    target_customer = os.environ.get('target_customer', 'default_value')
    tagline = os.environ.get('tagline', 'default_value')
    brand_communication_style = os.environ.get('brand_communication_style', 'default_value')


    

    if product_name == 'default_value' or product_name == '':
        logger.error(f"Can't generate ad, please provide product_name")
        return f"Can't generate ad, please provide product_name"
    if key_features == 'default_value' or key_features == '':
        logger.error(f"Can't generate ad, please provide key_features")
        return f"Can't generate ad, please provide key_features"
    if target_customer == 'default_value' or target_customer == '':
        logger.error(f"Can't generate ad, please provide target_customer")
        return f"Can't generate ad, please provide target_customer"
    if tagline == 'default_value' or tagline == '':
        logger.error(f"Can't generate ad, please provide tagline")
        return f"Can't generate ad, please provide tagline"
    if brand_communication_style == 'default_value' or brand_communication_style == '':
        logger.error(f"Can't generate ad, please provide brand_communication_style")
        return f"Can't generate ad, please provide brand_communication_style" 
    if price == 'default_value' or price == '':
        logger.error(f"Can't generate ad, please provide price")
        return f"Can't generate ad, please provide price"
    
    try:
        communication_style = brand_style(json_path, brand_communication_style)
    except Exception as e:
        logger.error(f"Can't generate ad\nException: {e}")
        return f"Can't generate ad\nException: {e}"
    
    communication_style["tagline"] = tagline
    

    product_description_generator = ProductDescriptionGenerator(product_name, key_features, target_customer, communication_style, price)
    temp_product_description = product_description_generator.agent_pipeline()

    try:
        product_description = extract_with_regex(temp_product_description)
    except Exception as e:
        logger.error(f"Error extracting with regex.\nException: {e}")
        return f"Error extracting with regex.\nException: {e}"
    
    product_description["name"] = product_name

   
    
    if product_description is None:
        logger.error(f"Can't generate product description")
        product_description = f"Can't generate product description"
    
 
    # Define the path for the 'output' folder inside the script's directory
    output_dir = script_dir / 'output'
    output_dir.mkdir(exist_ok=True)  # Create 'output' directory if it doesn't exist

    # Define the file path within the 'output' directory
    output_file = str(output_dir / 'result2.pdf')

    generate_pdf(product_description, output_file)
    

if __name__ == "__main__":
    main()    

