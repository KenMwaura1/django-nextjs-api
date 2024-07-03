
# Django NextJS Api

Backend api for a NextJS app.


## Installation

Install my-project with pip

```bash
  git clone 
  cd django-nextjs-api
  python3 -m venv venv
  pip install -r requirements.txt
  rav migrate
  rav run server
```
    
## License

[MIT](https://choosealicense.com/licenses/mit/)


## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)



## Authors

- [@KenMwaura1](https://www.github.com/KenMwaura1)


## API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.


## Usage/Examples

```python
curl -i -H 'Accept: application/json' http://localhost:8000/api/items

```


## FAQ

#### Question 1

Answer 1

#### Question 2

Answer 2


## Features

- Working with Next JS 
- Auth 
- 


## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.


## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
 pip install -r requirements.txt
```

Make migrations

```bash
  rav migrate
```

Start the server

```bash
  rav run server
```

