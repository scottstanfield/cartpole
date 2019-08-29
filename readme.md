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


# Cartpole Sample A pole is attached by an un-actuated joint to a cart,

which moves along a frictionless track. The system is controlled by
applying a force of +1 or -1 to the cart. The pendulum starts upright,
and the goal is to prevent it from falling over. A reward of +1 is
provided for every timestep that the pole remains upright. The episode
ends when the pole is more than 15 degrees from vertical, or the cart
moves more than 2.4 units from the center.

## WEB GUIDE If you're using the web interface, please follow the [quick
start guide](http://docs.bons.ai/guides/getting-started.html).

## LOCAL (CLI) GUIDE

### CLI INSTALLATION
1. Install the Bonsai CLI by following our [detailed CLI installation
   guide](http://docs.bons.ai/guides/cli-guide.html).

### CREATE YOUR BRAIN
1. Setup your BRAIN's local project folder.  `bonsai create
   <your_brain>`
2. Run this command to install additional requirements for training your
   BRAIN.  `pip install -r requirements.txt`

### HOW TO TRAIN YOUR BRAIN
1. Upload Inkling and simulation files to the Bonsai server with one
   command.  `bonsai push`
2. Run this command to start training mode for your BRAIN.  `bonsai
   train start`
3. Connect the simulator for training. Use the `--render` option to
   render the cartpole.  `python sim.py --brain=<your_brain> --render`
4. When training has hit a sufficient accuracy for prediction, about 250
   for at least 100 episodes, stop training your BRAIN.  `bonsai train
	stop`

### GET PREDICTIONS
1. Run the simulator using predictions from your BRAIN. You can now see
   AI playing the game!  `python hub.py --brain=<your_brain>
   --predict=<brain_version>`


## Questions about Inkling?  See our [Inkling
Guide](http://docs.bons.ai/guides/inkling-guide.html) and [Inkling
Reference](http://docs.bons.ai/references/inkling-reference.html) for
help.
