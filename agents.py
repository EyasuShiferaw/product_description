import logging
from functools import lru_cache
from prompt import agent1_system, agent2_system, agent3_system, agent1_user, agent2_user, agent3_user
from utility import get_completion
from dotenv import load_dotenv

load_dotenv()
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__) 

class ProductDescriptionGenerator:
    def __init__(self,product_name: str, key_features: str, target_customer: str, brand_communication_style: str, price: str):
        self.product_name = product_name
        self.key_features = key_features
        self.target_customer = target_customer
        self.brand_communication_style = brand_communication_style
        self.price = price
        self.product_description = None
        self.feedback = None
        self.final_product_description = None
    
    def __str__(self):
            return f"ProductDescriptionGenerator(product_name={self.product_name}, product_category={self.product_category}, key_features={self.key_features}, target_customer={self.target_customer}, brand_communication_style={self.brand_communication_style})"
    
    @lru_cache(maxsize=1000)
    def agent1(self):
        """
        Generate the first version of the product description
        """
        logger.info(f"Generating product description agent one start")
        messages = [
            {"role": "system", "content": agent1_system},
            {"role": "user", "content": agent1_user.format(product_name=self.product_name, key_features=self.key_features, target_customer=self.target_customer, brand_communication_style=self.brand_communication_style)}
        ]
        try:
            self.product_description  = get_completion(messages=messages)
        except Exception as e:
            logger.error(f"Can't generate ad\nException: {e}")
            return None
        else:

            logger.info("successfully generated ad")
        logger.info(f"Generating product description agent one finished")
       
    @lru_cache(maxsize=1000)   
    def agent2(self):
        """
        Generate the second version of the product description
        """
        logger.info(f"Generating product description agent two start")
        messages = [
            {"role": "system", "content": agent2_system},
            {"role": "user", "content": agent2_user.format(product_description=self.product_description, key_features=self.key_features, target_customer=self.target_customer, brand_communication_style=self.brand_communication_style)}
        ]
        try:
            self.feedback = get_completion(messages=messages)
        except Exception as e:
            logger.error(f"Can't generate ad\nException: {e}")
            return None
        else:
            logger.info("successfully generated ad")
        logger.info(f"Generating product description agent two finished")

    @lru_cache(maxsize=1000)
    def  agent3(self):
        """
        Generate the final version of the product description
        """
        logger.info(f"Generating product description agent three start")
        messages = [
            {"role": "system", "content": agent3_system},
            {"role": "user", "content": agent3_user.format(product_description=self.product_description, feedback=self.feedback, price=self.price, product_name=self.product_name, key_features=self.key_features, target_customer=self.target_customer, brand_communication_style=self.brand_communication_style)}
        ]
        try:
            self.final_product_description = get_completion(messages=messages)
        except Exception as e:
            logger.error(f"Can't generate ad\nException: {e}")
            return None
        else:
            logger.info(f"Generating product description agent three finished")

    def agent_pipeline(self):
        """
        Run the pipeline of the agents
        """
        self.agent1()
        if self.product_description is None:                
            return None
        logger.info(f"Product description agent one finished. {self.product_description}")
        self.agent2()
        if self.feedback is None:
            return None
        logger.info(f"Product description agent two finished. {self.feedback}")
        self.agent3()
        if self.final_product_description is None:
            return None
        logger.info(f"Product description agent three finished. {self.final_product_description}")
        return self.final_product_description

    