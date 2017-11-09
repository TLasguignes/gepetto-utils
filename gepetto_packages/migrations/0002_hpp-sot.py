# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-09 15:55
from __future__ import unicode_literals

from django.db import migrations

import requests

GITHUB_API = 'https://api.github.com'
PROJECTS = (
    'Humanoid Path Planner',
    'Stack of Tasks'
)


def add_hpp_sot(apps, schema_editor):
    Project, License, Package, Repo = (apps.get_model('gepetto_packages', model)
                                       for model in ['Project', 'License', 'Package', 'Repo'])
    for project_name in PROJECTS:
        project = Project(name=project_name)
        project.save()
        for data in requests.get(f'{GITHUB_API}/orgs/{project.slug}/repos').json():
            package = Package(name=data['name'], project=project, url=data['homepage'])
            package.save()
            repo = Repo(url=data['html_url'], package=package, default_branch=data['default_branch'],
                        open_issues=data['open_issues'])
            # repo.open_pr = len(requests.get(f'{GITHUB_API}/repos/{project.slug}/{package.slug}/pulls').json())
            repo.save()

class Migration(migrations.Migration):

    dependencies = [
        ('gepetto_packages', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_hpp_sot),
    ]
