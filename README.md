# Web Scrapping in Pond5

This project was built using the Flask Microframework. It derives data from Pond5 Website using web scraping.

### Demo

A live demo can be found [here](https://app-code-test.herokuapp.com/).

### Technologies

+ Flask Microframework (Python)
+ HTML
+ CSS


### UX

I have done a very simple web page index.html, which is similar to Pond5 website with black background and white letters. I have done web scraping with the help of Beautifulsoup.
I have scraped an image from Pond5 and displayed when the app is logged. When we request with mediainfo/<id> related image and its details wil be shown.
I have added a list of image ids (ids=['82831656','96146608','88382724','85925701','21327480']), if requested with any of these ids we can see corresponding image and related details.
if we check for ids other than these it will show errors.GET /system and GET /mediainfo/<id> returns lists and json. the output is displayed in html page using lists.


### Features

+ Scraps details from Pond5 website.
+ GET /ping request will return “pong”.
+ GET /system request returns system details.
+ GET /mediainfo/<id> (any id in ids=['82831656','96146608','88382724','85925701','21327480']) returns corresponding image and related details.
if we check for ids other than these it will show errors.

### Testing

All the testing for this project was done manually. 

Manual testing was done to ensure:

+ The site works as intended
+ Web Scraping is done correctly and Details and image is displayed as required.
+ The site was tested on  laptop screens and on an iPad, iPhone 10 and Galaxy A5 screen to test responsiveness.
+ GET /ping request return “pong”.
+ GET /system request returns system details.
+ GET /mediainfo/<id> (any id in ids=['82831656','96146608','88382724','85925701','21327480']) returns corresponding image and related details.
+ If any request other than above request is give it displayes errors.

#### Responsive 

The website have been tested in different viewports and it is responsve.


### Deployment 

This project is deployed using Heroku and GitHub.


### Run locally
The code is set up to host static assets on aws.  
To run this site locally including hosting static assets locally please use the following steps:
1. Clone the [github repository](https://github.com/femy16/code_test_pond)
2. In your terminal enter:
Every packages installed for the app is listed in requirements.txt.
```
pip3 install -r requirements.txt
```
3. To run the app from your terminal type: 
```python3 code_test.py```

### Credits

##### Media 
Fonts used were obtained from Google Fonts.

A better understanding of beautiful soup was obtained from [Python Tutorial: Web Scraping with BeautifulSoup and Requests](https://www.youtube.com/watch?v=ng2o98k983k&t=2236s).

All images and contents have been obtained from [Pond5](https://www.pond5.com/).
