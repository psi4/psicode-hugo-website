# hugosite

This is the temporary home to the new psicode website generated with Hugo. I propose that the Git model here be everyone push with full privleges. Contact Lori for collaborator access.

## getting started

##### get Hugo

* download and extract tarball from https://github.com/gohugoio/hugo/releases . add `hugo` command to `PATH` envvar
* works for Linux: `wget https://github.com/gohugoio/hugo/releases/download/v0.54.0/hugo_0.54.0_Linux-64bit.tar.gz`

##### get website

* `git clone https://github.com/loriab/hugosite.git`

##### get theme

* `cd hugosite/quickstart/themes/`
* `git clone https://github.com/loriab/meghna-hugo.git`

##### start the site building locally

* in another terminal window, `cd hugosite/quickstart/`
* `hugo server -D`
* view in browser at http://localhost:1313/
* updates automatically when save files (refresh browser if it gets stuck on the little square)
