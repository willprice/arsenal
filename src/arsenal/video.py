from typing import Union

import numpy as np
from moviepy.video.io.html_tools import html_embed
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
from moviepy.video.VideoClip import VideoClip


def clip_to_html(
    clip: Union[VideoClip, np.ndarray], verbose=False, fps=24, **kwargs
) -> str:
    if isinstance(clip, (np.ndarray, list)):
        clip = ImageSequenceClip(list(clip), fps=fps)
    assert hasattr(clip, "write_videofile")
    if clip.fps is None:
        clip.fps = fps
    if not verbose:
        rd_kwargs = {"logger": None}
    else:
        rd_kwargs = dict()
    return html_embed(clip, rd_kwargs=rd_kwargs, **kwargs)
