#!/bin/bash
osascript -e 'tell application "Terminal" to activate' 
osascript -e 'tell application "System Events" to tell process "Terminal" to keystroke "t" using command down' 
osascript -e 'tell application "Terminal" to do script "python /Users/academia/Desktop/peanutChat/repo/src/IMServer.py" in selected tab of the front window'
for VARIABLE in {1..3}
	do
		osascript -e 'tell application "Terminal" to activate' 
		osascript -e 'tell application "System Events" to tell process "Terminal" to keystroke "t" using command down' 
		osascript -e 'tell application "Terminal" to do script "python /Users/academia/Desktop/peanutChat/repo/src/IMClient.py" in selected tab of the front window'
	done

