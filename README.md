## Courser

A project that scrapes all the relevant information for the courses offered for Master's at NUS and stores it in a consolidated PDF.

## Why?

There were number of pages that needed to traversed for going thourgh all course info and stuff. Like timtable was on a separate page, course description was in a different portal and those also had layers of levels within them. 

I wanted all this info at once place so that I don't have to navigate between multiple chrome tabs and more imortantly I can share the info with Shadab for discussion.


## Workflow

### Run course_list.py

* Requests desired page - https://mysoc.nus.edu.sg/~postgd/LecturePreview.html that contain master list of courses that'll be offered this sem.
* Parse html obtained from above and get intermediate IVLE links for each course -  
Eg. - https://ivle.nus.edu.sg/lms/list_course.aspx?code=CS4211&acadyear=2017/2018
* Store all these intermediate links in a file - ivle_links.txt


### Run courses_desc.py

* Read ivle_links.txt and extract final url for each course that contains all the information.
Eg. - https://ivle.nus.edu.sg/Module/Student/default.aspx?CourseID=BE4CE92A-0E2C-4160-91BB-F26912239937&ClickFrom=StuViewBtn
* Store all course final links to a new file - final_links.txt

### Run download_info.py

* Read all final links from final_links.txt
* Extract the most sane parent div tag and all its relevant content
* Dump div tags of all courses to a master html file


### Convert html to pdf

Finally, convert master html file to pdf via pandoc.


### TODO

* Need a better name for the project :p
* Generate master PDF!!
* FInd a way to merge module information and slides - Should be doable..!!
* On the IVLE portal, information does not exist for some of the modules,check with seniors
* If information for some course does not exist, fetch it from course catalogue? - Would be tough anyway.
* Merge timetable and corresponding course information - Tough!!
* Code Improvements - Rename variables and scripts so they have more meaning..!!
* Discuss potential network issues with Shadab, from NUS.
