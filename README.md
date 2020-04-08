# Courtbot
> An information and notification site for court administration

Courtbot is a web application that provides information about court services. 

Courtbot is designed to work alongside existing court administration systems. It is designed not to integrate directly with court databases, but rather to accept data files from those systems (preferably daily) and then present the information to the public.

## Installing / Getting started

```shell
source .venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

You will need to configure a database to run, default is PostgreSQL. Check the Django Documentation for how to configure a database.

### Deploying / Publishing

Eventually, we will let you know how to deploy this.

## Features

This program does something simple that courts have long done poorly: display a court date and provide some guidance to the public and the lawyers about what to do before then.


## Links

Even though this information can be found inside the project on machine-readable
format like in a .json file, it's good to include a summary of most useful
links to humans using your project. You can include links like:

- Project homepage: https://your.github.com/awesome-project/
- Repository: https://github.com/your/awesome-project/
- Issue tracker: https://github.com/your/awesome-project/issues
  - In case of sensitive bugs like security vulnerabilities, please contact
    my@email.com directly instead of using issue tracker. We value your effort
    to improve the security and privacy of this project!
- Related projects:
  - Your other project: https://github.com/your/other-project/
  - Someone else's project: https://github.com/someones/awesome-project/


## Licensing

Courtbot is developed by Franklin Bynum, Judge of Harris County Criminal Court at Law # 8.

(c) 2020 Franklin Bynum, this software is licensed under GNU General Public License v3.