from app.lib.data_streamer import DataStreamer

from litestar import Litestar, MediaType, get, post
from litestar.config.compression import CompressionConfig
from litestar.datastructures import State
from litestar.static_files.config import StaticFilesConfig
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.response_containers import Template, Stream
from litestar.template.config import TemplateConfig

from pathlib import Path

@get("/event", media_type=MediaType.HTML, cache=False)
async def get_event() -> Template:
  return Template(
    name="event.html.jinja2",
    context={"title": "Test Page"},
  )
  
@post("/event", media_type=MediaType.JSON)
async def post_event(state: State, data: dict[str, str]) -> Stream:
  data_streamer = DataStreamer()
  return Stream(iterator=data_streamer)

app = Litestar(
  route_handlers=[get_event, post_event],
  compression_config=CompressionConfig(backend="gzip", gzip_compress_level=9),
  template_config=TemplateConfig(
    directory=Path("templates"),
    engine=JinjaTemplateEngine,
  ),
  static_files_config=[
    StaticFilesConfig(directories=[Path("static")], path="/static", name="static")
  ],
)