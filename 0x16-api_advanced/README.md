# API advanced
[<](https://github.com/TheeKingZa/alx-system_engineering-devops/tree/master/0x15-api/README.md) 0x16 [>](https://github.com/TheeKingZa/alx-system_engineering-devops/blob/master/0x17-web_stack_debugging_3/README.md)
---

# Background Context
```
  Questions involving APIs are common for interviews.
  Sometimes they’re as simple as ‘write a Python script that queries a given endpoint’,
  sometimes they require you to use recursive functions and format/sort the results.

  A great API to use for some practice is the Reddit API.
  There’s a lot of endpoints available,
  many that don’t require any form of authentication,
  and there’s tons of information to be parsed out and presented.
  Getting comfortable with API calls now can save you some face
  during technical interviews and even outside of the job market,
  you might find personal use cases to make your life a little bit easier.
```
---

# Read or watch:

* [Reddit API Documentation](https://www.reddit.com/dev/api/)
* [Query String](https://en.wikipedia.org/wiki/Query_string)

---

# NEED TO KNOW?
* [How to read API documentation to find the endpoints you’re looking for](#how-to-read-api-documentation-to-find-the-endpoints-you're-looking-for)
* [How to use an API with pagination](#how-to-use-an-api)
* [How to parse JSON results from an API](#how-to-parse-json-results-from-an-api)
* [How to make a recursive API call](#how-to-make-a-recursive-api-call)
* [How to sort a dictionary by value](#how-to-sort-a-dictionary-by-value)

---

# How to read API documentation to find the endpoints you’re looking for:

```
  When exploring the Reddit API documentation,
  look for sections that describe available endpoints.
  For example, to retrieve information about a subreddit's hot posts,
  you might find an endpoint like /r/{subreddit}/hot.
  Review the parameters and expected responses to understand how to structure your API requests.
```
---

[^](#need-to-know)

---

# How to use an API with pagination:
```
  APIs often use pagination to limit the number of results returned in a single response.
  Look for parameters like limit and after in the documentation.
  For instance, in a Reddit API request,
  you can use limit to specify the number of items per page
  and after to indicate the starting point for the next page.
```
---

[^](#need-to-know)

---

# How to parse JSON results from an API:

  * After making an API request, the response is typically in JSON format. Use your programming language's JSON parsing capabilities. In Python, for example, you can use the json module:
```
    import json

    response_data = '{"key": "value"}'
    parsed_data = json.loads(response_data)
    print(parsed_data['key'])  # Accessing the parsed data

```
---

[^](#need-to-know)

---

# How to make a recursive API call:

```
  Recursive API calls are often needed for paginated responses.
  Design a function that calls the API and,
  if there are more pages (after parameter),
  recursively calls itself with the updated parameters.
```
Example in Python:
```
  import requests

  def recursive_api_call(url, params=None):
      response = requests.get(url, params=params)
      data = response.json()

      # Process data...

      after = data.get('after')
      if after:
          params['after'] = after
          recursive_api_call(url, params)
```
---

[^](#need-to-know)

---
# How to sort a dictionary by value:
* Sorting a dictionary by values can be achieved using the sorted function in Python.

Example:
```
  my_dict = {'apple': 3, 'banana': 1, 'orange': 2}
  sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

  print(sorted_dict)
  # Output: {'banana': 1, 'orange': 2, 'apple': 3}
```

```
  In this example, key=lambda item:
  item[1] specifies that the sorting should be based on
  the values (item[1]) of the dictionary items.
  Adjust the key function based on your specific sorting requirements.
```
---

[^](#need-to-know)
