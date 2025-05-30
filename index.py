"""
Python Example: How to send message with image on WhatsApp API

This module provides functionality to send image messages via WhatsApp API using Maytapi.
"""

import requests
import json
import os
from typing import Dict, Any, Optional


class WhatsAppAPI:
    """WhatsApp API client for sending image messages using Maytapi."""

    def __init__(self, product_id: str, phone_id: str, api_token: str):
        """
        Initialize the WhatsApp API client.

        Args:
            product_id: Your Maytapi product ID
            phone_id: Your Maytapi phone ID
            api_token: Your Maytapi API token
        """
        self.product_id = product_id
        self.phone_id = phone_id
        self.api_token = api_token
        self.base_url = f"https://api.maytapi.com/api/{product_id}/{phone_id}"
        self.headers = {
            "Content-Type": "application/json",
            "x-maytapi-key": api_token
        }

    def send_image_message(
        self, 
        to: str, 
        image_url: str, 
        caption: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Send image message using a URL.

        Args:
            to: Recipient's phone number with country code (e.g., "1234567890")
            image_url: URL of the image to send
            caption: Optional caption for the image

        Returns:
            API response as a dictionary
        """
        endpoint = f"{self.base_url}/sendMessage"
        
        payload = {
            "to_number": to,
            "type": "image",
            "message": caption or "",
            "image": image_url
        }
        
        response = requests.post(endpoint, headers=self.headers, json=payload)
        response.raise_for_status()  # Raise exception for HTTP errors
        
        return response.json()

    def send_image_from_base64(
        self, 
        to: str, 
        base64_data: str, 
        caption: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Send image message using base64 encoded data.

        Args:
            to: Recipient's phone number with country code (e.g., "1234567890")
            base64_data: Base64 encoded image data (should start with "data:image/...")
            caption: Optional caption for the image

        Returns:
            API response as a dictionary
        """
        endpoint = f"{self.base_url}/sendMessage"
        
        payload = {
            "to_number": to,
            "type": "image",
            "message": caption or "",
            "image": base64_data
        }
        
        response = requests.post(endpoint, headers=self.headers, json=payload)
        response.raise_for_status()  # Raise exception for HTTP errors
        
        return response.json()


# Example usage
if __name__ == "__main__":
    # Load environment variables
    from dotenv import load_dotenv
    load_dotenv()
    
    # Get credentials from environment variables
    product_id = os.getenv("PRODUCT_ID")
    phone_id = os.getenv("PHONE_ID")
    api_token = os.getenv("API_TOKEN")
    
    if not all([product_id, phone_id, api_token]):
        print("Error: Missing environment variables. Please set PRODUCT_ID, PHONE_ID, and API_TOKEN")
        exit(1)
    
    # Initialize the API
    api = WhatsAppAPI(product_id, phone_id, api_token)
    
    # Example: Send image message
    try:
        response = api.send_image_message(
            to="1234567890",  # Replace with actual phone number
            image_url="https://example.com/image.jpg",
            caption="Check out this image!"
        )
        print(f"Message sent: {response}")
    except Exception as e:
        print(f"Error sending message: {e}")
