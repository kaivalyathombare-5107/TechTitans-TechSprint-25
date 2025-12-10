# TechTitans-TechSprint-25
A 3D Digital Twin Simulator for Contract Farming using Unity & Google Gemini. Built for Tech Sprint AI Hack '25.

AgriTwin: Digital Twin for Contract Farming 🚜
Tech Sprint AI Hack '25 Submission

Tagline: "Don't sign blindly. Simulate first."

1. The Problem
Farmers in India (specifically Nashik) sign complex contract farming agreements without understanding the risks.

They cannot predict how Weather + Soil + Contract Terms interact to determine final profit.

Result: Exploitation and financial loss.

2. The Solution
AgriTwin is a 3D Simulator (Digital Twin) that visualizes the financial outcome of a contract before a seed is planted.

Input: Farmer builds their land in 3D and uploads a contract PDF.

Processing: Google Gemini analyzes the contract terms vs. local risk data (Weather/Soil).

Output: The 3D farm changes visually (healthy crops vs. withered crops) to show profit or loss.

3. Tech Stack
Frontend (Visuals): Unity Engine (C#)

Backend (Brain): Python (Flask)

AI Model: Google Gemini 1.5 Pro (via Google AI Studio)

Communication: JSON over HTTP (REST API)

4. Project Architecture (How it connects)
Unity: Collects Crop, Acres, Price, Soil_Type.

Unity: Sends data as JSON to http://127.0.0.1:5000/analyze.

Python: Receives data + Prompts Gemini: "Calculate risk for [Crop] in [Nashik] at [Price]..."

Gemini: Returns Risk_Level (High/Low) and Estimated_Profit.

Unity: Visualizes the result (Green Particles = Profit, Dead Crops = Loss).

5. Development Roadmap (Checklist)
Phase 1: The Foundation (Days 1-3)
[ ] Repo Setup: Create Unity-Frontend and Python-Backend folders.

[ ] Unity: Create a 10x10 Grid System (Teammate).

[ ] Python: Create a basic app.py Flask server that returns "Hello World".

[ ] Connection Test: Send a dummy JSON from Unity to Python and print it.

Phase 2: The Logic (Days 4-10)
[ ] Python: Integrate google-generativeai library.

[ ] Python: Write the prompt engineering for Contract Analysis.

[ ] Unity: Build the UI (Input fields for Price, Acres).

[ ] Unity: Add Visuals (Cube changes color: Green=Healthy, Brown=Dead).

Phase 3: The Polish (Days 11-14)
[ ] Integration: Connect real Gemini output to Unity visuals.

[ ] Data: Add specific "Nashik" contexts (Onion, Tomato data).

[ ] Pitch: Record the demo video.

6. How to Run Locally
Backend (Python)
Bash

cd Python-Backend
pip install flask google-generativeai pandas
export GEMINI_API_KEY="your_key_here"
python main.py
# Server runs on http://127.0.0.1:5000
Frontend (Unity)
Open Unity-Frontend folder in Unity Hub (2022 LTS+).

Open Scene: Scenes/MainFarm.

Press Play.

7. Developer Rules (Read this!)
Git Ignore: NEVER push the Library or Temp folders from Unity.

API Keys: NEVER push your Google API Key to GitHub. Use environment variables.

Commits: Write clear messages (e.g., "Added Grid Script", not "update").
