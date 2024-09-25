# chatapp/views.py
from django.shortcuts import render
from django.http import JsonResponse
import requests
from django.views.decorators.http import require_GET
from . import config  # Assuming you store API_KEY in config.py or Django settings

conversation_history = []

def index(request):
    return render(request, 'index.html')

@require_GET
def get_bot_response(request):
    userText = request.GET.get('msg')

    conversation_history.append({"role": "user", "content": userText})
    
    url = "https://api.deepbricks.ai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {config.API_KEY}"
    }
    data = {
        "model": "gpt-4-turbo",
        "messages": conversation_history
    }

    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()

    # Append AI response to conversation history
    ai_response = response_json['choices'][0]['message']['content']
    conversation_history.append({"role": "assistant", "content": ai_response})

    return JsonResponse({"response": ai_response})
