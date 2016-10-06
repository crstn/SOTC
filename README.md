# Sound of the City

Little data analysis project about the [Discogs](http://discgos.com) database. To run, download and unzip their dumps into the *data* subfolder, e.g. via

    curl http://discogs-data.s3-us-west-2.amazonaws.com/data/discogs_20161001_artists.xml.gz | gunzip -c > artists.xml; curl http://discogs-data.s3-us-west-2.amazonaws.com/data/discogs_20161001_labels.xml.gz | gunzip -c > labels.xml; curl http://discogs-data.s3-us-west-2.amazonaws.com/data/discogs_20161001_masters.xml.gz | gunzip -c > masters.xml; curl http://discogs-data.s3-us-west-2.amazonaws.com/data/discogs_20161001_releases.xml.gz | gunzip -c > releases.xml;

Available tags for different datasets, the tags highlighted could be relevant for this research:

## Labels
- image
- images
- id
- name
- **contactinfo**
- profile
- data_quality
- url
- urls
- label
- sublabels
- parentLabel
- labels
		
## Master releases
- main_release
- image
- images
- id
- name
- anv
- **join** ???
- role
- tracks
- artist
- artists
- **genre**
- **genres**
- **style**  ???
- **styles**  ???
- year
- title
- data_quality
- description
- video
- videos
- master
- notes
- masters

## Releases
- image
- images
- id
- name
- anv
- join
- role
- tracks
- artist
- artists
- title
- label
- labels
- extraartists
- description
- descriptions
- format
- formats
- genre
- genres
- style
- styles
- country
- released
- notes
- data_quality
- position
- duration
- track
- tracklist
- identifier
- identifiers
- video
- videos
- catno
- entity_type
- entity_type_name
- resource_url
- company
- companies
- release
- master_id
- sub_tracks
- releases

## Artists
Maybe not needed at all?
- image
- images
- id
- name
- realname
- profile
- data_quality
- namevariations
- aliases
- artist
- members
- url
- urls
- groups
- artists

