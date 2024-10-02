"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyC00CZaNxRReClgnrJuex_j1ixWLe4S5SU")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)
history =[]
print("Hello,I'm GentleAI.How can i help you?")
while True:
    input_user= input("You:")
    chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "Mental Health Advice and care for students",
      ],
    },
    {
      "role": "model",
      "parts": [
        "## Mental Health Advice and Care for Students: A Comprehensive Guide\n\nThe pressures of being a student can be immense. From academic workloads to social expectations and financial concerns, it's no wonder that mental health is a growing concern among students. This guide aims to provide comprehensive information and resources to support student mental well-being:\n\n**1. Recognize the Signs:**\n\n* **Emotional:** Feeling overwhelmed, anxious, depressed, irritable, withdrawn, or hopeless.\n* **Behavioral:** Changes in sleep patterns, appetite, energy levels, social interactions, or academic performance.\n* **Physical:** Headaches, stomach aches, fatigue, or difficulty concentrating.\n\n**2. Seek Help and Support:**\n\n* **University Counseling Services:** Most universities have dedicated counseling centers with trained professionals who can provide individual therapy, group therapy, workshops, and crisis intervention.\n* **Student Support Services:** Many universities offer resources such as academic advisors, tutoring centers, and disability services, which can help manage stress and improve academic performance.\n* **Peer Support Groups:** Connect with other students who are going through similar experiences. Many universities offer peer support groups focused on specific issues, such as anxiety, depression, or stress management.\n* **Faculty and Staff:** Develop strong relationships with your professors and advisors. They may be able to provide academic support and refer you to other resources.\n* **Friends and Family:** Lean on your support network for emotional support and encouragement.\n\n**3. Take Care of Yourself:**\n\n* **Self-Care:** Prioritize sleep, a healthy diet, regular exercise, and engaging in activities you enjoy. These can significantly boost your mood and energy levels.\n* **Time Management:** Develop effective time management strategies to manage your workload and reduce stress.\n* **Stress Management Techniques:** Practice mindfulness, deep breathing exercises, yoga, or meditation to manage stress and promote relaxation.\n* **Healthy Communication:** Learn effective communication skills to express your needs and concerns to others.\n* **Limit Social Media:** Excessive social media use can contribute to anxiety and depression. Set boundaries and take breaks from social media when needed.\n\n**4. Understand Mental Health Conditions:**\n\n* **Anxiety Disorders:** Characterized by excessive worry, fear, and nervousness.\n* **Depression:** Characterized by persistent feelings of sadness, hopelessness, and loss of interest in activities.\n* **Eating Disorders:** Characterized by unhealthy eating habits and body image issues.\n* **Substance Abuse:** Characterized by the misuse of alcohol or drugs.\n* **Sleep Disorders:** Characterized by difficulty falling asleep, staying asleep, or experiencing restful sleep.\n\n**5. Be Aware of Crisis Resources:**\n\n* **National Suicide Prevention Lifeline:** 988\n* **Crisis Text Line:** Text HOME to 741741\n* **The Trevor Project:** 1-866-488-7386\n\n**Remember:** Seeking help is a sign of strength, not weakness. There are many resources available to support your mental well-being. Take care of yourself and reach out for help when you need it.\n\nThis is just a starting point. There are many other resources and information available online and through your university. Be proactive about your mental health and prioritize self-care. You deserve to be happy and healthy!",
      ],
    },
  ]
)

response = chat_session.send_message(input_user)
model_response= response.text
print(response.text)
print()
history.append=({'role':'user',"parts":[input_user]})
history.append=({'role':'user',"parts":[model_response]})