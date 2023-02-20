import os
from google.cloud import texttospeech
from django import template
register = template.Library()

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'mysite/templatetags/tts_secret.json'

@register.filter(name="synthesize_speech")
def synthesize_speech(text, lang='en-US', gender='defalut'):
    file_name = text.replace(' ', '_')
    is_file = os.path.isfile(f"/static/listening/{file_name}.mp3")
    if is_file:
        pass
    else:
        gender_type = {
            'defalut': texttospeech.SsmlVoiceGender.SSML_VOICE_GENDER_UNSPECIFIED,
            'male': texttospeech.SsmlVoiceGender.MALE,
            'female': texttospeech.SsmlVoiceGender.FEMALE,
            'neutral': texttospeech.SsmlVoiceGender.NEUTRAL
        }
        # lang_code = {
        #     'en-US': 'en-US',
        #     '日本語': 'ja-JP'
        # }

        client = texttospeech.TextToSpeechClient()

        synthesis_input = texttospeech.SynthesisInput(text=text)

        voice = texttospeech.VoiceSelectionParams(
            #language_code=lang_code[lang], ssml_gender=gender_type[gender]
            language_code=lang, ssml_gender=gender_type[gender]

        )

        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )

        response = client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )

        # The response's audio_content is binary.
        with open(f"static/listening/{file_name}.mp3", "wb") as out:
            # Write the response to the output file.
            out.write(response.audio_content)
            #print('Audio content written to file "output.mp3"')
        # [END tts_quickstart]
    return ("フレーズの詳細")