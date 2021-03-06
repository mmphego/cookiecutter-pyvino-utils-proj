#!/usr/bin/env python3

import argparse

from pyvino_utils import InputFeeder
from pyvino_utils.models.detection import face_detection


def arg_parser():
    parser = argparse.ArgumentParser(
        description="A simple OpenVINO based Face Detection running on CPU."
    )
    parser.add_argument("-i", "--input", help="Video or image input.", required=True)
    parser.add_argument(
        "-m", "--model", help="Model name (no extension).", required=True
    )
    parser.add_argument(
        "-b", "--show-bbox", action="store_true", help="Show bounding box."
    )
    # FIXME: Add more args
    return parser.parse_args()


def main(args):
    input_feed = InputFeeder(input_feed=args.input)
    face_detector = face_detection.FaceDetection(
        model_name=args.model, input_feed=input_feed
    )

    for frame in input_feed.next_frame(progress=False):
        inference_results = face_detector.predict(frame, show_bbox=args.show_bbox)

        # FIXME: Add code here

        if args.show_bbox:
            input_feed.show(frame)
    input_feed.close()


if __name__ == "__main__":
    args = arg_parser()
    main(args)
