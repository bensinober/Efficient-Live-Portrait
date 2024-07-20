import argparse
import warnings
from omegaconf import OmegaConf
from LivePortrait import EfficientLivePortrait
from LivePortrait.commons import save_config_to_yaml

warnings.filterwarnings("ignore")


def main(video_path, source_img, use_tensorrt, real_time, half):
    cfg_yaml = save_config_to_yaml()
    kwargs = OmegaConf.load(cfg_yaml)
    live_portrait = EfficientLivePortrait(use_tensorrt, half, **kwargs)
    live_portrait.render(live_portrait, video_path_or_id=video_path, image_path=source_img, real_time=real_time)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Live Portrait Rendering Script')
    parser.add_argument('-v', '--video', type=str, required=True,
                        help='Path to the driving video or your webcam id')
    parser.add_argument('-i', '--image', type=str, required=True, help='Path to the source image')
    parser.add_argument('-e', '--run_time', action='store_true', help='Turn on TensorRT mode')
    parser.add_argument('-fp16', '--half_precision', action='store_true', help='Half Precision on TensorRT mode')
    parser.add_argument('-r', '--real_time', action='store_true', help='Enable real-time webcam demo')
    args = parser.parse_args()

    main(args.video, args.image, args.run_time, args.half_precision, args.real_time)
