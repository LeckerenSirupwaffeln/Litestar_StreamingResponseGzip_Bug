from litestar.serialization import encode_json

from asyncio import sleep
import logging
from itertools import cycle


global_small_dict = {}
for i in range(500):
  global_small_dict[str(i)] = i
  
global_large_dict = {}
for i in range(1000000):
  global_large_dict[str(i)] = i

global_data_cycle = cycle((global_small_dict, global_large_dict))

class DataStreamer:
  def __aiter__(self) -> "DataStreamer":
    return self
  
  async def __anext__(self) -> bytes:
    await sleep(1)
    return encode_json(next(global_data_cycle))