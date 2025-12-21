---
title: freelancer engine v0.0.1
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
highlight_theme: darkula
headingLevel: 2

---

<!-- Generator: Widdershins v4.0.1 -->

<h1 id="freelancer-engine">freelancer engine v0.0.1</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

 This **freelancer-engine** is like online superhero 🦸‍♂️<br />
    Taking care of all the GPT and AI stuff, so you can focus on making your chat ideas
      come to life 🌱<br />
    So, grab your coding cape and join the fun! Our Chat Service is here to make your development
      journey super exciting and full of learnings 🔭

Email: <a href="mailto:bipulsinghkashyap@gmail.com">:-  Bipul Kumar Singh</a> 

<h1 id="freelancer-engine-freelance-health">Freelance Health</h1>

## freelance_health_freelance_health_get

<a id="opIdfreelance_health_freelance_health_get"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /freelance_health \
  -H 'Accept: application/json'

```

```http
POST /freelance_health HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/freelance_health',
{
  method: 'POST',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.post '/freelance_health',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.post('/freelance_health', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/freelance_health', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/freelance_health");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/freelance_health", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /freelance_health`

*Freelance Health*

> Example responses

> 200 Response

```json
null
```

<h3 id="freelance_health_freelance_health_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="freelance_health_freelance_health_get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="freelancer-engine-login">Login</h1>

## register_user_register_post

<a id="opIdregister_user_register_post"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /register \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /register HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "full_name": "string",
  "email": "user@example.com",
  "phone": "stringstri",
  "role": "Provider"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/register',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/register',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/register', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/register', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/register");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/register", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /register`

*Register User*

> Body parameter

```json
{
  "full_name": "string",
  "email": "user@example.com",
  "phone": "stringstri",
  "role": "Provider"
}
```

<h3 id="register_user_register_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[UserReg](#schemauserreg)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="register_user_register_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="register_user_register_post-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## validate_otp_validate_otp_post

<a id="opIdvalidate_otp_validate_otp_post"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /validate-otp \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /validate-otp HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "otp": 0,
  "phone": "stringstri",
  "new_login": true
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/validate-otp',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/validate-otp',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/validate-otp', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/validate-otp', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/validate-otp");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/validate-otp", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /validate-otp`

*Validate Otp*

> Body parameter

```json
{
  "otp": 0,
  "phone": "stringstri",
  "new_login": true
}
```

<h3 id="validate_otp_validate_otp_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ValidOTP](#schemavalidotp)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="validate_otp_validate_otp_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="validate_otp_validate_otp_post-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## login_user_login_post

<a id="opIdlogin_user_login_post"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /login \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /login HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "phone": "stringstri"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/login',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/login',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/login', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/login', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/login");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/login", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /login`

*Login User*

> Body parameter

```json
{
  "phone": "stringstri"
}
```

<h3 id="login_user_login_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[userLogin](#schemauserlogin)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="login_user_login_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="login_user_login_post-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## resend_otp_resend_otp_post

<a id="opIdresend_otp_resend_otp_post"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /resend-otp \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /resend-otp HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "phone": "stringstri"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/resend-otp',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/resend-otp',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/resend-otp', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/resend-otp', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/resend-otp");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/resend-otp", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /resend-otp`

*Resend Otp*

> Body parameter

```json
{
  "phone": "stringstri"
}
```

<h3 id="resend_otp_resend_otp_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[userLogin](#schemauserlogin)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="resend_otp_resend_otp_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="resend_otp_resend_otp_post-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="freelancer-engine-organization">Organization</h1>

## contact_us_org_contact_us_post

<a id="opIdcontact_us_org_contact_us_post"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /org/contact-us \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: string'

```

```http
POST /org/contact-us HTTP/1.1

Content-Type: application/json
Accept: application/json
token: string

```

```javascript
const inputBody = '{
  "data": {
    "comment": "string"
  }
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'string'
};

fetch('/org/contact-us',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'string'
}

result = RestClient.post '/org/contact-us',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'string'
}

r = requests.post('/org/contact-us', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'token' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/org/contact-us', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/org/contact-us");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/org/contact-us", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /org/contact-us`

*Contact Us*

> Body parameter

```json
{
  "data": {
    "comment": "string"
  }
}
```

<h3 id="contact_us_org_contact_us_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|token|header|string|true|none|
|body|body|[Body_contact_us_org_contact_us_post](#schemabody_contact_us_org_contact_us_post)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="contact_us_org_contact_us_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="contact_us_org_contact_us_post-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## about_us_org_about_us_get

<a id="opIdabout_us_org_about_us_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /org/about-us \
  -H 'Accept: application/json' \
  -H 'token: string'

```

```http
GET /org/about-us HTTP/1.1

Accept: application/json
token: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'token':'string'
};

fetch('/org/about-us',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'string'
}

result = RestClient.get '/org/about-us',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'string'
}

