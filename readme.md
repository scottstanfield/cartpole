# Steps for Linux

1. Install miniconda

```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O mini.sh
sh mini.sh
```

2. Clone this repo https://github.com/scottstanfield/bonsai-bootstrap
```
cd ~
git clone https://github.com/scottstanfield/bonsai-bootstrap
```

3. Setup your `bonsai` Anaconda/Python environment with this command:

```
	cd ~/bonsai-bootstrap
	conda env create -f environment.yml
	conda activate bonsai
```

> temporary steps for Azure AD integration

a) Create a stub ~/.bonsai that points to the right cloud
```
cat > ~/.bonsai <<EOD
[DEFAULT]
url=https://mumouarm-api.azdev.bons.ai
EOD
```

b) tie client with AAD
```
bonsai -a configure
```

c) generate new key from https://web-master.azdev.bons.ai/?cloud=mumouarm

d) verify:
```
bonsai list
```


7. Rename `brains` to `.brains`
