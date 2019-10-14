# wordpress scraper

Basic python script to login to wordpress & GET a page.

## Usage
- Create `conf.json` in this format: (See `conf.json.example`)
- ```json
  {
      "username": "user1",
      "password": "BlahbLahblAh123",
      "url": "https://my-wp-site.com",
      "redir": "https://my-wp-site.com/wp-admin/"
  }
  ```
- Run `main.py`
  - `python3 main.py`
- Done

## License
MIT &copy; 2019 Sebastian Safari
