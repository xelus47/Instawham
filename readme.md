# Instawham

An informal Instagram API

## Installation

```bash
 $ git clone github.com/xelus47/Instawham
 $ cd Instawham
 Instawham/ $ source source.sh
```

## Usage
TBA

## Explanation

### General

| page type | url | example |
| --------- | --- | ------- | 
| home | `/` | www.instagram.com |
| user | `/[username]/` | www.instagram.com/istaypuffed/ |
| post | `/p/[short_code]/`| www.instagram.com/p/BV0Jn0nFWpX/ |
| hashtag | `/explore/tags/[hashtag]/`| www.instagram.com/explore/tags/drugs/ |
| location | `/explore/locations/[id]/([location]/)`| www.instagram.com/explore/locations/44961364/ |

NB: location name may be omitted:
`/explore/locations/44961364/` is resolved by instagram.com as `/explore/locations/44961364/san-francisco-california/`

### ?__a=1
TBA

### Graphql

When you click "load more [x]", the site makes a GET request to `/graphql/query/`.
The url takes a query string and returns a nice JSON file.

#### Query string

Required:

| parameter  | variable type | usage |
| ---------- | ------------- | ----- |
| query_id   | `int`         | Requesting the appropriate page type (location, hashtag, etc) |
| [category] | varied        | Pointing to the specific node                                 | 
| first      | `int`         | I only want to see the first `n` entries for this query       |

Optional:

| Parameter | variable type | usage |
| ----------| ------------- | ---- |
| after     | varied, usually `str`| Only show entries behind this entry (varies per category of course) |

#### Page types and query IDs

| page type  | query parameter| variable type | json                    | query_id |
| ---------- | ---------------| ------------- | ----------------------- | -------- |
| user       | `id=`          | `int`         | `{ "data": { "user"`     | 17880160963012870 |
| location   | `id=`          | `int`         | `{ "data": { "location"`| 17881432870018455 |
| hashtag    | `tag_name=`    | `str`         | `{ "data": { "hashtag"` | 17882293912014529 |
| comments   | `shortcode=`   | `str`         | `{ "data": { "shortcode_media"`| 17852405266163336 |


# Update
Query IDs seem to update. The current `query_id` for user queries is 17859156310193001.
