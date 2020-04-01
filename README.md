# Video Production

Tooling, info and more about how Hack Quarantine gets it's videos out.

## Editing

Currently, [Olive](https://www.olivevideoeditor.org/) is being used to edit our
videos, along with Audacity to clean up the audio.


## Scripts

* crop.sh - script based around `ffmpeg`  to quickly crop our footage from the
raw stream footage.

* templateTool - script to automate creation of Olive projects for me, including
the title cards.

* make.sh - an older tool being used earlier on. Basically, this would take
source footage and prepend our intro / closing video. Dropped as source footage
needed more editing / audio improvements.

* get.sh - I get given links to all the assets in s3, which include access keys 
as part of the query string. wget'ing them gives me awkward filenames so i wrote
this.
