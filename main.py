import argparse
import logging
from moviepy.editor import VideoFileClip
import moviepy.video.fx.all as vfx

logging.basicConfig(format='%(filename)s: %(message)s',
                    level=logging.DEBUG)


def speed_up_video(file_path, speed_up):
    # divide the path into the path to the file and the file name
    name_of_file = file_path.split("\\")[-1]
    path_of_file = file_path.replace(name_of_file, "")

    logging.debug(f"Path of file: {path_of_file}")
    logging.debug(f"Name of file: {name_of_file}")

    # handle video file
    video = VideoFileClip(file_path)

    # changing the speed of file
    final = video.fx(vfx.speedx, speed_up)

    # saving video clip in the same directory
    final.write_videofile(f"{path_of_file}\\result_{name_of_file}")


if __name__ == "__main__":
    # setting up arguments
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-i",
        "--input_file_path",
        help="the path to the file to speed up",
        required=True,
    )
    # the speed of the desired file relative to the original one (speed ratio)
    parser.add_argument(
        "-s",
        "--speed_up",
        help="video file acceleration ratio",
        required=True,
    )

    # getting arguments from argparse:
    # - the path to the file you are looking for,
    # - the path where you want to save the file

    args = parser.parse_args()
    try:
        path_to_source = args.input_file_path
    except OSError:
        logging.error(msg="Please specify the path to the file!")
        raise

    speed = int(args.speed_up)

    speed_up_video(path_to_source, speed)

