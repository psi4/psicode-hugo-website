import json
import yaml

## Inputs
#  * `data/installs/{edition}.yaml` for branch info
#  * `installers_built` dict below (should be defined for all != brn)
#  * `psi4rt` dict below
#  * customize further restrictions on py versions wrt manager/os/branch in logic below

edition = "v14"

# remember, WSL = Linux
cycle_12 = [
    ("linux", "py2.7"),
    ("linux", "py3.5"),
    ("linux", "py3.6"),
    ("macos", "py2.7"),
    ("macos", "py3.5"),
    ("macos", "py3.6"),
    ("windows wsl", "py2.7"),
    ("windows wsl", "py3.5"),
    ("windows wsl", "py3.6"),
]
cycle_13 = [
    ("linux", "py3.6"),
    ("linux", "py3.7"),
    ("macos", "py3.6"),
    ("macos", "py3.7"),
    ("windows wsl", "py3.6"),
    ("windows wsl", "py3.7"),
]
cycle_14 = [
    ("linux", "py3.6"),
    ("linux", "py3.7"),
    ("linux", "py3.8"),
    ("linux", "py3.9"),
    ("macos", "py3.6"),
    ("macos", "py3.7"),
    ("macos", "py3.8"),
    ("macos", "py3.9"),
    ("windows wsl", "py3.6"),
    ("windows wsl", "py3.7"),
    ("windows wsl", "py3.8"),
    ("windows wsl", "py3.9"),
    ("windows native", "py3.8"),
]
cycle_15 = [
    ("linux", "py3.7"),
    ("linux", "py3.8"),
    ("linux", "py3.9"),
    ("macos", "py3.7"),
    ("macos", "py3.8"),
    ("macos", "py3.9"),
    ("windows wsl", "py3.7"),
    ("windows wsl", "py3.8"),
    ("windows wsl", "py3.9"),
    ("windows native", "py3.8"),
]

installers_built = {
    "1.2.1": cycle_12,
    "1.3rc2": cycle_13,
    "1.3": cycle_13,
    "1.3.1": cycle_13,
    "1.3.2": cycle_13,
    "1.4rc1": cycle_14,
    "1.4rc2": cycle_14,
    "1.4rc3": cycle_14,
    "1.4": cycle_14,
    False: [],
    "1.5dev": cycle_15,
}

psi4rt = {
    "1.2.1": "1.2",
    "1.3": "1.3",
    "1.3.1": "1.3.1",
    "1.3.2": "1.3.2",
    "1.4rc1": "1.4.dev30",
    "1.4rc2": "1.4.dev33",
    "1.4rc3": "1.4.dev35",
    "1.4": "1.4",
}

## Outputs
#  * `data/installs/cmd/{edition}.json`
#  * `data/installs/dlbtn/{edition}.json`

with open(f"../data/installs/{edition}.yaml") as fp:
    ydict = yaml.load(fp, Loader=yaml.FullLoader)

for br in ydict["menu"]:
    if br["datakey"] == "branch":
        branches = br["cells"]
    if br["datakey"] == "python":
        pythons = br["cells"]
    if br["datakey"] == "os":
        oses = br["cells"]
    if br["datakey"] == "pm":
        managers = br["cells"]

brs = [i["jscode"] for i in branches]
brchnls = {i["jscode"]: i["channel"] for i in branches}
brhashs = {i["jscode"]: i["hash"] for i in branches}
brvvs = {i["jscode"]: i["tag"] for i in branches}

pys = [i["jscode"] for i in pythons]

oss = [i["jscode"] for i in oses]
osp4cs = {i["jscode"]: i["psi4conda"] for i in oses}
osexts = {i["jscode"]: i["psi4condaext"] for i in oses}
oscplrs = {i["jscode"]: i["condacompiler"] for i in oses}
osbashs = {i["jscode"]: i["bashrc"] for i in oses}
ostitles = {i["jscode"]: i["title"] for i in oses}
oschnls = {i["jscode"]: i["channel"] for i in oses}

pms = [i["jscode"] for i in managers]


def psi4conda_filename(os, py, pm, br):
    vergil = "http://vergil.chemistry.gatech.edu/psicode-download/"
    psi4conda = f"Psi4conda-{brvvs[br]}-{py.replace('.', '')}-{osp4cs[os]}-x86_64.{osexts[os]}"
    return vergil, psi4conda


