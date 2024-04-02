# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.





## Code Validation


### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.
![screenshot](documentation/pic5.png)


### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
|  | question.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ben1998-hub/Game-Quiz2/main/question.py) | ![screenshot](documentation/pic6.png) | |
|  | run.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ben1998-hub/Game-Quiz2/main/run.py) | ![screenshot](documentation/pic7.png) | |

## Browser Compatibility


Recommended browsers to consider:
- [Chrome](https://www.google.com/chrome)
- [Firefox (Developer Edition)](https://www.mozilla.org/firefox/developer)
- [Edge](https://www.microsoft.com/edge)
- [Safari](https://support.apple.com/downloads/safari)
- [Brave](https://brave.com/download)
- [Opera](https://www.opera.com/download)



🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | About | Contact ||Notes |
| --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/c1.png) | ![screenshot](documentation/c2.png) | ![screenshot](documentation/c3.png) |  | Works as expected |
| Firefox | ![screenshot](documentation/f1.png) | ![screenshot](documentation/f2.png) | ![screenshot](documentation/f3.png) |  | Works as expected |
| Edge | ![screenshot](documentation/e1.png) | ![screenshot](documentation/e2.png) | ![screenshot](documentation/e3.png) |  | Works as expected |

| repeat for any other tested browsers | x | x | x | x | x |

## Responsiveness




I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | About | Contact || Notes |
| --- | --- | --- | --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/iphone1.png) | ![screenshot](documentation/iphone2.png) | ![screenshot](documentation/iphone3.png) |  | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/ipad1.png) | ![screenshot](documentation/ipad2.png) | ![screenshot](documentation/ipad3.png) | | Works as expected |
| Desktop | ![screenshot](documentation/d1.png) | ![screenshot](documentation/d2.png) | ![screenshot](documentation/d3.png) |  | Works as expected |
 
| repeat for any other tested browsers | x | x | x | x | x |

## Lighthouse Audit



I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/light1.png) | ![screenshot](documentation/light2.png) | Some minor warnings |
| About | ![screenshot](documentation/light3.png) | ![screenshot](documentation/light4.png) | Some minor warnings |
| Gallery | ![screenshot](documentation/light5.png) | ![screenshot](documentation/light6.png) | Slow response time due to large images |
| x | x | x | repeat for any other tested pages/sizes |

## Defensive Programming




.

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Home | | | | | |
| | Feature is expected to do nothing when the user does an incorrect input | Tested the feature by doing lots of incorrect inputs | The feature behaved as expected, | Test concluded and passed | ![screenshot](documentation/p1.png) |
| |
| | |
| Rules | | | | | |
| |
| | Feature is expected to list all rules when the user inputs B | Tested the feature by doing making sure the user can't crash the site with an incorrect input | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/p2.png) |
| start | | | | | |
| ||
| | Feature is expected to do start quiz when the user inputs a | Tested the feature by doing lots of random inputs | The feature did not respond to z, B, or C. |  | ![screenshot](documentation/p3.png) |

| repeat for all remaining pages | x | x | x | x | x |



| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Home | | | | |
| | press a | Redirectied to quiz | Pass | |
| | press b | Redirectied to rules | Pass | |
| | press c | Redirectied to end quiz | pass | |

| repeat for all remaining pages | x | x | x | x |



## Bugs




  





If you legitimately cannot find any unfixed bugs or warnings, then use the following sentence:


> [!NOTE]  
> There are no remaining bugs that I am aware of.
