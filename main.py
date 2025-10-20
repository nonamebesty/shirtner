#from bot import Bot

import asyncio

# Check if an event loop is already set on the current thread
try:
    asyncio.get_event_loop()
except RuntimeError:
    # If no loop is set, create a new one and set it
    asyncio.set_event_loop(asyncio.new_event_loop())

# The rest of your imports can follow
from bot import Bot
# ...


if __name__ == '__main__':
    Bot().run()
