// server.js
const express = require('express');
const dotenv = require('dotenv');
const axios = require('axios');
const path = require('path');

// Load environment variables
dotenv.config();
console.log("API Key:", process.env.GEMINI_API_KEY);

const app = express();
const port = process.env.PORT || 3000;

// Serve static files (CSS, HTML, etc.)
app.use(express.static(path.join(__dirname, 'public')));

// Parse incoming form data
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// Route for the homepage
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Route for handling chat requests
app.post('/chat', async (req, res) => {
    const userMessage = req.body.message;

    try {
        // Call the Gemini GenAI API
        const response = await axios.post('https://api.gemini.ai/chat', {
            message: userMessage,
            context: "mental health"
        }, {
            headers: {
                'Authorization': `Bearer ${process.env.GEMINI_API_KEY}`,
                'Content-Type': 'application/json'
            }
        });

        // Send the AI's response back to the client
        res.json({ response: response.data.response });

    } catch (error) {
        console.error('Error with Gemini API:', error.message);
        res.status(500).json({ response: "Sorry, I couldn't process your request at the moment." });
    }
});

// Start the server
app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});
