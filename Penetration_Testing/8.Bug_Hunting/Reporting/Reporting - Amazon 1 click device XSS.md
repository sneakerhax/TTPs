# Reporting - Amazon 1 click device XSS

I wanted to share a bug that is far from complicated but drives home the point that all data that is controlled by a user should be sanitized & output encoded if it will return back to the client. Sometimes because of the nature of the data developers assume that certain types of input can’t exist there. This is a trick I have used to find multiple bugs in the past couple of years.

All of my personal devices such as iPhone and iPad  have names that can trigger XSS. I achieve this by naming the device some XSS payload such as the simple one found below:

![alt text](.img/Amazon%20-%201%20click%20XSS%20iphone%20payload.png)

This has triggered XSS on many different softwares including notification software, routers, and in this case Amazon. It does this because many of these softwares have a page that lists devices and is viewed by other users. In the case of Amazon the XSS was triggered when accessing the one click devices. The bug was reported through email as seen in the next section.

### Reporting the bug to Amazon

Report date: July 19th 2017

Issue fix confirmed: November 13th 2017

Reported to: Amazon Security [security@amazon.com]

Bug Type: XSS(Stored)

Description:
Under the account settings for 1 click purchasing which can be found here:
Your Account > Manage Default Address and 1-Click Settings
The device names listed under 1-Click Status are not sanitized
 
POC:
My phone name is <script>alert(1)</script> and once this is loaded into the 1-Click Status an alert window appears with the number 1

![alt text](.img/Amazon%20-%201%20click%20XSS%20POC.png)

![alt text](.img/Amazon%20-%201%20click%20XSS%20browser%20console.png)

If you need additional information please let me know.

Thanks,

Justin

### Discovery of mobile compatibility and reporting (Update)

Additionally later I found that this could be triggered from a mobile phone as seen in the example below. This update was reported to Amazon on August 19th 2017:

![alt text](.img/Amazon%20-%201%20click%20XSS%20mobile%20POC.png)

### Fix implemantation

This issue was fixed by adding output encoding to the device listing. Additionally they have moved 1-click device listing to it’s own page under Your Account -> 1-Click settings -> Manager 1-Click for your devices:

![alt text](.img/Amazon%20-%201%20click%20XSS%20-%20fix.png)

### Conclusion

In this case the 1 click device list is only something that the user would view and the attack vector is through the name of their device. This means the only valid attack vector as I specified to them in a later email is to attack reps who assist me with my account and have to view my 1 click devices for troubleshooting. This however is not always the case in all bugs I have discovered. In other bugs I have discovered other users would be affected by my XSS payload.
