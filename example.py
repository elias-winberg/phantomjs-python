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
