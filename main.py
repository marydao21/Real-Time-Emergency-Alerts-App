# Import FastAPI modules
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import List, Dict
from datetime import datetime

# Create FastAPI app instance
app = FastAPI()

# Use static files in "static" folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load HTML templates from "templates" folder
templates = Jinja2Templates(directory="templates")

# Manage all connected users
class connection_handler:
    def __init__(self):
        # Store active WebSocket connections and map them to users IDs
        self.active_connections: Dict[WebSocket, int] = {}
        self.next_id = 1  # Start from User #1

    async def connect(self, websocket: WebSocket):
        # Accept WebSocket connection
        await websocket.accept()
        # Assign an incremental integer ID
        user_id = self.next_id
        self.active_connections[websocket] = user_id
        self.next_id += 1  # Increment ID for next user
        print(f"User {user_id} connected. Total users: {len(self.active_connections)}")
        return user_id  # Return the assigned ID

    def disconnect(self, websocket: WebSocket):
        # Remove the user from active connections
        user_id = self.active_connections.get(websocket, "Unknown")
        if websocket in self.active_connections:
            del self.active_connections[websocket]
            print(f"User {user_id} disconnected. Remaining users: {len(self.active_connections)}")

    async def broadcast(self, message: str):
        # Send a message to all connected users
        print(f"Broadcasting message: {message}")
        for connection in self.active_connections.keys():
            try:
                await connection.send_text(message)
            except Exception as e:
                print(f"Error sending message: {e}")

# Create an instance of connection_handler
users_manager = connection_handler()

# When someone visits the homepage "/", show them the index.html page
@app.get("/", response_class=HTMLResponse)
async def get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# WebSocket communication endpoint at "/ws"
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    # Accept the connection and assign ID
    user_id = await users_manager.connect(websocket)

    # Send user their ID
    await websocket.send_text(f"ID: {user_id}") 

    try:
        while True:
            # Wait for incoming message
            data = await websocket.receive_text()

            # Add timestamp and user ID
            timestamp = datetime.now().strftime('%H:%M:%S')
            broadcast_message = f"[{timestamp}] 🔔 User #{user_id}: {data}"

            # Broadcast the timestamped message to all users
            await users_manager.broadcast(broadcast_message)

    except WebSocketDisconnect:
        users_manager.disconnect(websocket)
        await users_manager.broadcast(f"🔔 User #{user_id} disconnected.")
