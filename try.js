const axios = require('axios');
require('dotenv').config();

(async () => {
    try {
        const response = await axios.post(
            'https://api.gemini.ai/chat',
            {
                "input": "Hello!",
                "context": "mental health"
            },
            {
                headers: {
                    'Authorization': `Bearer ${process.env.GEMINI_API_KEY}`,
                    'Content-Type': 'application/json'
                }
            }
        );

        console.log("API Response:", response.data);
    } catch (error) {
        console.error('Error details:', error.response ? error.response.data : error.message);
    }
})();
