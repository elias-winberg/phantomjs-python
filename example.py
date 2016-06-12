from phantomjs.driver import Driver
from phantomjs.phantom import Phantom


def on_page_1_event(sender, event):
    print(event)


def log(sender, line):
    print(line)


# Create a Driver (assumes that the PhantomJS executable has been added to the PATH, and that port 3000 is not in use).
driver = Driver(engine='phantomjs', port=3000)

# Connect the 'on_stderr' event to the 'log' function.
driver.on_stderr.connect(log, sender=driver)

# Connect the 'on_stdout' event to the 'log' function.
driver.on_stdout.connect(log, sender=driver)

# Start the driver with the PhantomJS command-line option 'debug' set to 'true'.
driver.start(('--debug', 'true'))

# Wait a maximum of five seconds for the driver to start.
ready = driver.wait_for_ready(timeout=5)

# Assert that the driver was successfully started.
assert (ready is True)

# Create a Phantom instance.
phantom = Phantom(driver)

# Create a new Page.
page_1 = phantom.create_web_page()

# Connect the 'on_event' event with the 'on_page_1_event' function.
page_1.on_event.connect(on_page_1_event, sender=page_1)

# Try to open 'phantomjs.org'.
status = page_1.open('http://phantomjs.org/')

# Assert that 'phantomjs.org' was successfully opened.
assert (status == 'success')

# Get the title of the current page.
title_1 = page_1.get_property('title')

# Get the title of the current page by evaluating a JavaScript function in the context of the web page.
title_2 = page_1.evaluateJavaScript('function(){return document.title;}')

# Assert that 'title_1' equals to 'title_2'.
assert (title_1 == title_2)

# Close the page.
page_1.close()

# Kill the driver.
driver.kill()
