#!/usr/bin/env python3
import sys
import os
from title import TitleCard
from oliveProject import OliveProject
from projectName import projectName

baseDir = os.getcwd()
olive_template = '{}/templates/olive_template.ove'.format(baseDir)

tc = TitleCard()

title = sys.argv[1]
author = sys.argv[2]

card_name = '{}/{}'.format(
    '{}/assets/titles'.format(baseDir),
    projectName(title, author, ff='png')
)

# Create the title card
tc.generate(title, author).save(
    card_name
)

# Make the Olive project
op = OliveProject()
op.open(olive_template)

title_card = None

for footage in op.media():
    # find the title card
    if footage.props['name'] == 'title_card':
        footage.props['url'] = card_name
        if not op.update_media(footage):
            raise

op.write(projectName(
    title,
    author,
    ff='ove'
), 'Project_files')

print('[!] Project generated!')
