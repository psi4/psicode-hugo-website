import json
import yaml

## Inputs
#  * `data/installs/{edition}.yaml` for branch info
#  * menu arrays below (should match menu in file above)
#  * installers_built dict below (should be defined for all != brn)

edition = 'v131'

pms = ['installer', 'conda', 'source']
oss = ['linux', 'macos', 'windows wsl']
pys = ['py2.7', 'py3.5', 'py3.6', 'py3.7']
brs = ['brp', 'brs', 'brn']

installers_built = {
    '1.2.1': ['py2.7', 'py3.5', 'py3.6'],
    '1.3rc2': ['py3.6', 'py3.7'],
    '1.3': ['py3.6', 'py3.7'],
    '1.3.1': ['py3.6', 'py3.7'],
    False: [],
}

psi4rt = {
    '1.2.1': '1.2',
    '1.3': '1.3',
    '1.3.1': '1.3.1',
}

## Outputs
#  * `data/installs/cmd/{edition}.json`
#  * `data/installs/dlbtn/{edition}.json`

with open(f'../data/installs/{edition}.yaml') as fp:
    ydict = yaml.load(fp)

for br in ydict['menu']:
    if br['datakey'] == 'branch':
        branches = br['cells']
brchnls = {br['jscode']: br['channel'] for br in branches}
brhashs = {br['jscode']: br['hash'] for br in branches}
brvvs = {br['jscode']: br['tag'] for br in branches}

osp4cs = {'linux': 'Linux', 'macos': 'MacOSX', 'windows wsl': 'WindowsWSL'}
oscplrs = {'linux': 'gcc', 'macos': 'clang', 'windows wsl': 'gcc'}
osbashs = {'linux': 'bashrc', 'macos': 'bash_profile', 'windows wsl': 'bashrc'}


def compute_command(os, py, pm, br):
    osp4c = osp4cs[os]
    oscplr = oscplrs[os]
    osbash = osbashs[os]

    pynn = py.replace('.', '')
    pyvv = py.replace('py', '')

    brchnl = brchnls[br]
    brhash = brhashs[br]
    brvv = brvvs[br]

    if py in ['py2.7', 'py3.5'] and br != 'brp':
        return """'# old python not supported after v1.2.1'"""

    if pm == 'installer':
        if br == 'brn':
            return """'# installers provided only for release versions'"""
        else:
            if py in installers_built[brvv]:
                return rf"""'# download via button above  -OR-  following line' +
                          brprompt + 'curl "http://vergil.chemistry.gatech.edu/psicode-download/Psi4conda-{brvv}-{pynn}-{osp4c}-x86_64.sh" -o Psi4conda-{brvv}-{pynn}-{osp4c}-x86_64.sh --keepalive-time 2' +
                          brprompt + 'bash Psi4conda-{brvv}-{pynn}-{osp4c}-x86_64.sh -b -p $HOME/psi4conda' +
                          bash + 'echo $\'. $HOME/psi4conda/etc/profile.d/conda.sh\\nconda activate\' >> ~/.{osbash}' +
                          tcsh + 'echo "source $HOME/psi4conda/etc/profile.d/conda.csh\\nconda activate" >> ~/.tcshrc' +
                          '<br /># log out, log back in so conda and psi4 in path' +
                          brprompt + 'psi4 --test'"""
            else:
                return """'# installers not provided for this python version'"""

    elif pm == 'conda':
        if (br == 'brs' and 'rc' not in edition) or br == 'brn':
            return f"""pprompt + 'conda install psi4 psi4-rt python={pyvv} {brchnl}'"""
        else:
            extras = ''
            #if os in ['linux', 'windows wsl'] and brvv == '1.2.1':
            #    extras = ' libint=1.2.1=h87b9b30_4'
            return f"""pprompt + 'conda install psi4={brvv} psi4-rt={psi4rt[brvv]}{extras} python={pyvv} {brchnl}'"""

    elif pm == 'source':
        if br == 'brn':
            checkout = ''
        else:
            checkout = f""" && git checkout {brhash}"""

        return rf"""pprompt + 'git clone https://github.com/psi4/psi4.git && cd psi4{checkout}' +
                      brprompt + 'conda create -n p4dev psi4-dev python={pyvv} {brchnl}' +
                      brprompt + 'conda activate p4dev' +
                      brprompt + '`psi4-path-advisor --{oscplr}`' +
                      brprompt + 'cd objdir && make -j`getconf _NPROCESSORS_ONLN`'"""


def compute_download_button(os, py, pm, br):
    osp4c = osp4cs[os]
    pynn = py.replace('.', '')
    brvv = brvvs[br]

    if pm == 'installer' and br != 'brn' and (py in installers_built[brvv]):
            return rf"""['<i class="fa fa-download" aria-hidden="true"></i> download psi4conda installer',
                         'http://vergil.chemistry.gatech.edu/psicode-download/Psi4conda-{brvv}-{pynn}-{osp4c}-x86_64.sh',
                         'Psi4conda-{brvv}-{pynn}-{osp4c}-x86_64.sh',
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
                key = ','.join([pm, os, py, br])

                ans = compute_command(os, py, pm, br)
                if ans is not None:
                    cmddict[key] = ans

                ans = compute_download_button(os, py, pm, br)
                if ans is not None:
                    dlbtndict[key] = ans

#with open(f'{edition}-cmd.dat', 'w') as fp:
#    for k, v in cmddict.items():
#        fp.write(f"""        '{k}': {v},\n\n""")

with open(f'../data/installs/cmd/{edition}.json', 'w') as fp:
    json.dump(cmddict, fp, indent=4, sort_keys=True)

with open(f'../data/installs/dlbtn/{edition}.json', 'w') as fp:
    json.dump(dlbtndict, fp, indent=4, sort_keys=True)
