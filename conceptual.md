### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  *Python syntax is based on indentation/code blocks which can enhance readability where are Javascript syntax uses semicolons and curly bracers to define code blocks. In Python you do not need to declare a variable with const/var/let however this means that you also can change variables even if they should stay the same unlike Javascript which is more rigid in what each variable type can and cannot do.

  *Javascript is mainly used for web developemnt and essential for front-end development specifically. Python on the other hand seems to be more focued on backend and is also used in other areas such as data analysis and computer science.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  *Python's built in .get("c") would return either the value associated with key "c" or a default value instead of raising an error
  *if/else statment where you print(dict['c'])else print('key not found') - either way you are making sure that the app has something to return within the code block

- What is a unit test?
  *when writing an app it is best to test each individual component or unit of the application to ensure that they work correctly apart so when we put them together we can break down the issues better should there be one. You want to think of a unit as each funtion/method and work through the steps individually. The tests should focus on fast execution and make sure that the behavior is repeatable in a multitude of situations

- What is an integration test?
  *once we are done with unit testing we move onto integration tests which  check how the units work together - this is more of a 'real world" situation and can identify issues that may arise once the units are interacting with each other

- What is the role of web application framework, like Flask?
  *frameworks provide a set of tools, libraries and help to organize/structure code. Many have templates (jinja), definire URL routs to handle HTTP requests, process form handling and database interactions, etc.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  *a route URL can be more descriptive and user friendly however this can cause the URLs to be long and confusing. Query params offer more flexibilty  but are less readable/user friendly. Also this one should not use sensative data

- How do you collect data from a URL placeholder parameter using Flask?
  *By using the route() decorator and specify the param's name within brackets. Then when the request is made to the route Flask will extract the value from the URL

- How do you collect data from the query string using Flask?
  *The query string uses key-value pairs at the end of the URL and we can grab them through the request object which provides access to data sent in the request with request.args 

- How do you collect data from the body of the request using Flask?
  *using the request object and the method that best works for you based on your request type. For example you might need form data in a POST request and you would use the request.form for a dictionary like object with key value pairs. Once you have access to it you can then save them to variables for use in different functions.

- What is a cookie and what kinds of things are they commonly used for?
  *a cookie is a pice of data that a user's browser stores on a device and can send back to the server with every request so the server can ID the user and maintain information to be sent back. Its used for personalization of websites, remembering preferences, session management, and so on.

- What is the session object in Flask?
  *a built in features that stores user specific data across requests without cookies or URL params . The data is exncrypted ensuring that it cannot be tampered with or read by the client. Stored on server side so we should avoid storying large amounts of data or else it can bog down the performance.

- What does Flask's `jsonify()` do?
  *.jsonify() that creates a JSON response from Python data structures and is useful when building RESTful APIs in Flask