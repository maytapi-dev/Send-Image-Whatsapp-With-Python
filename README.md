# 🖼️ WhatsApp Image Messaging API for Python | Send Images via WhatsApp Business API

> **Professional WhatsApp Business API Integration** - Send image messages programmatically using Python with Maytapi's powerful WhatsApp API. Perfect for businesses, developers, and automation projects.

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![WhatsApp API](https://img.shields.io/badge/WhatsApp-Business%20API-25D366.svg)](https://maytapi.com/)
[![Maytapi](https://img.shields.io/badge/Powered%20by-Maytapi-orange.svg)](https://maytapi.com/)

## 🌟 Overview

This Python library provides a seamless integration with **WhatsApp Business API** for sending image messages programmatically. Built specifically for developers who need reliable WhatsApp messaging capabilities in their applications, chatbots, marketing automation, or business communication systems.

**Perfect for:** E-commerce notifications, customer support, marketing campaigns, automated reporting, and business communication workflows.

## 🔗 Essential Links & Resources

| Resource | Description | Link |
|----------|-------------|------|
| 🌐 **Official Website** | Maytapi WhatsApp API Platform | [Visit Site](https://maytapi.com/) |
| 🔐 **Developer Console** | Manage API keys and configurations | [Login Here](https://console.maytapi.com/login) |
| 💰 **Pricing & Plans** | Flexible pricing for all business sizes | [View Pricing](https://maytapi.com/whatsapp-api-pricing) |
| 📖 **API Documentation** | Complete developer documentation | [Read Docs](https://maytapi.com/whatsapp-api-documentation) |
| 🚀 **Live Demo** | Try the API in action | [Demo Page](https://maytapi.com/demo) |
| 💬 **24/7 Support** | Get help from our expert team | [Contact Support](https://maytapi.com/support) |

## ⭐ Key Features & Capabilities

### 📤 **Image Sending Methods**
- ✅ **URL-based Image Sending** - Direct image URLs (JPEG, PNG, GIF, WebP)
- ✅ **Base64 Image Encoding** - Send images from local files or memory
- ✅ **Image Captions** - Add descriptive text to your images
- ✅ **Bulk Image Messaging** - Send to multiple recipients

### 🛠️ **Developer-Friendly Features**
- ✅ **Lightweight HTTP Requests** - Built with `requests` library
- ✅ **Environment Variables** - Secure credential management with `.env`
- ✅ **Comprehensive Error Handling** - Detailed error messages and logging
- ✅ **Type Hints** - Full Python typing support
- ✅ **Async Support** - Optional asynchronous operations
- ✅ **Rate Limit Management** - Built-in request throttling

### 🔒 **Security & Reliability**
- ✅ **Secure API Authentication** - Token-based security
- ✅ **HTTPS Encryption** - All communications encrypted
- ✅ **Request Validation** - Input sanitization and validation
- ✅ **Retry Mechanisms** - Automatic retry for failed requests

---

## 📦 Kurulum

Kütüphaneyi kullanmak için aşağıdaki paketleri yükleyin:

```bash
pip install requests python-dotenv
```
## 🔧 Usage Example
```python
from whatsapp_api import WhatsAppAPI

api = WhatsAppAPI(
    product_id="YOUR_PRODUCT_ID",
    phone_id="YOUR_PHONE_ID",
    api_token="YOUR_API_TOKEN"
)

# URL üzerinden görsel gönder
api.send_image_message(
    to="905XXXXXXXXX",
    image_url="https://example.com/image.jpg",
    caption="İşte gönderdiğim görsel!"
)

# Base64 formatında görsel gönder
api.send_image_from_base64(
    to="905XXXXXXXXX",
    base64_data="data:image/jpeg;base64,...",
    caption="Base64 görsel mesajı"
)
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
