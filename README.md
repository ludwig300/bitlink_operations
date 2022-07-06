Bitly url shortener
	
	The project creates a bitlink
	Checks the count of clicks on a bitlink

How to install

	[Service Bitly, sing up.](https://bit.ly/)

	[Generate a token](https://bitly.com/a/oauth_apps)
	GENERIC ACCESS TOKEN — Type of token. Look like this 17c09e20ad155405123ac1977542fecf00231da7
	
	Create .env file in directory bitlink_operations/ and write:

		BITLY_TOKEN = Your token
		
	Remember, it is recommended to use [virtualenv/venv](https://docs.python.org/3/library/venv.html) for better isolation.
	Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

		pip install -r requirements.txt
		
How to use

	in cmd
		
		python main.py <URL>
		
Project Goals
The code is written for educational purposes on online-course for web-developers dvmn.org.