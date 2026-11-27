# Audio

Local speech, voice and music: engines that run audio models, and the best free models to run in them.

### VoiceStudio
Link: https://github.com/debpalash/VoiceStudio
Stars: ★ 118.9k
What it does: Fully local voice cloning, voice design and video dubbing. AGPL.
Use it when: Your video needs a voiceover or dub and you do not want to send audio to a cloud API. Clone only voices you have consent for.
Works with: macOS, Linux, Windows
Install: `brew install --cask debpalash/tap/voicestudio`

### Voicebox
Link: https://github.com/jamiepine/voicebox
Stars: ★ 61.4k
What it does: Open-source AI voice studio: clone, dictate and create voiceovers locally.
Use it when: You want a desktop app for voiceovers. Clone only voices you have consent for.
Works with: macOS, Windows
Install: Download from voicebox.sh

### whisper.cpp
Link: https://github.com/ggml-org/whisper.cpp
Stars: ★ 55.6k
What it does: Local speech-to-text: OpenAI's Whisper models in C/C++, fast on CPU and Apple silicon, no Python.
Use it when: You need transcripts or subtitles from recordings without sending audio to a cloud API. Pair it with Whisper small below.
Works with: macOS, Linux, Windows; CPU, Metal, CUDA, Vulkan
Install: `brew install whisper-cpp`, then `whisper-cli -m ggml-small.bin -f audio.wav` (16 kHz WAV: `ffmpeg -i in.mp3 -ar 16000 -ac 1 -c:a pcm_s16le audio.wav`)

### Piper
Link: https://github.com/OHF-Voice/piper1-gpl
Stars: ★ 6.4k
What it does: Fast local neural text-to-speech that runs on a CPU, with voices in many languages. Maintained by the Open Home Foundation; GPL-3.0.
Use it when: You need quick, light offline speech, for example in a Home Assistant voice pipeline. Each voice has its own licence.
Works with: Linux, macOS, Windows; Python
Install: `pip install piper-tts`, `python3 -m piper.download_voices en_US-lessac-medium`, then `python3 -m piper -m en_US-lessac-medium -f out.wav -- 'Hello'`

### audio.cpp
Link: https://github.com/0xShug0/audio.cpp
Stars: ★ 4.5k
What it does: All-in-one C++ engine for local audio models: text-to-speech, voice cloning, speech recognition, music generation, voice conversion and separation, across 150+ model families, with a CLI, a server API and a web UI.
Use it when: You want one local tool for many audio models instead of a Python environment per model. Each model keeps its own licence; check its licence list before commercial use.
Works with: macOS, Linux, Windows; CPU, CUDA, Metal, Vulkan, HIP, SYCL; browser via WebGPU
Install: `brew tap 0xShug0/audio-cpp`, `brew trust 0xShug0/audio-cpp`, then `brew install audio-cpp`; or prebuilt binaries from its releases

### Best free voice models

Text-to-speech models with open weights and a licence that allows commercial use. Ranks are from the [Artificial Analysis speech arena](https://artificialanalysis.ai/text-to-speech/leaderboard), read on 2026-11-25; check the live board before you commit. Fish Audio Drama 3 (#9) and Breeze TTS 2 (#15) rank higher but are research or non-commercial only, so they are left out. audio.cpp and VoiceStudio, above, run models like these locally.

### Ming-3.0-tts
Link: https://huggingface.co/inclusionAI/Ming-3.0-tts-0.5B
Maker: Ant Group
Rank: #27 (Elo 1180); best free model
Licence: MIT
Use it when: You want the best free voice quality, in English, Chinese, Japanese, Korean or major European languages.
Run: `git clone https://github.com/inclusionAI/Ming-3.0-tts.git`, `pip install -r requirements.txt`, then `python infer.py`

### Phonon 31M
Link: https://huggingface.co/gradium/phonon-31m-en
Maker: Gradium
Rank: #46 (1109)
Licence: Apache-2.0
Use it when: You need English speech from a tiny model on modest hardware.
Run: `pip install git+https://github.com/huggingface/transformers`, then load with `transformers` as its model card shows

### Kokoro 82M
Link: https://huggingface.co/hexgrad/Kokoro-82M
Maker: hexgrad
Rank: #68 (1061)
Licence: Apache-2.0
Use it when: You want a small, fast, widely supported voice model for narration.
Run: `pip install kokoro soundfile`, then `from kokoro import KPipeline`

### Maya1
Link: https://huggingface.co/maya-research/maya1
Maker: Maya Research
Rank: #74 (1049)
Licence: Apache-2.0
Use it when: You want to describe a voice in words and add emotions like laughter or whispering.
Run: `pip install torch transformers accelerate snac soundfile`, then load with `transformers` as its model card shows

### Chatterbox
Link: https://huggingface.co/ResembleAI/chatterbox
Maker: Resemble AI
Rank: #87 (1021)
Licence: MIT
Use it when: You need to clone a voice from a short sample, in many languages. Clone only voices you have consent for.
Run: `pip install chatterbox-tts`, then `from chatterbox.tts import ChatterboxTTS`

### VibeVoice 1.5B
Link: https://huggingface.co/microsoft/VibeVoice-1.5B
Maker: Microsoft
Rank: #91 (955)
Licence: MIT
Use it when: You generate long, multi-speaker audio such as a podcast or dialogue.
Run: Clone [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) and follow its install steps

### Tacotron 2
Link: https://huggingface.co/speechbrain/tts-tacotron2-ljspeech
Maker: Google (SpeechBrain checkpoint)
Rank: Not ranked; 2017 research model
Licence: Apache-2.0
Use it when: You want a small, classic English single-voice model to learn from or fine-tune on your own voice data.
Run: `pip install speechbrain torchaudio`, then the Python snippet on its model card; it pairs with the [HiFi-GAN vocoder](https://huggingface.co/speechbrain/tts-hifigan-ljspeech)

### FastSpeech 2
Link: https://huggingface.co/speechbrain/tts-fastspeech2-ljspeech
Maker: Microsoft (SpeechBrain checkpoint)
Rank: Not ranked; 2020 research model
Licence: Apache-2.0
Use it when: Like Tacotron 2 but faster, with speed, pitch and energy you can set per call.
Run: `pip install speechbrain torchaudio`, then the Python snippet on its model card; it pairs with the [HiFi-GAN vocoder](https://huggingface.co/speechbrain/tts-hifigan-ljspeech)

### Free speech-to-text models

Open-weights transcription models you can run locally; whisper.cpp, above, runs them.

### Whisper small
Link: https://huggingface.co/openai/whisper-small
Maker: OpenAI
Rank: Not ranked
Licence: Apache-2.0
Use it when: You want accurate multilingual transcription from a 244M-parameter model that runs on a laptop. Use `small.en` for English only.
Run: In whisper.cpp: `curl -LO https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-small.bin`; in Python: `pip install openai-whisper`, then `whisper audio.mp3 --model small`
