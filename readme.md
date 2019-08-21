# Install Bonsai CLI + Anaconda on Linux

### 1. Install Miniconda 

Miniconda just installs the core scripts, and pulls down the necessary
packages when requested. The full Anaconda [downloads all packages][1] and
consumes ~3 GB.

Note: https://aka.ms/miniconda.sh redirects to
https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh.
The shortened name here is easier to type.

```bash
cd ~
wget aka.ms/miniconda.sh
sh miniconda.sh -b
rm miniconda.sh
```

### 2. Clone Limited Preview starter 

Repository: https://github.com/scottstanfield/bonsai-bootstrap

```bash
git clone https://github.com/scottstanfield/bonsai-bootstrap
```

### 3. Create the bonsai Anaconda environment

```bash
cd ~/bonsai-bootstrap
conda env create -f environment.yml
conda activate bonsai
```

### 4. Temporary steps for Azure AD integration

This section will be obsolete will change on **Wed, Aug 21, 2019**.

a) Create a stub `~/.bonsai` that points to the right cloud

```bash
cat >> ~/.bonsai <<EOD
[DEFAULT]
url=https://mumouarm-api.azdev.bons.ai
EOD
```

b) Start the one-time AAD authentication

```bash
bonsai -a configure
```

Note: if you've authenticated before, there's a chance the CLI will ask
you to got to http://mumouarm-api.azdev.bons.ai/accounts/settings/key
resulting in a 404 error. Go to step c).

c) Generate new key from https://web-master.azdev.bons.ai/?cloud=mumouarm

Note: when you paste the key into the client, it won't echo the
characters to the screen. But you still need to hit enter after pasting.

d) Verify:

```bash
bonsai list
```

# Cartpole instructions


```bash
conda activate bonsai
cd cartpole
bonsai create cart-0820-2
bonsai push
bonsai train start
python hub.py --render
bonsai train stop
```


[1]: http://deeplearning.lipingyang.org/2018/12/23/anaconda-vs-miniconda-vs-virtualenv/
