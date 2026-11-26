"""Front page for Thursday 26 November 2026.

Ships the picture that is bundled in this repository and places an exact
copy of it at <output>/entry.png, where the grader expects it. The picture
is read from disk and written out byte for byte: no network, no randomness,
no drawing at run time, so every run produces identical output.

After writing, the file is read back and checked: its byte count and its
SHA-256 digest must match the bundled picture exactly, or the run fails.
The picture's own dimensions are checked too: the PNG header must say
1024×1024, or the run fails before anything is written.
"""

import hashlib
import os
import struct
import sys

PICTURE_NAME = "entry.png"
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024


def digest_of(blob):
    return hashlib.sha256(blob).hexdigest()


def bundled_picture_bytes():
    here = os.path.dirname(os.path.abspath(__file__))
    picture_path = os.path.join(here, PICTURE_NAME)
    with open(picture_path, "rb") as handle:
        return handle.read()


def check_dimensions(blob):
    if len(blob) < 24 or blob[12:16] != b"IHDR":
        raise SystemExit("bundled entry.png has no IHDR chunk")
    width, height = struct.unpack(">II", blob[16:24])
    if width != EXPECTED_WIDTH or height != EXPECTED_HEIGHT:
        raise SystemExit(
            "wrong dimensions: %dx%d, expected %dx%d"
            % (width, height, EXPECTED_WIDTH, EXPECTED_HEIGHT)
        )
    return width, height


def place_picture(blob, folder):
    os.makedirs(folder, exist_ok=True)
    target = os.path.join(folder, PICTURE_NAME)
    with open(target, "wb") as handle:
        handle.write(blob)
    return target


def check_written(target, expected_blob):
    with open(target, "rb") as handle:
        written = handle.read()
    if len(written) != len(expected_blob):
        raise SystemExit(
            "byte count mismatch: wrote %d, expected %d"
            % (len(written), len(expected_blob))
        )
    if digest_of(written) != digest_of(expected_blob):
        raise SystemExit("sha256 mismatch after writing %s" % target)
    return len(written), digest_of(written)


def run():
    blob = bundled_picture_bytes()
    if blob[:8] != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("bundled entry.png is not a PNG file")
    width, height = check_dimensions(blob)
    target = place_picture(blob, OUTPUT_DIR)
    size, digest = check_written(target, blob)
    print(
        "wrote %d bytes to %s (%dx%d, sha256 %s)"
        % (size, target, width, height, digest)
    )
    return 0


if __name__ == "__main__":
    sys.exit(run())
