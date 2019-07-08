# Report - Amazon 1 click device XSS

I wanted to share a bug that is far from complicated but drives home the point that all data that is controlled by a user should be sanitized & output encoded if it will return back to the client. Sometimes because of the nature of the data developers assume that certain types of input can’t exist there. This is a trick I have used to find multiple bugs in the past couple of years.

All of my personal devices such as iPhone and iPad  have names that can trigger XSS. I achieve this by naming the device some XSS payload such as the simple one found below:

