from bs4 import BeautifulSoup
import requests
import platform
from flask import Flask,render_template,request,redirect,url_for,jsonify
import os
import json
# print(os.uname())
# print(platform.sys.version);
# print(platform.system())

ids=['82831656','96146608','88382724','88382724']
stm=[{
    "opt_system":platform.system(),
    "system_version":platform.sys.version
}]
app = Flask(__name__)

source=requests.get("https://www.pond5.com/photo/82831656/business-people-conversation-technology-hand.html").text

def find_pic(source):
    soup=BeautifulSoup(source,'lxml')
    mydiv=soup.find('div',class_='p5_big_image')
    mypicture=mydiv.find('img')['src']
    mypic_id=mypicture.split('/')[3].split('-')[6]
    return(mypicture)
# print(platform.platform())
@app.route("/",methods=["GET"])
def show_Image():
     mypic=find_pic(source)
     return render_template("index.html",mypic=mypic)
     
@app.route("/ping",methods=["GET"])
def ping_pong():
    pong="Pong"
    return render_template("index.html",pong=pong)
    
@app.route("/system",methods=["GET"])
def system_details():
    return render_template("index.html",system=stm)
    
@app.route("/mediainfo/<id>",methods=["GET"])
def media_details(id):
    if id in ids:
        source=requests.get('https://www.pond5.com/photo/'+id).text
        soup=BeautifulSoup(source,'lxml')
        mydiv=soup.find('div',class_='p5_big_image')
        mypic=mydiv.find('img')['src']
        print(mypic)
        mypic_id=mypic.split('/')[3].split('-')[6]
        image_title_hedding=soup.find('h1',class_='Site-sectionHeadingAlt')
        heading=image_title_hedding.find('span').text
        
        pic_details=[{
        "image_filename":mypic_id,
        "image_title":heading,
        }]
        pic_size_dimensions=[]
        for image_size_div in soup.find_all('div',class_='Arrange--gutter10px'):
                size=image_size_div.find('span',class_='u-textLineHeightMatch').text
                dimension = image_size_div.find('div',class_='u-textLineHeightMatch').text
                # print(dimension)
                
                pic_size_dimensions.append('Size: '+size)
                pic_size_dimensions.append('Dimension: '+dimension)
                # pic_details[0]['size'] = size
                # pic_details[0]['dimension'] = dimension
                
                
        # print(pic_size_dimensions)    
    
       
        # data=json.loads(pic_details)
        
        
        return render_template("index.html",mypic=mypic,pic_details=pic_details,pic_size_dimensions=pic_size_dimensions)
    else:
        return("Id out of range")
    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8081, debug=True)
