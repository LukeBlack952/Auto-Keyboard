import keyboard
msg = input("What do you want to send? >> ")
mt = input("Select Message Type (Discord or Default) >> ")
if mt.upper() == "DISCORD":
    t = "shift+enter"
elif mt.upper() == "DEFAULT":
    t = "enter"
print("Press CTRL when you want to activate the script.")
keyboard.wait("ctrl")
keyboard.write("This was written using Auto Keyboard by LukeBlack952 (GitHub)",delay=0.01)
keyboard.press_and_release(str(t),do_release=True)
keyboard.press_and_release(str(t),do_release=True)
keyboard.write(str(msg),delay=0.01)
keyboard.press_and_release("enter",do_release=True)
print("Done!")
keyboard.press_and_release("ctrl+shift+esc",do_release=True)
print("You can close Task Manager, it opened because it cancels the script from running.")
input()
