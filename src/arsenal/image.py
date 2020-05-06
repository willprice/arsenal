import base64
import io
from typing import Optional

import numpy as np
from arsenal.collections import intersperse
from PIL import Image

_default_sep_color = (100, 100, 100)  # RGB (0-255)


def resize_image(
    image: np.ndarray,
    *,
    height: Optional[int] = None,
    width: Optional[int] = None,
    resample=Image.NEAREST,
) -> np.ndarray:
    if height is None and width is None:
        raise ValueError("At least one of width and height should be provided")
    img_height, img_width = image.shape[:-1]
    if height is None:
        height = int(width * img_height / img_width)
    if width is None:
        width = int(height * img_width / img_height)

    # image shape (H, W, 3)
    return np.array(Image.fromarray(image).resize((width, height), resample=resample))


def vstack_with_sep(rows, sep_width=3, sep_color=_default_sep_color, **kwargs):
    assert len(rows) > 0
    sep = np.ones((sep_width, rows[0].shape[1], 3), dtype=np.uint8)
    sep[:, :] *= np.array(sep_color, dtype=np.uint8)
    return np.vstack(intersperse(rows, sep, **kwargs))


def hstack_with_sep(cols, sep_width=3, sep_color=_default_sep_color, **kwargs):
    assert len(cols) > 0
    sep = np.ones((cols[0].shape[0], sep_width, 3), dtype=np.uint8)
    sep[:, :] *= np.array(sep_color, dtype=np.uint8)
    return np.hstack(intersperse(cols, sep, **kwargs))


def encode_to_base64_str(img: Image.Image) -> str:
    img = Image.fromarray(img)
    with io.BytesIO() as f:
        img.save(f, format="jpeg")
        return base64.b64encode(f.getvalue()).decode("ascii")


def decode_base64_img(b64_img: str) -> Image.Image:
    return Image.open(io.BytesIO(base64.b64decode(b64_img)))
