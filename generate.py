#! /usr/bin/env python3
from jinja2 import Template
import os

VERSION = "0.0.1"

# Default Files
TEMPLATE = "Dockerfile.j2"
OUTPUT = "Dockerfile"

# Setting Context
PG_VERSION = "11-alpine"

def main():
    context = {
        'version': VERSION,
        'pg_version': PG_VERSION,
        'pg_database': os.environ.get("PGDATABASE", "sysdb"),
        'pg_user': os.environ.get("PGUSER", "pguser"),
        'pg_password': os.environ.get("PGPASSWORD", "password")
    }

    with open(TEMPLATE, 'r') as obj:
        template = Template(obj.read())

        with open(OUTPUT, 'w') as wobj:
            wobj.write(template.render(context))

if __name__ == "__main__":
    main()
