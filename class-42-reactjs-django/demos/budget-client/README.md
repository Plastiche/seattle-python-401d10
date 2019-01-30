## Lab Instructions

- in project director run `npm install` then `npm start`
- Search through the code looking for `LAB TASK:` to see the one task for today's lab.
- Ask for help ;)

***Note:*** you'll need a running RESTFUL API from Lab 39 to connect to. Any trouble with that LMK.

If you get back a permissions error when attempting to log in to API then add below to your settings.py

```
CORS_ORIGIN_ALLOW_ALL = True
# CORS_ORIGIN_WHITELIST = tuple(
#     os.environ.get(
#         'CORS_ORIGIN_WHITELIST',
#         'localhost',
#     ).split()
# )
```
