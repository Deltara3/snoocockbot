# Please don't copy until the bot is suspended. Then I don't really care. (Reddit please no suspension)

import praw
import os
from keep_alive import keep_alive
from multiprocessing import Process

# file variable name = os.environ['variable name']
# Hopefully above makes sense. If not please suggest a change.

reddit = praw.Reddit(
  client_id = bot_client_id, # Recommended to use a hidden variable.
  client_secret = bot_client_id, # Recommended to use a hidden variable.
  user_agent = "follow Reddit guidelines when filling this in", # Please do
  username = "obviously put your bot name here",
  password = bot_password, # Recommended to use a hidden variable.
  validate_on_submit = True # Added to comply with upcoming Reddit guidelines.
)

# For logging purposes
print(reddit.user.me())

# haha funny function name
def lmaoSnooCockBot():
  for item in reddit.inbox.stream(skip_existing=True):
    if "u/your bot name, pretty easy to understand" in item.body.lower():
      # For logging purposes
      print(20*"--")
      print(item.body)
      print("by: ", item.author)
      print(20*"--")
      try:
        item.reply('    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡏⠀⠀⠈⡆⠀⣠⠞⢻⡀⠀⠀⠀⠀⠀⠀⠀\n    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⣶⣤⠠⠓⠋⠁⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀\n    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⣀⣀⡀⠀⢀⣾⠃⠀⠀⠀⠀⠀⠀⠀\n    ⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡤⠖⠛⠉⠉⠉⠉⠉⠙⠛⢀⣀⣀⡀⠀⠀⠀⠀\n    ⠀⠀⠀⠀⠀⠀⢀⡾⡽⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠉⠳⡄⠀⠀\n    ⠀⠀⠀⠀⠀⠀⠸⣿⢡⣾⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠀⠀\n    ⠀⠀⠀⠀⠀⠀⢰⠇⠘⠛⠃⠀⠀⠀⠀⠒⠒⠢⠀⠀⠀⠠⡤⢄⡼⠃⠀⠀\n    ⠀⠀⠀⠀⠀⠀⠸⡇⠀⠀⢀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠘⢻⠀⠀⠀⠀\n    ⠀⠀⠀⠀⠀⠀⠀⠻⣄⠀⠀⠈⠉⠉⠉⠀⠀⣴⠛⣦⠀⠀⢀⠞⠀⠀⠀⠀\n    ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣤⣀⡀⠀⠀⠀⠀⡸⠀⠈⠛⣶⠋⠀⠀⠀⠀⠀\n    ⠀⠀⠀⠀⠀⠀⠀⠀⡴⢛⡝⠁⠙⠿⡿⠛⠚⢇⠀⠀⠀⣽⠀⠀⠀⠀⠀⠀\n    ⠀⠀⠀⠀⠀⠀⠀⢸⠁⣾⠁⠀⠀⠀⠀⠀⠀⢈⣳⡦⠚⠁⠀⠀⠀⠀⠀⠀\n    ⠀⣴⢟⣿⣦⣄⡀⠈⢧⣿⠀⠀⠀⠀⠀⠀⠀⠸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀\n    ⠀⠹⣮⣷⣤⡈⠙⠛⠲⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n    ⠀⠀⠀⠀⠈⠙⠳⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀\n    ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠻⣖⠦⣤⣤⡄⠀⠀⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀\n    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠋⠀⠸⣿⡗⠀⠀⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀\n    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠒⠉⠘⠧⡤⠴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀\n    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
      except Exception as ex:
        print(ex)

if __name__ == '__main__':
  process1 = Process(target=lmaoSnooCockBot)
  process2 = Process(target=keep_alive)
  process1.start()
  process2.start()

  process1.join()
  process2.join()
