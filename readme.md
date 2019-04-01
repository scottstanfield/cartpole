# Steps

1. Accept and configure your [bonsai](https://beta.bons.ai)
2. Install miniconda (or skip of you have anaconda)
3. git clone https://github.com/scottstanfield/bonsai-bootstrap
4. Setup your `bonsai` anaconda environment with this command:

```
	conda env create -f environment.yml
	conda activate bonsai
```

5. Verify the `bonsai` cli works:
```
	bonsai
```

6. Copy your access key to clipboard from here:
https://beta.bons.ai/accounts/settings/key

```
	bonsai configure
```

7. Rename `brains` to `.brains`