r = requests.get('/org/about-us', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'token' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/org/about-us', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/org/about-us");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/org/about-us", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /org/about-us`

*About Us*

<h3 id="about_us_org_about_us_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|token|header|string|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="about_us_org_about_us_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="about_us_org_about_us_get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="freelancer-engine-user">User</h1>

## get_user_get_user_get

<a id="opIdget_user_get_user_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /get-user \
  -H 'Accept: application/json' \
  -H 'token: string'

```

```http
GET /get-user HTTP/1.1

Accept: application/json
token: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'token':'string'
};

fetch('/get-user',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'string'
}

result = RestClient.get '/get-user',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'string'
}

r = requests.get('/get-user', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'token' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/get-user', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/get-user");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/get-user", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /get-user`

*Get User*

<h3 id="get_user_get_user_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|token|header|string|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="get_user_get_user_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="get_user_get_user_get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## get_address_get_address_get

<a id="opIdget_address_get_address_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /get-address \
  -H 'Accept: application/json' \
  -H 'token: string'

```

```http
GET /get-address HTTP/1.1

Accept: application/json
token: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'token':'string'
};

fetch('/get-address',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'string'
}

result = RestClient.get '/get-address',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'string'
}

r = requests.get('/get-address', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'token' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/get-address', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/get-address");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/get-address", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /get-address`

*Get Address*

<h3 id="get_address_get_address_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|token|header|string|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="get_address_get_address_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="get_address_get_address_get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## add_address_add_address_post

<a id="opIdadd_address_add_address_post"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /add-address \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: string'

```

```http
POST /add-address HTTP/1.1

Content-Type: application/json
Accept: application/json
token: string

```

```javascript
const inputBody = '{
  "full_name": "string",
  "house": "string",
  "area": "string",
  "landmark": "string",
  "pincode": "string",
  "mobile": "stringstri"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'string'
};

fetch('/add-address',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'string'
}

result = RestClient.post '/add-address',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'string'
}

