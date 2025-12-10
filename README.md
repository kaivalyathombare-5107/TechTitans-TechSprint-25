# TechTitans-TechSprint-25
A 3D Digital Twin Simulator for Contract Farming using Unity & Google Gemini. Built for Tech Sprint AI Hack '25.

AgriTwin: AI Contract Guardian for Farmers 🛡️
Tech Sprint AI Hack '25 Submission

Tagline: "Visualizing the fine print. See the risk before you sign."

1. The Problem
Legal Complexity: Indian farmers cannot read complex English contracts or identify hidden "predatory clauses" (e.g., no payment during hail/pest attacks).

Lack of Context: A text warning isn't enough. Farmers need to see the potential consequences of a bad contract to understand the gravity of the risk.

2. The Solution
AgriTwin is an AI-powered software dashboard that combines Legal Analysis with 3D Visualization.

The Brain (Gemini AI): The user uploads a contract photo or pastes text. The AI scans for unfair terms, missing clauses, and hidden risks.

The Eyes (Unity 3D): Instead of just showing text, the software uses a 3D engine to visualize the consequence.

Example: If the contract has no "Drought Protection" clause, the 3D farm on the dashboard visually dries up and withers.

3. Tech Stack & Roles
Frontend (Unity): Handles the Chat Interface (UI) and Risk Visualization (3D Particle Systems).

Backend (Python/Flask): Handles the API connection and logic.

AI Model: Google Gemini 1.5 Pro (via Google AI Studio) for legal text analysis.

4. How It Works (The Flow)
Input: User uploads a contract PDF or asks a question in the Unity Chat UI.

Processing: Python sends the text to Google Gemini with a specific prompt: "Find faults in this contract regarding payment security and weather risk."

Tagging: Gemini returns a text summary and a Visual Tag (e.g., TAG_DROUGHT, TAG_PEST, TAG_SAFE).

Visualization: Unity receives the tag and triggers the corresponding 3D animation (e.g., The "Pest" tag triggers a particle system of bugs eating the crop).

5. Development Roadmap
Phase 1: The Interface (Days 1-4)
[ ] Unity UI: Build a split-screen layout (Left: Chat Window, Right: 3D Viewport).

[ ] Unity 3D: Create 3 distinct "State Prefabs":

Healthy Farm (Standard state).

Dead Farm (For drought/risk warnings).

Pest Infested (For lack of pesticide support).

[ ] Python: Setup basic Flask server.

Phase 2: The Intelligence (Days 5-10)
[ ] Python: Connect to Google Gemini API.

[ ] Prompt Engineering: Create the "Legal Expert" persona that outputs strictly formatted JSON (Text + Visual Tag).

[ ] Integration: Connect Unity Chat input to Python backend.

Phase 3: The Demo (Days 11-15)
[ ] Test Case: Feed a specific "Bad Contract" and ensure the 3D farm reacts correctly.

[ ] Polish: Add "Warning" UI popups in Unity.

6. How to Run Locally
Backend (Python)
Bash

cd Python-Backend
pip install flask google-generativeai
# Set your GEMINI_API_KEY environment variable
python app.py
Frontend (Unity)
Open Unity-Frontend folder in Unity Hub.

Open Scene: Scenes/DashboardMain.

Press Play to see the Chat UI and 3D Viewport.

7. Key Features (For Judges)
Visual Legal Aid: Bridges the literacy gap by showing risks visually.

Real-time Analysis: Uses Gemini 1.5 Pro for instant feedback.

Interactive 3D: Uses Unity's Particle Systems to simulate weather and crop outcomes based on contract data.
