Here's comprehensive documentation for your Livestream Viewer application:

---

## **API Documentation**

### **Base URL**
`http://localhost:5000/api` (or your deployed backend URL)

---

### **1. Status Check**
**Endpoint:** `GET /api/status`  
**Purpose:** Verify backend and database connectivity  
**Response:**
```json
{
  "status": "operational",
  "timestamp": "2023-08-20T12:34:56.789Z",
  "services": {
    "database": "connected",
    "stream_service": "ready"
  }
}
```

---

### **2. Stream Configuration**
**Endpoint:** `GET /api/stream/config`  
**Purpose:** Get default stream settings  
**Response:**
```json
{
  "defaultStreamUrl": "rtsp://example.com/stream",
  "maxQuality": "1080p",
  "allowedFormats": ["rtsp", "hls"]
}
```

---

### **3. Overlay Management**

#### **Get All Overlays**
**Endpoint:** `GET /api/overlays`  
**Response:**
```json
[
  {
    "_id": "64e1a2b3a1b2c3d4e5f6g7h8",
    "type": "text",
    "content": "Live Now!",
    "x": 100,
    "y": 50,
    "width": "200px",
    "height": "50px"
  }
]
```

#### **Create Overlay**
**Endpoint:** `POST /api/overlays`  
**Body:**
```json
{
  "type": "text|image",
  "content": "Your text or image URL",
  "x": 0,
  "y": 0,
  "width": "100px",
  "height": "50px"
}
```
**Success Response (201 Created):**
```json
{
  "id": "64e1a2b3a1b2c3d4e5f6g7h8",
  "message": "Overlay created successfully"
}
```

#### **Update Overlay**
**Endpoint:** `PUT /api/overlays/:id`  
**Body:** (Same as create)  
**Success Response:**
```json
{
  "message": "Overlay updated successfully"
}
```

#### **Delete Overlay**
**Endpoint:** `DELETE /api/overlays/:id`  
**Success Response:**
```json
{
  "message": "Overlay deleted successfully"
}
```

---

## **User Documentation**

### **1. Setup Instructions**

#### **Prerequisites**
- Node.js (v16+)
- Python (v3.8+)
- MongoDB (local or Atlas)
- FFmpeg (for RTSP conversion)

#### **Installation**
1. **Backend:**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   pip install -r requirements.txt
   ```

2. **Frontend:**
   ```bash
   cd frontend
   npm install
   ```

#### **Environment Setup**
Create `.env` files:
- **Backend:**
  ```env
  MONGO_URI=mongodb+srv://<user>:<password>@cluster.mongodb.net/livestream_app
  DEFAULT_STREAM_URL=rtsp://your-stream-url
  ```
- **Frontend:**
  ```env
  VITE_API_BASE_URL=http://localhost:5000
  ```

---

### **2. Running the Application**

1. **Start Services:**
   ```bash
   # Terminal 1 - Backend
   python app.py

   # Terminal 2 - Stream Service
   python streaming_service.py

   # Terminal 3 - Frontend
   npm run dev
   ```

2. **Access Application:**
   Open `http://localhost:3000` in your browser

---

### **3. Using the Application**

#### **Setting Up Stream**
1. Navigate to **Settings** page
2. Enter RTSP URL (e.g., `rtsp://192.168.1.100/live.sdp`)
3. Click "Save"

#### **Adding Overlays**
1. Go to **Stream** page
2. Click "Add Overlay" button
3. Configure:
   - **Type**: Text or Image
   - **Content**: Text or Image URL
   - **Position**: X/Y coordinates
   - **Size**: Width/Height
4. Click "Save"

#### **Managing Overlays**
- **Edit**: Click on overlay → Modify properties → Update
- **Delete**: Click trash icon next to overlay
- **Reposition**: Drag and drop overlays on the stream

---

### **4. Troubleshooting**

| Issue | Solution |
|-------|----------|
| Stream not loading | Verify RTSP URL and FFmpeg service |
| Overlays not saving | Check MongoDB connection |
| 404 Errors | Ensure backend is running on port 5000 |
| CORS Errors | Verify `CORS(app)` is enabled in Flask |

---

### **5. Example Requests**

**Create Overlay (cURL):**
```bash
curl -X POST http://localhost:5000/api/overlays \
  -H "Content-Type: application/json" \
  -d '{"type":"text","content":"Live","x":10,"y":10,"width":"100px","height":"50px"}'
```

**Get Stream Config (JavaScript):**
```javascript
fetch('/api/stream/config')
  .then(res => res.json())
  .then(data => console.log(data));
```

---

This documentation covers all API endpoints and user workflows. For additional help, check the `README.md` in the project repository.
