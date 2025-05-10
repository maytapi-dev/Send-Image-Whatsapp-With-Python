## 🖼️ WhatsApp Image Messaging API (Python)  
Send image messages via WhatsApp using Maytapi's API with Python.

## 🚀 Features  
- Send image messages via public URLs  
- Send images using Base64 encoded strings  
- Optional captions for images  
- Uses `requests` for lightweight HTTP calls  
- Environment variable support with `.env`  

## 📦 Installation  
Install the required packages:

```bash
pip install requests python-dotenv
```
## 🔧 Usage Example
```python
from whatsapp_api import WhatsAppAPI  # Or import from your file

api = WhatsAppAPI(
    product_id="YOUR_PRODUCT_ID",
    phone_id="YOUR_PHONE_ID",
    api_token="YOUR_API_TOKEN"
)

# Send image via URL
response = api.send_image_message(
    to="1234567890",
    image_url="https://example.com/image.jpg",
    caption="Check out this image!"
)
print(response)

# Send image via Base64
response = api.send_image_from_base64(
    to="1234567890",
    base64_data="data:image/jpeg;base64,...",
    caption="Base64 image message"
)
print(response)

```
## 🔒 Authentication  
Ensure you have the following credentials:  
- Product ID  
- Phone ID  
- API Token

## 📝 Methods  
- `send_image_message()`: Send image via URL  
- `send_image_from_base64()`: Send image using Base64 encoding

## 🔍 Error Handling  
The library provides comprehensive error logging and raises exceptions on HTTP errors.

## 📜 License  
MIT License

## 🤝 Support  
For issues or questions, please open a GitHub issue.
