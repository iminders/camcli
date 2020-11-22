set -e
cd "$(dirname "$0")"
echo `pwd`

pip install -e .
cd camcli && python3 -m pytest
