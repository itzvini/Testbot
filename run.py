from highrise.__main__ import BotDefinition, main, import_module, arun
import time

room_id = "65e93ab505782ba2fe3745c7"
bot_token = "559e0fc1599e679b49704bd55939f00dc57057a41a976826d52afebcee9b22ad"
bot_file = "main"
bot_class = "MyBot"

if __name__ == "__main__":
  definitions = [
	  BotDefinition(
	    getattr(import_module(bot_file), bot_class)(),
      room_id, 
			bot_token)]  # More BotDefinition classes can be added to the definitions list
  while True:
    try:
      arun(main(definitions))
    except Exception as e:
      # Print the full traceback for the exception
      import traceback
      print("Caught an exception:")
      traceback.print_exc()  # This will print the full traceback       
      time.sleep(10)       
      continue
