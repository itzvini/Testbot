from highrise.__main__ import BotDefinition, main, import_module, arun
import time

room_id = "634b1d865fe6f2c1cd36975f"
bot_token = "ec2e42db96e06b6e8c6b59611e74eda7ca8f89264a07dabcc567c44fcadcca9c"
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
