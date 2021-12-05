#!/bin/sh
heroku pg:push mnd postgresql-round-50139 --app mnd --exclude-table-data=django_admin_log