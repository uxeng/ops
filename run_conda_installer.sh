#!/usr/bin/env bash
#
./run_disable_ipv6.sh
#
CONTEXT="uxeng"
if [[ -z "${DATA_DIR}" ]]; then
  export DATA_DIR="/data"
fi


if [[ -z "${DEPLOY_VER}" ]]; then
  export DEPLOY_VER="default/$CONTEXT"
else
  export DEPLOY_VER=$DEPLOY_VER/$CONTEXT
fi
DEPLOY_VER_CONDA=$DEPLOY_VER


#
echo "DATA_DIR: $DATA_DIR"
echo "DEPLOY_VER: $DEPLOY_VER"
mkdir -p $DEPLOY_VER


DADIF_PATHS=""
export PATH="$DADIF_PATHS":$PATH
echo "PATH: $PATH"

## Conda
CONDA_CHECK_CMD="conda"
CONDA_CMD_DESCRIPTION=$CONDA_CHECK_CMD
export CONDA_INSTALLER_NAME="Miniforge3-Linux-x86_64.sh"
export CONDA_INSTALLER_URL="https://github.com/conda-forge/miniforge/releases/latest/download/$CONDA_INSTALLER_NAME"
DADIF_TMP_DIR="$DATA_DIR/$DEPLOY_VER/DEPLOYER"
MINICONDA_NAME=miniconda
MINICONDA_PATH=$DATA_DIR/$DEPLOY_VER_CONDA/$MINICONDA_NAME/
PATH=$MINICONDA_PATH/bin:$PATH
CONDA_ENV="uxeng"
CONDA_ENV_HOME=$(pwd)/apps/$CONDA_ENV
CONDA_HOME="$DATA_DIR/$DEPLOY_VER_CONDA/miniconda"

#
CONDA_ENVIRONMENT_FILE_NAME="conda_environment_$CONDA_ENV.sh"
source $DATA_DIR/$DEPLOY_VER/$CONDA_ENVIRONMENT_FILE_NAME
#

echo "CONDA ENV HOME: $CONDA_ENV_HOME"
echo "DADIF TMP Dir: $DADIF_TMP_DIR"
if ! command -v $CONDA_CHECK_CMD &> /dev/null
then
    echo "Current dir:"
    echo "$CONDA_CMD_DESCRIPTION could not be found. Going to Install it"
    mkdir -p $DADIF_TMP_DIR
    echo "Working Dir to download conda:"
    cd $DADIF_TMP_DIR
    pwd
    echo "Downloading conda from: $CONDA_INSTALLER_URL"
    curl -L -O --url $CONDA_INSTALLER_URL
    chmod +x $DADIF_TMP_DIR/*.sh
    echo "Going to install CONDA in: $CONDA_HOME"
    ./$CONDA_INSTALLER_NAME -b -p $CONDA_HOME 
fi

conda list --name $CONDA_ENV
UXENG_CONDA_ENV_EXIST=$?
echo "UXENG_CONDA_ENV_EXIST? $BACKSTAGE_CONDA_ENV_EXIST"
if [ "$UXENG_CONDA_CONDA_ENV_EXIST" -eq "0" ]; then
   echo "CONDA ENV $CONDA_ENV exist";
   exit;
fi

conda env
echo "Updating Conda"
conda config --set default_threads 4
conda update -n base -c conda-forge conda -y
echo "Installing Mamba Solver"
conda install -n base conda-libmamba-solver -y
echo "Setting Solver to libmama"
conda config --set solver libmamba

cd $CONDA_ENV_HOME
echo "Current Dir:"
pwd
conda env create -f $CONDA_ENV_HOME/environment.yml

eval "$(conda shell.bash hook)"
conda env list
conda install -y conda-build
conda activate $CONDA_ENV
conda develop $CONDA_ENV_HOME
conda info


echo "#!/usr/bin/env bash" > $CONDA_ENVIRONMENT_FILE_NAME
echo "export PATH=$PATH" >> $CONDA_ENVIRONMENT_FILE_NAME
echo "source $CONDA_HOME/etc/profile.d/conda.sh" >> $CONDA_ENVIRONMENT_FILE_NAME
chmod +x $CONDA_ENVIRONMENT_FILE_NAME
eval "$(conda shell.bash hook)"
conda activate $CONDA_ENV

CONDA_ENVIRONMENT_FILE_NAME="conda_environment_$CONDA_ENV.sh"
echo "#!/usr/bin/env bash" > $CONDA_ENVIRONMENT_FILE_NAME
echo "export PATH=$PATH" >> $CONDA_ENVIRONMENT_FILE_NAME
echo "source $CONDA_HOME/etc/profile.d/conda.sh"  >> $CONDA_ENVIRONMENT_FILE_NAME
##
cd /home/uxeng/dev/

apt-get install git -y
# Ignores
echo "src/app.egg-info/" >> .gitignore
echo "__pycache__/" >> .gitignore
echo "dist/" >> .gitignore

git config --global --add safe.directory /home/uxeng/dev
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
git init
git add .
git commit -m 'Updated'
sleep infinity