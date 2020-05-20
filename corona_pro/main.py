from plyer import notification    #  to install=pip install plyer
import requests
from bs4 import BeautifulSoup    #  to install=pip install bs4
# function for receiving notifications
def notifyMe(title,message):
    notification.notify(title=title,message=message,
                        app_icon="C:\\Users\\rahul\\Downloads\\img.ico",#set your location of the icon and it should be .ico because plyer only supports .ico
                        timeout=20 #total time for the notifications
                        )
if __name__ == '__main__':
    try:
        html_data=requests.get('https://www.mohfw.gov.in/').text       # send request to the website...feel freee to chose any website which has all the contents
        soup = BeautifulSoup(html_data, 'html.parser')   #  web crawling is done using beautifulsoup......gets whole code of website in html format
        st=""
        for tbody in soup.find_all('tbody'):
            st+=tbody.get_text()
        nation_content=st.split("\n\n")
        #----add the state for which you want to get notifications
        fav_states=['Haryana','Delhi','Karnataka','Odisha','Maharashtra']
        for i in nation_content[1:34]:
            if(i==''):
                continue
            final_data=(i[1:].split("\n"))
            if final_data[1] in fav_states:
                heading="Corona Update"
                body=f"State :{final_data[1]}\n Cases :{final_data[2]}\n Cured :{final_data[3]}\n Death :{final_data[4]}"
                notifyMe(heading,body)
    except:
        print('CHECK COMMENTS')


        #----------------To get regular notifications put the program in while loop and set time using sleep to get notifications timely-------------


