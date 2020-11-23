# psicode-hugo-website [![Netlify Status](https://api.netlify.com/api/v1/badges/d7f8026f-8c6b-41a8-b266-747fd04a8804/deploy-status)](https://app.netlify.com/sites/admiring-tesla-08529a/deploys)

This is the home of the new psicode website generated with Hugo. Committers to psi4/psi4 have push access (at least that was my intention). There's nice build check and preview capabilites upon pull request, so contributions through PR preferred.

## getting started

##### get Hugo

* download and extract tarball from https://github.com/gohugoio/hugo/releases . add `hugo` command to `PATH` envvar
* works for Linux: `wget https://github.com/gohugoio/hugo/releases/download/v0.54.0/hugo_0.54.0_Linux-64bit.tar.gz`

##### get website

* Fork this repo, then clone it locally
* `git clone --recursive https://github.com/<USERNAME>/psicode-hugo-website.git`
* `git remote add upstream https://github.com/psi4/psicode-hugo-website.git`

##### get theme

**Skip unless `--recursive` above doesn't work.**

* need to get GH:loriab/meghna-hugo at branch `bootstrap4`. It's a submodule, so it'll handle itself with thte `recursive` above. If not, below is the approximate directions

* `cd psicode-hugo-website/themes/`
* `git submodule add https://github.com/loriab/meghna-hugo.git`
* `git checkout bootstrap4`

##### start the site building locally

* in another terminal window, `cd psicode-hugo-website`
* `hugo server -D`
* if OSX balks on the many static docs with `socket: too many open files in system`, try *http://blog.mact.me/2014/10/22/yosemite-upgrade-changes-open-file-limit
* view in browser at http://localhost:1313/
* updates automatically when save files (refresh browser if it gets stuck on the little square)

##### deploy the website

* push to a branch on your fork, submit a PR, and netlify will build a preview. Once merged to `master` of this repo, `https://app.netlify.com/sites/admiring-tesla-08529a/deploys` will go to work. Should be up in a couple minutes.
* users with write access to this repo are free to merge their own PRs. otherwise, request a review.
