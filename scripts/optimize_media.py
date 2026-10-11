#!/usr/bin/env python3
"""Prepare imported Lark photos and videos for fast, private web delivery."""
from __future__ import annotations

import argparse
import os
import subprocess
from pathlib import Path

from PIL import Image, ImageOps


def optimize_image(path: Path) -> None:
    print(f"Optimizing image: {path.name}", flush=True)
    with Image.open(path) as source:
        image = ImageOps.exif_transpose(source).convert("RGB")
        image.thumbnail((1600, 1600), Image.Resampling.LANCZOS)
        image.save(path, "JPEG", quality=80, optimize=True, progressive=True)


def optimize_video(path: Path) -> None:
    print(f"Optimizing video: {path.name}", flush=True)
    target = path.with_name(path.stem + ".optimized.mp4")
    subprocess.run(
        [
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(path),
            "-map_metadata", "-1", "-vf", "scale='min(1280,iw)':-2",
            "-c:v", "libx264", "-preset", "medium", "-crf", "28",
            "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", str(target),
        ],
        check=True,
    )
    os.replace(target, path.with_suffix(".mp4"))
    if path.suffix.lower() != ".mp4":
        path.unlink()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("folder", type=Path)
    args = parser.parse_args()
    for path in sorted(args.folder.iterdir()):
        if path.name.startswith("lark-image-"):
            optimize_image(path)
        elif path.name.startswith("lark-video-"):
            optimize_video(path)


if __name__ == "__main__":
    main()
