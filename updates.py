from discord_webhook import DiscordWebhook
import os
web_url = os.environ['durl']

class logging:
  def send(md, content):
    DiscordWebhook(url=web_url, content=f"```{md}\n{content}\n```").execute()