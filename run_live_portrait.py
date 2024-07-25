from LivePortrait import EfficientLivePortrait
from LivePortrait.commons import save_config_to_yaml
import argparse
import warnings
from omegaconf import OmegaConf

warnings.filterwarnings("ignore")


def main(video_path, source_img, ref_img, max_faces, use_tensorrt, real_time, half_precision, use_face_id, cropping_video):
    cfg_yaml = save_config_to_yaml()
    kwargs = OmegaConf.load(cfg_yaml)
    live_portrait = EfficientLivePortrait(use_tensorrt, half_precision, cropping_video, **kwargs)

    if use_face_id:
        live_portrait.render(video_path_or_id=video_path, image_path=source_img, ref_img=ref_img, max_faces=max_faces, real_time=real_time)
    else:
        live_portrait.render(video_path_or_id=video_path, image_path=source_img, ref_img=None, max_faces=max_faces, real_time=real_time)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Live Portrait Rendering Script')
    parser.add_argument('-v', '--video', type=str, required=True,
                        help='Path to the driving video or your webcam id')
    parser.add_argument('-i', '--image', type=str, required=True, help='Path to the source image')
    parser.add_argument('-ref', '--ref_image', type=str, help='Path to the ref image')
    parser.add_argument('-num', '--max_faces', type=int, default=1, required=False, help='Enter number of faces you want to extract in Video Motion')
    parser.add_argument('-e', '--run_time', action='store_true', help='Turn on TensorRT mode')
    parser.add_argument('-fp16', '--half_precision', action='store_true', help='Half Precision on TensorRT mode')
    parser.add_argument('-r', '--real_time', action='store_true', help='Enable real-time webcam demo')
    parser.add_argument('--use_face_id', action='store_true', help='Use reference image for face ID')
    parser.add_argument('--cropping_video', action='store_true', required=False, help='Auto Cropping 1:1 Video')
    args = parser.parse_args()

    main(args.video, args.image, args.ref_image, args.max_faces, args.run_time, args.real_time, args.half_precision, args.use_face_id, args.cropping_video)
