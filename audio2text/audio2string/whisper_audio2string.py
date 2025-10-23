import mlx_whisper

class whisper_audio2string:
  def audio2string(self):
    # 音声ファイルを指定して文字起こし
    audio_file_path = "./audio2text/audio2string/test/audio-output.wav"

    result = mlx_whisper.transcribe(
      audio_file_path, path_or_hf_repo="./audio2text/audio2string/whisper-base-mlx"
    )

    # 文字起こしテキストのみを抽出
    text_only = result['text']
    # print(text_only)

    return text_only
