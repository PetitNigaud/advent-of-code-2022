echo "convert ${FNAME}.ipynb to ${FNAME}.py"
jupyter nbconvert "${FNAME}.ipynb" --to script
echo "excuting ${FNAME}.py with pypy "
echo ""
pypy "${FNAME}.py"