def compute_command(os, py, pm, br):
    pyvv = py.replace("py", "")
    brvv = brvvs[br]

    vergil, psi4conda = psi4conda_filename(os, py, pm, br)

    if pm == "installer":
        if br == "brn":
            return """'# installers provided only for release versions'"""
        else:
            if (os, py) in installers_built[brvv]:
                if os == "windows native":
                    return rf"""'# download via button above' +
                             '<br /># install via GUI by double-clicking downloaded `.exe` file analogous to https://conda.io/projects/conda/en/latest/user-guide/install/windows.html' +
                             '<br /># -OR- install via following line' +
                             brprompt + 'start /wait "" {psi4conda} /InstallationType=JustMe /RegisterPython=0 /S /D=%UserProfile%\\psi4conda' +
                             brprompt + 'psi4 --test'"""
                else:
                    return rf"""'# download via button above  -OR-  following line' +
                             brprompt + 'curl "{vergil}{psi4conda}" -o {psi4conda} --keepalive-time 2' +
                             brprompt + 'bash {psi4conda} -b -p $HOME/psi4conda' +
                             bash + 'echo $\'. $HOME/psi4conda/etc/profile.d/conda.sh\\nconda activate\' >> ~/.{osbashs[os]}' +
                             tcsh + 'echo "source $HOME/psi4conda/etc/profile.d/conda.csh\\nconda activate" >> ~/.tcshrc' +
                             '<br /># log out, log back in so conda and psi4 in path' +
                             brprompt + 'psi4 --test'"""
            else:
                return """'# installers not provided for this python version'"""

    elif pm == "conda":
        if (os, py) not in installers_built[brvv]:
            return """'# conda packages not provided for this python version'"""
        elif (br == "brs" and "rc" not in edition) or br == "brn":
            return f"""pprompt + 'conda install psi4 python={pyvv} {brchnls[br]} {oschnls[os]}'"""
        else:
            extras = ""
            if os == "windows native" and brvv in ["1.4rc3"]:
                brvv = "1.4rc4.dev1"
            # if os in ['linux', 'windows wsl'] and brvv == '1.2.1':
            #    extras = ' libint=1.2.1=h87b9b30_4'
            return f"""pprompt + 'conda install psi4={brvv}{extras} python={pyvv} {brchnls[br]} {oschnls[os]}'"""

    elif pm == "source":
        if (os, py) not in installers_built[brvv]:
            if os == "windows native" and ("linux", py) in installers_built[brvv] and brvv != "1.3.2":
                pass
            else:
                return """'# source code does not support this python version'"""

        if br == "brn":
            checkout = ""
        else:
            checkout = f""" && git checkout {brhashs[br]}"""

        if os == "windows native":
            return rf"""pprompt + 'git clone https://github.com/psi4/psi4.git && cd psi4{checkout}' +
                    '<br /># see https://github.com/psi4/psi4/blob/master/.azure-pipelines/azure-pipelines-windows.yml to set up a build environment'"""
        else:
            return rf"""pprompt + 'git clone https://github.com/psi4/psi4.git && cd psi4{checkout}' +
                    brprompt + 'conda create -n p4dev psi4-dev python={pyvv} {brchnls[br]} {oschnls[os]}' +
                    brprompt + 'conda activate p4dev' +
                    brprompt + '`psi4-path-advisor --{oscplrs[os]}`' +
                    brprompt + 'cd objdir && make -j`getconf _NPROCESSORS_ONLN`'"""


def compute_download_button(os, py, pm, br):
    brvv = brvvs[br]

    vergil, psi4conda = psi4conda_filename(os, py, pm, br)

    if pm == "installer" and br != "brn" and ((os, py) in installers_built[brvv]):
        return rf"""['<i class="fa fa-download" aria-hidden="true"></i> download psi4conda installer',
                         '{vergil}{psi4conda}',
                         '{psi4conda}',
                         '/images/installs/conda_ovals.{pm}.jpeg']"""

    else:
        return rf"""['<i class="fa fa-link" aria-hidden="true"></i> goto miniconda installers',
                     'https://conda.io/miniconda.html',
                     '#',
                     '/images/installs/conda_ovals.{pm}.jpeg']"""


cmddict = {}
dlbtndict = {}
for os in oss:
    for py in pys:
        for pm in pms:
            for br in brs:
                key = ",".join([pm, ostitles[os].lower(), py, br])

                ans = compute_command(os, py, pm, br)
                if ans is not None:
                    cmddict[key] = ans

                ans = compute_download_button(os, py, pm, br)
                if ans is not None:
                    dlbtndict[key] = ans

with open(f"../data/installs/cmd/{edition}.json", "w") as fp:
    json.dump(cmddict, fp, indent=4, sort_keys=True)

with open(f"../data/installs/dlbtn/{edition}.json", "w") as fp:
    json.dump(dlbtndict, fp, indent=4, sort_keys=True)
