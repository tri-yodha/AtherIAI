# AtherAI: AI-Powered Educational Animation Platform

## Project Overview

AtherAI is an AI-powered platform that transforms text descriptions into professional animations, making educational content creation more accessible and efficient.

## System Requirements

- Python 3.8+
- Node.js 18+
- pip
- npm or yarn

## Project Structure

```
atherai/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── src/
│
├── frontend/
│   ├── src/
│   │   └── app.jsx
│   ├── package.json
│   └── vite.config.js
```

## Setup and Installation

### Backend Setup

1. Navigate to the backend directory
   ```bash
   cd backend
   ```

2. Create a virtual environment
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install Python dependencies
   ```bash
   pip install -r requirements.txt
   ```

5. Run the backend server
   ```bash
   python main.py
   ```

### Frontend Setup

1. In a new terminal, navigate to the frontend directory
   ```bash
   cd frontend
   ```

2. Install npm dependencies
   ```bash
   npm install
   ```

3. Start the frontend development server
   ```bash
   npm run dev
   ```

## Running the Application

1. First, start the backend server (step 5 in Backend Setup)
2. Then, start the frontend development server (step 3 in Frontend Setup)
3. Open a web browser and navigate to the local development URL (typically http://localhost:3000)

## Technology Stack

### Frontend
- React 18+
- TypeScript
- Next.js 14+
- Tailwind CSS
- Vite

### Backend
- FastAPI (Python)
- GraphQL
- PyTorch
- TensorFlow

### AI Infrastructure
- GPT-4 API
- IBM Granite Model

## Deployment

- Containerized with Docker
- Kubernetes for orchestration
- Supports cloud and self-hosted deployments


## Troubleshooting

- Ensure all dependencies are correctly installed
- Check that backend server is running before starting frontend
- Verify Python and Node.js versions meet minimum requirements
- Check network ports are not blocked

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

License - MIT
```


