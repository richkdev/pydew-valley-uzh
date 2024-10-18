import zengl

from src.settings import SCREEN_SIZE
from src.support import resource_path

ctx = zengl.context()

screen_texture = ctx.image(size=SCREEN_SIZE, format="rgba8unorm")

pipeline = ctx.pipeline(
    vertex_shader=open(resource_path("src/shaders/template.vert.glsl")).read(),
    fragment_shader=open(resource_path("src/shaders/blue_tint.frag.glsl")).read(),
    layout=[
        {
            "name": "screen_texture",
            "binding": 0,
        },
    ],
    resources=[
        {
            "type": "sampler",
            "binding": 0,
            "image": screen_texture,
        },
    ],
    framebuffer=None,
    viewport=(0, 0, *SCREEN_SIZE),
    topology="triangles",
    vertex_count=3,
)
