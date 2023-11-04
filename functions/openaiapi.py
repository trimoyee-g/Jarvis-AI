# import os
import openai
from config import apikey
openai.api_key = apikey

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write an email",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)
'''
{
"choices": [
    {
      "text": "\n\nSubject: Important Meeting on Wednesday\n\nDear Team,\n\nWe have an important meeting scheduled for Wednesday at 10 am. The purpose of this meeting is to review our progress on the project so far and to discuss our plans going forward.\n\nPlease make sure you come to the meeting prepared with an update on your progress and any other relevant information. Be sure to also bring any questions or concerns that you may have. \n\nIf you cannot attend the meeting, please let me know as soon as possible.\n\nThanks,\n[Your Name]",
      "index": 0,
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 3,
    "completion_tokens": 115,
    "total_tokens": 118
  }
}
'''