r = requests.post('/add-address', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'token' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/add-address', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/add-address");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/add-address", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /add-address`

*Add Address*

> Body parameter

```json
{
  "full_name": "string",
  "house": "string",
  "area": "string",
  "landmark": "string",
  "pincode": "string",
  "mobile": "stringstri"
}
```

<h3 id="add_address_add_address_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|token|header|string|true|none|
|body|body|[UserAddress](#schemauseraddress)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="add_address_add_address_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="add_address_add_address_post-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## delete_address_delete_address_delete

<a id="opIddelete_address_delete_address_delete"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /delete-address \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: string'

```

```http
DELETE /delete-address HTTP/1.1

Content-Type: application/json
Accept: application/json
token: string

```

```javascript
const inputBody = '{
  "address_id": 0
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'string'
};

fetch('/delete-address',
{
  method: 'DELETE',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'string'
}

result = RestClient.delete '/delete-address',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'string'
}

r = requests.delete('/delete-address', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'token' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','/delete-address', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/delete-address");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/delete-address", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /delete-address`

*Delete Address*

> Body parameter

```json
{
  "address_id": 0
}
```

<h3 id="delete_address_delete_address_delete-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|token|header|string|true|none|
|body|body|[RemoveAddress](#schemaremoveaddress)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="delete_address_delete_address_delete-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="delete_address_delete_address_delete-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## update_address_update_address_put

<a id="opIdupdate_address_update_address_put"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT /update-address \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: string'

```

```http
PUT /update-address HTTP/1.1

Content-Type: application/json
Accept: application/json
token: string

```

```javascript
const inputBody = '{
  "user_address": {
    "full_name": "string",
    "house": "string",
    "area": "string",
    "landmark": "string",
    "pincode": "string",
    "mobile": "stringstri"
  },
  "remove_address": {
    "address_id": 0
  }
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'string'
};

fetch('/update-address',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'string'
}

result = RestClient.put '/update-address',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'string'
}

r = requests.put('/update-address', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'token' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','/update-address', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/update-address");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/update-address", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /update-address`

*Update Address*

> Body parameter

```json
{
  "user_address": {
    "full_name": "string",
    "house": "string",
    "area": "string",
    "landmark": "string",
    "pincode": "string",
    "mobile": "stringstri"
  },
  "remove_address": {
    "address_id": 0
  }
}
```

<h3 id="update_address_update_address_put-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|token|header|string|true|none|
|body|body|[UpdateAddress](#schemaupdateaddress)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="update_address_update_address_put-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="update_address_update_address_put-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="freelancer-engine-landing">Landing</h1>

## home_page_home_get

<a id="opIdhome_page_home_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /home \
  -H 'Accept: application/json' \
  -H 'token: string'

```

```http
GET /home HTTP/1.1

Accept: application/json
token: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'token':'string'
};

fetch('/home',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'string'
}

result = RestClient.get '/home',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'string'
}

r = requests.get('/home', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'token' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/home', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/home");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/home", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /home`

*Home Page*

<h3 id="home_page_home_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|token|header|string|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="home_page_home_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="home_page_home_get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

# Schemas

<h2 id="tocS_Body_contact_us_org_contact_us_post">Body_contact_us_org_contact_us_post</h2>
<!-- backwards compatibility -->
<a id="schemabody_contact_us_org_contact_us_post"></a>
<a id="schema_Body_contact_us_org_contact_us_post"></a>
<a id="tocSbody_contact_us_org_contact_us_post"></a>
<a id="tocsbody_contact_us_org_contact_us_post"></a>

```json
{
  "data": {
    "comment": "string"
  }
}

```

Body_contact_us_org_contact_us_post

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|data|[ContactUS](#schemacontactus)|true|none|none|

<h2 id="tocS_ContactUS">ContactUS</h2>
<!-- backwards compatibility -->
<a id="schemacontactus"></a>
<a id="schema_ContactUS"></a>
<a id="tocScontactus"></a>
<a id="tocscontactus"></a>

```json
{
  "comment": "string"
}

```

ContactUS

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|comment|string|true|none|none|

<h2 id="tocS_HTTPValidationError">HTTPValidationError</h2>
<!-- backwards compatibility -->
<a id="schemahttpvalidationerror"></a>
<a id="schema_HTTPValidationError"></a>
<a id="tocShttpvalidationerror"></a>
<a id="tocshttpvalidationerror"></a>

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}

```

HTTPValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|detail|[[ValidationError](#schemavalidationerror)]|false|none|none|

<h2 id="tocS_RemoveAddress">RemoveAddress</h2>
<!-- backwards compatibility -->
<a id="schemaremoveaddress"></a>
<a id="schema_RemoveAddress"></a>
<a id="tocSremoveaddress"></a>
<a id="tocsremoveaddress"></a>

```json
{
  "address_id": 0
}

```

RemoveAddress

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|address_id|integer|true|none|none|

<h2 id="tocS_UpdateAddress">UpdateAddress</h2>
<!-- backwards compatibility -->
<a id="schemaupdateaddress"></a>
<a id="schema_UpdateAddress"></a>
<a id="tocSupdateaddress"></a>
<a id="tocsupdateaddress"></a>

```json
{
  "user_address": {
    "full_name": "string",
    "house": "string",
    "area": "string",
    "landmark": "string",
    "pincode": "string",
    "mobile": "stringstri"
  },
  "remove_address": {
    "address_id": 0
  }
}

```

UpdateAddress

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|user_address|[UserAddress](#schemauseraddress)|true|none|none|
|remove_address|[RemoveAddress](#schemaremoveaddress)|true|none|none|

<h2 id="tocS_UserAddress">UserAddress</h2>
<!-- backwards compatibility -->
<a id="schemauseraddress"></a>
<a id="schema_UserAddress"></a>
<a id="tocSuseraddress"></a>
<a id="tocsuseraddress"></a>

```json
{
  "full_name": "string",
  "house": "string",
  "area": "string",
  "landmark": "string",
  "pincode": "string",
  "mobile": "stringstri"
}

```

UserAddress

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|full_name|string|true|none|none|
|house|string|true|none|none|
|area|string|true|none|none|
|landmark|string|true|none|none|
|pincode|string|true|none|none|
|mobile|string|true|none|none|

<h2 id="tocS_UserReg">UserReg</h2>
<!-- backwards compatibility -->
<a id="schemauserreg"></a>
<a id="schema_UserReg"></a>
<a id="tocSuserreg"></a>
<a id="tocsuserreg"></a>

```json
{
  "full_name": "string",
  "email": "user@example.com",
  "phone": "stringstri",
  "role": "Provider"
}

```

UserReg

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|full_name|string|true|none|none|
|email|string(email)|true|none|none|
|phone|string|true|none|none|
|role|string|true|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|role|Provider|
|role|Customer|

<h2 id="tocS_ValidOTP">ValidOTP</h2>
<!-- backwards compatibility -->
<a id="schemavalidotp"></a>
<a id="schema_ValidOTP"></a>
<a id="tocSvalidotp"></a>
<a id="tocsvalidotp"></a>

```json
{
  "otp": 0,
  "phone": "stringstri",
  "new_login": true
}

```

ValidOTP

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|otp|integer|true|none|none|
|phone|string|true|none|none|
|new_login|boolean|true|none|none|

<h2 id="tocS_ValidationError">ValidationError</h2>
<!-- backwards compatibility -->
<a id="schemavalidationerror"></a>
<a id="schema_ValidationError"></a>
<a id="tocSvalidationerror"></a>
<a id="tocsvalidationerror"></a>

```json
{
  "loc": [
    "string"
  ],
  "msg": "string",
  "type": "string"
}

```

ValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|loc|[anyOf]|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|msg|string|true|none|none|
|type|string|true|none|none|

<h2 id="tocS_userLogin">userLogin</h2>
<!-- backwards compatibility -->
<a id="schemauserlogin"></a>
<a id="schema_userLogin"></a>
<a id="tocSuserlogin"></a>
<a id="tocsuserlogin"></a>

```json
{
  "phone": "stringstri"
}

```

userLogin

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|phone|string|true|none|none|

