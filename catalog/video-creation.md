# Video creation

Most tools here have more than 30,000 stars. Smaller agent skills for video, such as OpenFilm and motionmaxxing, are under [Skills](#skills).

### ComfyUI
Link: https://github.com/Comfy-Org/ComfyUI
Stars: ★ 148.9k
What it does: Node-graph GUI and API for running diffusion models, including the open video models below.
Use it when: You want to run open-weights video models on your own GPU, or chain generation steps.
Works with: NVIDIA, AMD, Apple silicon
Install: Desktop app from comfy.org, or clone and `pip install -r requirements.txt`

### MoneyPrinterTurbo
Link: https://github.com/harry0703/MoneyPrinterTurbo
Stars: ★ 145.9k
What it does: Generates a finished short video (script, stock footage, voice, subtitles, music) from a topic.
Use it when: You need many short vertical videos fast and stock footage is acceptable.
Works with: Docker; OpenAI, DeepSeek, Ollama and others
Install: `git clone https://github.com/harry0703/MoneyPrinterTurbo.git`, then `docker compose -f docker-compose.release.yml up`

### OpenCut
Link: https://github.com/OpenCut-app/OpenCut
Stars: ★ 99.5k
What it does: Open-source CapCut alternative video editor.
Use it when: You want a free, simple editor for cutting and captioning clips.
Works with: Browser; self-hostable
Install: See its README

### Manim
Link: https://github.com/3b1b/manim
Stars: ★ 97k
What it does: 3Blue1Brown's engine for precise animated maths and diagrams.
Use it when: You explain an algorithm or concept and want exact, code-defined animation.
Works with: Python
Install: `pip install manimgl`

### HyperFrames
Link: https://github.com/heygen-com/hyperframes
Stars: ★ 91.3k
What it does: HeyGen's open-source video editor: your agent writes HTML compositions and renders them to MP4.
Use it when: You want Claude Code or Codex to make promos, explainers or captioned clips from a prompt, a URL or your footage.
Works with: Claude Code, Codex; Node
Install: `npx skills add heygen-com/hyperframes`, then `npx hyperframes init my-video`

### OpenMontage
Link: https://github.com/OpenMontageInc/OpenMontage
Stars: ★ 83.8k
What it does: Agentic video production system with production pipelines, tools and agent skills. AGPL.
Use it when: You want an agent to run a whole production: script, assets, edit, render.
Works with: Claude Code and other agents
Install: `git clone https://github.com/OpenMontageInc/OpenMontage.git`, then follow its README

### OBS Studio
Link: https://github.com/obsproject/obs-studio
Stars: ★ 80.2k
What it does: Screen recording and live streaming.
Use it when: You record product demos, tutorials or bug repros.
Works with: macOS, Windows, Linux
Install: `brew install --cask obs`

### Remotion
Link: https://github.com/remotion-dev/remotion
Stars: ★ 76.1k
What it does: Make videos programmatically with React components.
Use it when: You know React and want data-driven or templated videos rendered in code or CI. Companies above 3 people need a paid licence.
Works with: Node, React; agent skills at `remotion-dev/skills`
Install: `npx create-video@latest`

### anime.js
Link: https://github.com/juliangarnier/anime
Stars: ★ 75.1k
What it does: Lightweight JavaScript animation engine.
Use it when: You need motion graphics inside an HTML or web composition (HyperFrames supports it).
Works with: Browser, Node
Install: `npm install animejs`

### FFmpeg
Link: https://github.com/FFmpeg/FFmpeg
Stars: ★ 68.3k
What it does: The encoder, decoder and filter engine underneath almost every tool here.
Use it when: Your agent needs to cut, convert, resize, subtitle or stitch video from the command line.
Works with: Every OS
Install: `brew install ffmpeg`

### LosslessCut
Link: https://github.com/mifi/lossless-cut
Stars: ★ 46.5k
What it does: Trims and splits video without re-encoding, so it is instant and keeps full quality.
Use it when: You need to cut a long recording into clips quickly.
Works with: macOS, Windows, Linux
Install: `brew install --cask losslesscut`

### Pixelle-Video
Link: https://github.com/ATH-MaaS/Pixelle-Video
Stars: ★ 30.6k
What it does: Fully automated short-video engine with AI-generated visuals.
Use it when: You want topic-to-video like MoneyPrinterTurbo but with generated images and clips instead of stock footage.
Works with: Python, FFmpeg, ComfyUI
Install: `git clone https://github.com/ATH-MaaS/Pixelle-Video.git`, then `uv run streamlit run web/app.py`

### stable-diffusion.cpp
Link: https://github.com/leejet/stable-diffusion.cpp
Stars: ★ 8.1k
What it does: Image and video diffusion in plain C/C++ with no Python: SD, Flux, Wan, LTX-2.5 and MiniMax H3, with a CLI, a server and a web UI.
Use it when: You want to run the open video models below on a CPU, Apple silicon or a small GPU without ComfyUI or a Python stack.
Works with: macOS, Linux, Windows; CPU, CUDA, Metal, Vulkan, OpenCL, SYCL
Install: Prebuilt binaries from its releases, then `sd-cli -m <model> -p "a lovely cat"`

### Best free video generation models

Only open-weights models you can download and run without paying; closed and API-only models are left out. Ranks are from the [Artificial Analysis](https://artificialanalysis.ai/video/leaderboard/text-to-video) blind-vote boards, read on 2026-11-25. They move monthly, so check the live [text-to-video](https://artificialanalysis.ai/video/leaderboard/text-to-video) and [image-to-video](https://artificialanalysis.ai/video/leaderboard/image-to-video) boards. The **Run** column says how to start each one; ComfyUI and stable-diffusion.cpp run most of them.

### MiniMax H3
Link: https://huggingface.co/MiniMaxAI/MiniMax-H3
Maker: MiniMax
Rank: #3 text-to-video (Elo 1164), #6 image-to-video (1135); best free model
Licence: Free in the EU, UK, US and South Korea. Above $20M yearly revenue you need MiniMax's written permission; commercial products must show "MiniMax H3"
Use it when: You want the best quality you can run yourself.
Run: In ComfyUI (see the [Comfy tutorial](https://docs.comfy.org/tutorials/video/minimax/minimax-h3)), or with diffusers or vLLM

### Hyperflow H3
Link: https://huggingface.co/VideoRebirthAI/hyperflow
Maker: Video Rebirth
Rank: #4 text-to-video (1156), #10 image-to-video (1120)
Licence: Same licence as MiniMax H3
Use it when: You want a second H3-based model to compare.
Run: `pip install "hyperflow-h3[examples] @ git+https://github.com/Video-Rebirth/hyperflow.git"`, then the diffusers example on its model card

### Pika H3 Flex
Link: https://huggingface.co/Pika-Labs/Pika-H3-Flex
Maker: Pika
Rank: #16 text-to-video (1123), #13 image-to-video (1116)
Licence: Same licence as MiniMax H3
Use it when: You mostly animate still images.
Run: In ComfyUI (see the [Comfy tutorial](https://docs.comfy.org/tutorials/video/pika/pika-h3-flex)), or clone [Pika-H3-Flex](https://github.com/Pika-Labs/Pika-H3-Flex); one large GPU, tested on H100 80GB

### LTX-2.5
Link: https://huggingface.co/Lightricks/LTX-2.5
Maker: Lightricks
Rank: #32 text-to-video (938), #35 image-to-video (914)
Licence: Free for companies under $10M yearly revenue; paid licence above
Use it when: You want video and audio generated together in one pass.
Run: In ComfyUI with [ComfyUI-LTXVideo](https://github.com/Lightricks/ComfyUI-LTXVideo), or `git clone https://github.com/Lightricks/LTX-2.git` then `uv sync`

### Wan 2.2
Link: https://huggingface.co/Wan-AI/Wan2.2-T2V-A14B
Maker: Alibaba
Rank: Not on the boards
Licence: Apache-2.0: free for any use, no revenue cap, region or attribution rule
Use it when: You need a licence with no conditions at all.
Run: In ComfyUI, or `git clone https://github.com/Wan-Video/Wan2.2.git`, `pip install -r requirements.txt`, then `python generate.py --task t2v-A14B`
