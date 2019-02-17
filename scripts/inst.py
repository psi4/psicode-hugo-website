import json

release = '406f4de'

pms = ['installer', 'conda', 'source']
oss = ['linux', 'macos', 'windows wsl']
pys = ['py2.7', 'py3.5', 'py3.6']
brs = ['brs', 'brn']


cmddict = {}

for os in oss:
    osp4c = {'linux': 'Linux', 'macos': 'MacOSX', 'windows wsl': 'WindowsWSL'}[os]
    oscplr = {'linux': 'gcc', 'macos': 'clang', 'windows wsl': 'gcc'}[os]
    osbash = {'linux': 'bashrc', 'macos': 'bash_profile', 'windows wsl': 'bashrc'}[os]

    for py in pys:
        pynn = py.replace('.', '')
        pyvv = py.replace('py', '')

        for pm in pms:

            for br in brs:
                # NOTE brs changes btwn dev and psi4 channels
                #brchnl = {'brp': '-c psi4', 'brs': '-c psi4/label/dev', 'brn': '-c psi4/label/dev'}[br]
                brchnl = {'brp': '-c psi4', 'brs': '-c psi4', 'brn': '-c psi4/label/dev'}[br]

                key = ','.join([pm, os, py, br])
                val = 'Report empty value!'

                if pm == 'installer':
                    if br == 'brn':
                        val = """'# installers provided only for release versions'"""
                    else:
                        val = rf"""'# download via button above  -OR-  following line' +
                                  brprompt + 'curl "http://vergil.chemistry.gatech.edu/psicode-download/psi4conda-' + installerrelease + '-{pynn}-{osp4c}-x86_64.sh" -o Psi4conda-latest-{pynn}-{osp4c}-x86_64.sh --keepalive-time 2' +
                                  brprompt + 'bash Psi4conda-latest-{pynn}-{osp4c}-x86_64.sh -b -p $HOME/psi4conda' +
                                  bash + 'echo $\'. $HOME/psi4conda/etc/profile.d/conda.sh\\nconda activate\' >> ~/.{osbash}' +
                                  tcsh + 'echo "source $HOME/psi4conda/etc/profile.d/conda.csh\\nconda activate" >> ~/.tcshrc' +
                                  '<br /># log out, log back in so conda and psi4 in path' +
                                  brprompt + 'psi4 --test'"""

                elif pm == 'conda':
                    val = f"""pprompt + 'conda install psi4 psi4-rt python={pyvv} {brchnl}'"""

                elif pm == 'source':
                    if br == 'brn':
                        checkout = """'"""
                    else:
                        #checkout = f""" && git checkout ' + checkout {release}"""
                        checkout = """ && git checkout ' + checkoutrelease"""

                    val = rf"""pprompt + 'git clone https://github.com/psi4/psi4.git && cd psi4{checkout} +
                                  brprompt + 'conda create -n p4dev psi4-dev python={pyvv} {brchnl}' +
                                  brprompt + 'conda activate p4dev' +
                                  brprompt + '`psi4-path-advisor --{oscplr}`' +
                                  brprompt + 'cd objdir && make -j`getconf _NPROCESSORS_ONLN`'"""

                cmddict[key] = val


with open('cmddict.dat', 'w') as fp:
    for k, v in cmddict.items():
        fp.write(f"""        '{k}': {v},\n\n""")

with open('cmddict.json', 'w') as fp:
    json.dump(cmddict, fp, indent=4, sort_keys=True)
