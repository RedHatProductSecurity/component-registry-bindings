# component-registry-bindings
Python bindings for accessing the Component Registry data entities in native python.

## Requirements

* Python 3
* pip

## Installation

You can install the bindings via Python 3 pip:

* directly from the [GitHub](https://github.com/RedHatProductSecurity/component-registry-bindings) repository (will install the version from master branch)
    ```
    pip install -e git+https://github.com/RedHatProductSecurity/component-registry-bindings#egg=component_registry_bindings
    ```

## Component Registry Compatibility

Component Registry and bindings both uses [semantic versioning](https://semver.org/) (eg. MAJOR.MINOR.PATCH, 1.2.3). Bindings are compatible with Component Registry when MAJOR and MINOR version matches.

Eg.
* Component Registry 1.2.0, bindings 1.2.0 - compatible
* Component Registry 1.2.0, bindings 1.2.1 - compatible
* Component Registry 1.2.2, bindings 1.2.1 - compatible
* Component Registry 1.3.0, bindings 1.2.1 - **feature incomplete**
* Component Registry 2.0.0, bindings 1.9.9 - **incompatible**

## Usage

### Import the bindings

```python
import component_registry_bindings
```

### Create a session
Session is the main part of the bindings which you will be using. You can create it using the `component_registry_bindings.new_session`. Created session is then used to access the various endpoints.

You must always specify `component_registry_server_uri` of the Component Registry instance you want to access.

By default, the SSL verification is enabled, you can disable it by passing `verify_ssl` argument
```python
session = component_registry_bindings.new_session(component_registry_server_uri="<component registry uri>", username="<username>", password="<password>", verify_ssl=False)
```

### Session operations

This section describes possible session operations. See [response section](#response) to learn how to work with obtained operation responses.

Operations can be performed on the following entities
* builds
* channels
* components
* products
* product_versions
* product_streams
* product_variants

#### status

  Most basic operation of the session is retrieving the status.

  See /GET /api/{api_version}/status` in [API docs](openapi_schema.yml) for more details (query parameters, response format, etc.)

```python
    status_response = session.status()
```

#### builds.retrieve_list

  Retrieve a list of Builds.

  See /GET /api/{api_version}/builds in [API docs](openapi_schema.yml) for more details (query parameters, response format, etc.)
```python
    all_builds = session.builds.retrieve_list()
    select_builds = session.builds.retrieve_list(type="BREW")
```

#### builds.retrieve

Retrieve a single Build with specified 'id'.
See `/GET /api/{api_version}/builds/{id}` in [API docs](openapi_schema.yml) for more details (query parameters, response format, etc.)

```python
session.builds.retrieve(id="1872838")
```

#### components.retrieve_list

Retrieve a list of Components.

See `/GET /api/{api_version}/components` in [API docs](openapi_schema.yml) for more details (query parameters, response format, etc.)
```python
  all_components = session.components.retrieve_list()
  select_components = session.components.retrieve_list(arch="x86_64")
```

#### components.retrieve

Retrieve a single Component with specified `id`.

See `/GET /api/{api_version}/components/{id}` in [API docs](openapi_schema.yml) for more details (query parameters, response format, etc.)
```python
session.components.retrieve(id="be2e8441-b188-483a-be4a-c040e8c665d2")
```

#### search components

Retrieve a list of Components. Performs full text search filter.
```python
    components = session.components.search("crypto")
```

#### tag components

Create a tag for the component
```python
    tag = session.components.create_tags(id="be2e8441-b188-483a-be4a-c040e8c665d2")
```

#### untag components

Delete tags for the component
```python
    session.components.delete_tags(id="be2e8441-b188-483a-be4a-c040e8c665d2")
```

### Response

This section describes how to work with responses. See [operations section](#session-operations) to learn how to get these responses.

#### Single response
This response is typically retrieved from the [retrieve](#retrieve) or [status](#status) operations and you receive only one item of desired resource in the response.

Retrieved data are encapsulated in respective model of the retrieved resource which is built on the bindings side.

```python
single_response = session.components.retrieve_list(
    purl="pkg:upstream/github.com/cryostatio/private-cryostat-operator@b63e22b47b0ba47759f6d4a15bbbd11be031da83?version=b63e22b47b0ba47759f6d4a15bbbd11be031da83")
```

You can access all the model fields as attributes.

```python
single_response.results[0].uuid
# "4a41bafd-43e9-4255-b5cc-a554af8dbb0c"
```

alternately you can retrieve directly by uuid

```python
single_response = session.components.retrieve(
    id="4a41bafd-43e9-4255-b5cc-a554af8dbb0c"
```

Which can then be converted to a dictionary.

```python
single_response_dict = single_response.to_dict()
```

Each paginated response comes also with pagination helpers which allows user to conveniently browse through all the pages without the need to adjust offset or limit. These methods are `.next()`, `.prev()` for basic navigation in both directions and `.iterator` which returns iterable enabling looping through the responses in for loop.
