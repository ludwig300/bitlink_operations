**Bitly url shortener**

- **The project** 
  - Creates a bitlinks
  - Checks the count of clicks on a bitlinks

- **Installing required dependencies**

  - [Service Bitly, sing up.](https://bit.ly/)

  - [Generate a token](https://bitly.com/a/oauth_apps)

    **GENERIC ACCESS TOKEN** — Type of token. Look like this *17c09e20ad155405123ac1977542fecf00231da7*
	
- **Setting environment variables**
  - Create ***.env*** file in directory **bitlink_operations/** and write:

	    BITLY_TOKEN = Your token
		
  -  -+
  -  Remember, it is recommended to use [virtualenv/venv](https://docs.python.org/3/library/venv.html) for better isolation.
     Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

	     pip install -r requirements.txt
		
- **Application launch**

  - Open directory **bitlink_operations/** from **cmd**
      
            python main.py <URL>

    Replace <URL> with **URL** to create a bitlink or replace with a **bitlink** to get the count of clicks. 
	
*Project Goals
 The code is written for educational purposes on online-course for web-developers dvmn.org.*
