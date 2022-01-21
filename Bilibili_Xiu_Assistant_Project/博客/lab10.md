| The Link Your Class                        | [https://bbs.csdn.net/forums/MUEE308FZ](https://bbs.csdn.net/forums/MUEE308FZ) |
| :----------------------------------------- | :----------------------------------------------------------- |
| The Link of Requirement of This Assignment | https://bbs.csdn.net/topics/603608738                        |
| The Name of Team                           | Langcent互联网股份有限公司                                   |
| The Goal of This Assignment                | Alpha Sprint                                                 |
| Leader's MU STU ID and Name                | 19103069  Jian Lang                                          |
| Teammate 1's MU STU ID and Name            | 19104120  Wei Xie                                            |
| Teammate 2's MU STU ID and Name            | 19103620  Yuxiang He                                         |
| Teammate 3's MU STU ID and Name            | 19105584  Diancong Wu                                        |
| Teammate 4's MU STU ID and Name            | 19103778  Zekai Wang                                         |

## I.Problem List After Alpha Spring

✴️ ***Problems Encountered:***

1️⃣ As for obtaining the search results of Bilibili by crawler, if the page variable in the URL is always changed through the for loop, the website server will consider it as malicious crawling data and will refuse access. 

2️⃣ In the aspect of obtaining data, there is a problem that obtaining data with a single interface is not comprehensive. Sometimes it is necessary to use multiple interfaces for the same object to obtain enough target information, and finding usable interfaces has become an urgent problem to be solved.

3️⃣ How to flexibly set the update days. 

4️⃣ If a request is initiated in the Wechat applet, it must be encrypted using HTTPS in the back-end protocol. Otherwise, the access fails.

5️⃣ Do not know how to change the state of a single object obtained from the back-end.

------

✳️ ***The way to deal with:***

1️⃣ Decided to set page as the first page of data. Because the Upper data we crawled is sorted according to the attention heat. From the practical point of view, the following several results do not attract too much attention, naturally there is no possibility of attention.

2️⃣ Obtain the information interface of the web page through the developer tool of edge browser to get the required information

3️⃣ Decide to add an item in the user model database to allow users to customize their own update days. And the corresponding interface to modify the days.

4️⃣ Our group decided to apply for a domain name to resolve our server IP address, and use HTTPS to encrypt the domain name to meet the requirements of the applet backend.

5️⃣ This can be solved by adding a object array and set the name of each slot to a sequent number.

## II.UML

✅ ***Class Diagram:***

![UML类图](C:\Users\大瞎蘸酱\Desktop\Bilibili咻管家项目\博客\1-7天通用\每日提交图片集合\UML图\UML类图.jpg)

------

✅ ***Use Case Diagram:***

![UML用例](C:\Users\大瞎蘸酱\Desktop\Bilibili咻管家项目\博客\1-7天通用\每日提交图片集合\UML图\UML用例.jpg)

------

✅ ***Sequence Diagram:***

![UML网站序列](C:\Users\大瞎蘸酱\Desktop\Bilibili咻管家项目\博客\1-7天通用\每日提交图片集合\UML图\UML网站序列.jpg)

------

✅ ***State Diagram:***

![系统UML状态图](C:\Users\大瞎蘸酱\Desktop\Bilibili咻管家项目\博客\1-7天通用\每日提交图片集合\UML图\系统UML状态图.jpg)

------

✅ ***Activity Diagram:***

![系统UML活动图](C:\Users\大瞎蘸酱\Desktop\Bilibili咻管家项目\博客\1-7天通用\每日提交图片集合\UML图\系统UML活动图.jpg)

## III.Actual Progress of The Project

**1️⃣** **Registeration Page**

This is the registration page ,which is the beginning of the whole applet. Here you are required to register the user name, enter a password, upload a profile, and bind a UID (each Bilibili user has his or her own UID number). It is important to note that if the UID does not exist or cannot access the concerned information, the registration will fail. Once determined, the UID cannot be changed. Then you can click the button below to go to the login interface. 

------

**2️⃣** **Login Page**

This is the login page. If you have already registered your account in our applet, you can login directly to use it. Otherwise you must click the register button below to register.

------

**3️⃣** **Search and Search Result Page**

This is the search page, mainly based on the name provided by the user to obtain the search results of Upper. In order to facilitate the user's search, the search results will be ranked according to the number of followers followed fans from the highest to the lowest. By the way, the more complete your name is, the easier it is to get the result you want.

图

This is result the search page gets, with the profile picture and name of each Upper. The user can select Upper and click the red heart button to add it to the applet's special concerns list.

------

4️⃣ **Xiu Friends Page** 

This is your friend's personal information. We can see the UID, profile, and sign that the friend is bound to. We also have access to our friends' special concerns list and Bilibili's concerns list according to his bound UID.

------

5️⃣ **Search Friends and Search Friends Result** **Page**

This is the friends search page, and you can search for anyone who has signed up for the applet. And add him as a friend.

图

We found the user by inputting the username, and clicked the button on the right to add the user as a friend.

------

6️⃣ **Xiu Friends Personal Page** 

This applet we also provide a friend function. On the friends page, you can view the user's friends, delete friends or search to add new friends.In addition, clicking on your friend's profile picture will give you access to some information about your friend.

------

7️⃣ **Mine Page**

This is the user information page, where we have many of our core functions. First you can change your sign and profile here. And you can view the followed uppers in the applet whether there is an update video on Bilibili, followed Uppers witch bound UID concerns, special concern list and other functions(Being developed).

------

8️⃣ **Focused Page**

Just like the registration function mentioned above, each user needs to bind a UID of Bilibili, and this page is to obtain the following uppers of Bilibili through the bound UID. And we can add these concerns to our special concerns list on our applet.

------

9️⃣ **Special Care List Page**

This is one of the core parts of the whole applet - the special care list. Uppers we followed in this list will be pushed their latest videos in the near future.

------

**1️⃣**0️⃣ **Setting Page**

This page is aimed at providing users a way to change some properties. For example, they can select the days they want to obtained the broadcasted videos.

------

## IV.Github Repository Link

|                       Code Repository                        |                     Document Respository                     |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
| https://github.com/LobsterJian/Bilibili_Xiu_Assistant_Code_Repository.git | https://github.com/LobsterJian/Bilibili_Xiu_Assistant_Document_Repository.git |

## V.Team Members' Experience

1️⃣ **Leader: Jian Lang**

The day just before I wrote this blog, I successfully overcame a big problem in our whole project. I must say after alpha sprint, given we have figured out all the core methods of developing, we do things easily in such a long time. However, just in last week, when my members and I have finished all the functions and tend to make the mini program be published in Wechat applet, then the problem came. We need to use domain name instead of using ip address to visit the web server. However, we do not have a domain name. Then after keep trying for several days, I finally find a way to bind our ip address with our domain name(Newly registered). Also in last day, I overcame this problem. And at that time, I think I can overcome every problems encounted in the future.

------

2️⃣ **Member: Wei Xie**

After the Alpha sprint, as the subsequent projects became more and more perfect and the demand became more and more, the functions became more and more complete, I really realized what is the pressure of demand. Then in the interaction with the front end is also to understand a lot of network layer knowledge, increased the fun of coding. For example, operation database, installation framework, management background and so on. At the same time, this project also let me really realized how to develop a project to the entire small program development online process.

------

3️⃣ **Member: Yuxiang He**

The project development after alpha sprint makes me really understand what is demand changing anytime and anywhere. Sometimes you will constantly change the code because of the changing demand. Sometimes you also need to add code according to the newly added demand. Writing it for many times has greatly improved my coding ability and exercised myself. In addition, after the alpha sprint, more and more things between the front-end and back-end need to be communicated. In this process, it not only makes me better understand how the whole project is realized, but also makes me proficient in how to express my ideas clearly, which is a great improvement for me in teamwork aspect.

------

4️⃣ **Member: Diancong Wu**

During the period after the Alpha Sprint, our project became more and more perfect, with more and more functions needed to be implemented, and we had higher requirements for the overall beauty and smoothness of the front-end. During this process, I deeply understood the problems and difficulties encountered in front-end development. Also, because some of the functionality required backend collaboration, I learned a little about databases. The most important thing is that through this project, I understand the development of a small program that can be used from scratch with practice, and help me better understand the course knowledge of this semester.

------

5️⃣ **Member: Zekai Wang**

After Alpha sprint, more and more, I feel my weakness of the front, from the beginning that through the study of short time I can do, now finds myself just understand code should be how to write, but don't know how to use is appropriate, I feel that I must follow the ongoing projects of actual combat, I can really do front-end development on my own, thanks to my teammates for their help. This time we help each other to learn from each other, I am very happy.
