from audio2string.whisper_audio2string import whisper_audio2string

# インスタンス作成
transcriber = whisper_audio2string()

# 文字起こし
text = transcriber.audio2string()
print(text)