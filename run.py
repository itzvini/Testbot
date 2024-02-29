from highrise.__main__ import BotDefinition, main, import_module, arun
import time

room_id = "65c55ac2e041cb2e84e2c40d"
bot_token = "6581b5686f7f3beafedc3dd67c5aeb19429044efe81ac82f821edc7af06c0005"
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
