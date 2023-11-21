import requests
import json

def emotion_detector(text_to_analyse):
    if not text_to_analyse.strip():
        return None

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers = header)
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        emotion_predictions= formatted_response["emotionPredictions"][0]["emotion"]
        dominant_emotion = max(emotion_predictions.items(), key=lambda x: x[1])[0]

        return {
            'anger': emotion_predictions['anger'],
            'disgust': emotion_predictions['disgust'],
            'fear': emotion_predictions['fear'],
            'joy': emotion_predictions['joy'],
            'sadness': emotion_predictions['sadness'],
            "The dominant emotion is": dominant_emotion
        }

    elif response.status_code == 400:
     
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            "dominant emotion": None
        }
    else:
        return None

  
        
