# psicode-hugo-website

This is the temporary home to the new psicode website generated with Hugo. Committers to psi4/psi4 have push access (at least that was my intention). For now, I propose that the Git model be everyone push with full privileges. Contact Lori for collaborator access.

## getting started

##### get Hugo

* download and extract tarball from https://github.com/gohugoio/hugo/releases . add `hugo` command to `PATH` envvar
* works for Linux: `wget https://github.com/gohugoio/hugo/releases/download/v0.54.0/hugo_0.54.0_Linux-64bit.tar.gz`

##### get website

* `git clone --recursive https://github.com/psi4/psicode-hugo-website.git`

##### get theme

* need to get GH:loriab/meghna-hugo at branch `bootstrap4`. It's a submodule, so it'll handle itself with thte `recursive` above. If not, below is the approximate directions

* `cd psicode-hugo-website/themes/`
* `git submodule add https://github.com/loriab/meghna-hugo.git`
* `git checkout bootstrap4`

##### start the site building locally

* in another terminal window, `cd psicode-hugo-website`
* `hugo server -D`
* view in browser at http://localhost:1313/
* updates automatically when save files (refresh browser if it gets stuck on the little square)

##### deploy the website

* push to `master` of this repo and `https://app.netlify.com/sites/admiring-tesla-08529a/deploys` will go to work. Should be up in a couple minutes.
