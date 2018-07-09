# learn-machine-learning

learn machine-learning, exercise

## first install

```bash
# install tensorflow for mac
pip install --ignore-installed --upgrade "https://raw.githubusercontent.com/lakshayg/tensorflow-build/master/tensorflow-1.8.0-cp36-cp36m-macosx_10_7_x86_64.whl"

# for https://colab.research.google.com/
pip install jupyter_http_over_ws
jupyter serverextension enable --py jupyter_http_over_ws
```

## start local server for <https://colab.research.google.com>

```bash
jupyter notebook \
  --NotebookApp.allow_origin='https://colab.research.google.com' \
  --port=8888
```
