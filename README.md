# Efficient-Live-Portrait
## 📹 SDXL-Lightning + Controlnet-Open-Pose + Live-Portrait


https://github.com/user-attachments/assets/5ca959f9-8fcc-4233-8a1d-9b201bd042c9



https://github.com/user-attachments/assets/24086eea-7075-45ec-8eef-2a9344185746


## 📹 Video2Video Demo


https://github.com/user-attachments/assets/de259719-d174-4c83-9287-2fa77c3b8fad


## 📹 Video Demo for normal mode
 

https://github.com/user-attachments/assets/ac0e92d7-34e1-4402-a202-d06a2e806abe

## 📹 Video Demo for Face-ID mode
+ Single Face Image
  ![368220873_826368889022136_4472311944594836999_n](https://github.com/user-attachments/assets/25851766-a454-4f16-8d44-f63923cdabf2)

+ Through Face-ID adapter
   

https://github.com/user-attachments/assets/197a8d75-3c56-43f5-ac71-e7110d9e53d1


## Introduction
This repo is the optimize task by converted to ONNX and TensorRT models for [LivePortrait: Efficient Portrait Animation with Stitching and Retargeting Control](https://github.com/KwaiVGI/LivePortrait).
We are actively updating and improving this repository. If you find any bugs or have suggestions, welcome to raise issues or submit pull requests (PR) 💖.

Also we adding feature: 
+ Real-Time demo with ONNX models
+ TensorRT runtime with latest Tensorrt version. You should run on Colab, this still can't use on Window
+ Face-ID adapter for control Face animation in the Multiple Faces image you want to do
+ Coming soon for ControlNet Stable Diffusion. Stay tuned
## Features
[✅] 20/07/2024: TensorRT Engine code and Demo

[✅] 22/07/2024: Support Multiple Faces

[✅] 22/07/2024: Face-ID Adapter for Control Face Animation

[✅] 24/07/2024: Multiple Face motion in Video for animation multiples Face in image

[✅] 28/07/2024: Supported Video2Video Live Portrait (only use one Face)

[✅] 30/07/2024: Support SDXL-Lightning Controlnet-Open-Pose from 1 to 8 step for change source image to Art Image

[  ] Integrate Animate-Diff Lightning Motion module


## 🔥 Getting Started
### 1. Clone the code and prepare the environment
```bash
git clone https://github.com/aihacker111/Efficient-Live-Portrait
# create env using conda
conda create -n ELivePortrait python==3.10.14
conda activate ELivePortrait
# install dependencies with CPU
pip install -r requirements-cpu.txt
# install dependencies with GPU
pip install -r requirements-gpu.txt
# install dependencies with pip for mps
pip install -r requirements-mps.txt 
```

**Note:** make sure your system has [FFmpeg](https://ffmpeg.org/) installed!

### 2. Download pretrained weights

The pretrained weights is also automatic downloading
You don't need to download and put model into sources code
```text
pretrained_weights
|
├── landmarks
│   └── models
│       └── buffalo_l
│       |   ├── 2d106det.onnx
│       |    └── det_10g.onnx
|       └── landmark.onnx
└── live_portrait
      |
      ├── appearance_feature_extractor.onnx
      ├── motion_extractor.onnx
      ├── generator_warping.onnx
      ├── stitching_retargeting.onnx
      └── stitching_retargeting_eye.onnx
      └── stitching_retargeting_lip.onnx
      ├── appearance_feature_extractor_fp32.engine
      ├── motion_extractor_fp32.engine
      ├── generator_fp32.engine
      ├── stitching_fp32.engine
      └── stitching_eye_fp32.engine
      └── stitching_lip_fp32.engine
      ├── appearance_feature_extractor_fp16.engine
      ├── motion_extractor_fp16.engine
      ├── generator_fp16.engine
      ├── stitching_fp16.engine
      └── stitching_eye_fp16.engine
      └── stitching_lip_fp16.engine
      

```
### 3. Inference and Real-time Demo 🚀
#### Fast hands-on

+ TensorRT FP32 is seem slower than FP16 but result better than fp16, so be careful to use both of it, I'm not recommend using ONNX model because it's not still update and fix grid sample or speed
+ Also If you want to Quality Result. Please remove FP16, the speed can be slower than fp16 but result is better
For run Face-ID mode:
```bash
python run_live_portrait.py --driving_video 'path/to/your/video/driving/or/webcam/id' --source_image 'path/to/your/image/want/to/animation' -condition_image 'path/the/single/face/image/to/compute/face-id' --task ['image', 'video', 'webcam'] --run_time --half_precision --use_face_id 
```
For run Multiple Face Motion mode:
```bash
python run_live_portrait.py --driving_video 'path/to/your/video/driving/or/webcam/id' --source_image 'path/to/your/image/want/to/animation'  --task ['image', 'video', 'webcam'] --run_time --half_precision
```
For Vid2Vid Live Portrait:
```bash
python run_live_portrait.py --driving_video 'path/to/your/video/driving/or/webcam/id' --source_video 'path/to/your/video/want/to/animation'  --task ['image', 'video', 'webcam'] --run_time --half_precision
```
For SDXL-Lightning + OpenPose-Lora + Live Portrait
```bash
python /content/Efficient-Live-Portrait/run_live_portrait.py --driving_video 'path/to/your/video' --source_image 'path/to/your/image/want/to/animation'  --run_time --task image --use_diffusion --lcm_steps [1, 2, 4, 8] --prompt '1girl, offshoulder, light smile, shiny skin best quality, masterpiece, photorealistic'
```
#### Colab Demo
 Follow in the colab folder
### 5. Inference speed evaluation 🚀🚀🚀

We'll release it soon
