# PhantomJS
PhantomJS integration module for Python

## Easy to use:
```python
from phantomjs.phantom import Phantom
from phantomjs.driver import Driver

driver = Driver(engine='phantomjs', port=3000)
driver.start()
driver.wait_for_ready()
phantom = Phantom(driver=driver)
page = phantom.create_page()
status = page.open('http://phantomjs.org/')
print(status)
driver.kill()
```

## `Phantom`:
### Supported native functions:
* addCookie
* clearCookies
* deleteCookie
* exit
* injectJs

### `phantom.get_property`:


  Get a phantom property using `#.get_property(field)`:
  ```python
cookiesEnabled = phantom.get_property('cookiesEnabled')
  ```
### `phantom.set_property`:


  Set a phantom property using `#.set_property(field, value)`:
  ```python
cookiesEnabled = phantom.set_property('cookiesEnabled', False)
  ```

## `Page`:
### Supported native functions:
* addCookie
* childFramesCount
* childFramesName
* clearCookies
* close
* currentFrameName
* deleteCookie
* evaluateJavaScript
* getPage
* go
* goBack
* goForward
* includeJs
* injectJs
* open
* openUrl
* release
* reload
* render
* renderBase64
* sendEvent
* setContent
* stop
* switchToChildFrame
* switchToFocusedFrame
* switchToFrame
* switchToMainFrame
* switchToParentFrame
* uploadFile

### `page.get_property`:


  Get a Page property using `#.get_property(field)`:
  ```python
content = page.get_property('content')
  ```
### `page.set_property`:


  Set a Page property using `#.set_property(field, value)`:
  ```python
content = page.set_property('content', 'Hello, World!')
  ```
### `page.get_setting`:


  Get a Page setting using `#.get_setting(field)`:
  ```python
javascriptEnabled = page.get_setting('javascriptEnabled')
  ```
### `page.set_setting`:


  Set a Page setting using `#.set_setting(field, value)`:
  ```python
javascriptEnabled = page.set_setting('javascriptEnabled', False)
  ```


Feel free to contribute!
