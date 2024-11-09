# Wi-Fi QR Code Generator

## Overview
The Wi-Fi QR Code Generator is a simple Python application that allows users to generate QR codes for Wi-Fi networks they are currently connected to. This tool enables easy sharing of Wi-Fi credentials by generating a QR code that others can scan to connect directly to the network.

## Key Features
- **Wi-Fi QR Code Generation**: Automatically generates a QR code for the Wi-Fi network you are connected to.
- **Easy Sharing**: Quickly share your Wi-Fi credentials without needing to type out the password.
- **User-Friendly Interface**: Designed to be simple and intuitive, ideal for all levels of users.
- **Windows Support**: This tool is specifically built for Windows users.
- **Language**: Available in English.

## Technical Details
- **Platform**: Windows
- **User Interface Framework**: PySide6 (Qt for Python)
- **QR Code Library**: QR-Code
- **Programming Language**: Python 3.x

## Installation
### Prerequisites
- Python 3.x
- PySide6
- QR-Code library

### Installation Steps
1. **Clone the repository**:
    ```bash
    git clone https://github.com/tkb/wifi-pass.git
    ```
2. **Navigate to the project directory**:
3. **Install the required dependencies**:
    ```bash
    pip install wifi-qrcode-generator
   pip install PySide6
    ```

### Running the Application
1. After installation, run the application by executing the following command:
    ```bash
    python wifi_qr_generator.py
    ```

2. The program will automatically detect the Wi-Fi network you are currently connected to, and generate a QR code that you can share.

## How to Use
1. **Open the application**: Launch the program by running the Python script `main.py`.
2. **QR Code Generation**: Once the app is open, it will detect the Wi-Fi network you're connected to and generate a QR code for that network.
3. **Scan the QR Code**: To share the Wi-Fi credentials, others can scan the QR code using their device's camera or any QR code scanning app. The device will automatically connect to the network without needing to enter the password manually.

## Limitations
- **Wi-Fi Compatibility**: The software may not work with all Wi-Fi networks, particularly those with advanced security configurations or non-standard setups.
- **Windows Only**: This software is designed to work exclusively on Windows operating systems. It does not currently support other platforms like macOS or Linux.

## Acknowledgments
- **PySide6**: For building the graphical user interface.
- **QR-Code**: For QR code generation.
- **Python**: For being the powerful language behind the application.
