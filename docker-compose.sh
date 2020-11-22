set -e
cd "$(dirname "$0")"
echo `pwd`

cd camcli
python3 -m pytest
