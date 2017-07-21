## Courser

A project that scrapes all the relevant information for the courses offered for Master's at NUS and stores it in a consolidated PDF.

## Why?

There were number of pages that needed to traversed for understanding all course info.
Like timtable was on a separate page, course description was in a different portal and those too had layers of levels within them. 

I want all this info at once place so that I don't have to navigate between multiple chrome tabs and more imortantly I can share the info with Shadab.
Since all these info is under a portal he can't access it. 


## Workflow

### script 1 - all_courses.py

* request.get desired page - https://mysoc.nus.edu.sg/~postgd/LecturePreview.html and sent coockies
* Parse html, get following link
    * https://ivle.nus.edu.sg/lms/list_course.aspx?code=CS4211&acadyear=2017/2018
    * request.get above page, send coockies again
* Parse html, get following link
    * https://ivle.nus.edu.sg/Module/Student/default.aspx?CourseID=BE4CE92A-0E2C-4160-91BB-F26912239937&ClickFrom=StuViewBtn
    * Store this link in file/json


### script 2 - courses_info.py

* Create a master html file that would store all info
* for each line in saved file/json
    request.get line and send coockies
    Parse html and extract relevant data
    Write this data to master html file


### Convert html to pdf

Finally, convert master html file to pdf via pandoc.

