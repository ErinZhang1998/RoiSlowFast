## How to load config

Follow `https://github.com/facebookresearch/SlowFast/blob/master/INSTALL.md` to install PySlowFast

```python
from config import load_cfg
from slowfast.models import SlowFast

cfg = load_cfg(CONFIG_FILENAME)
model = SlowFast(cfg)
```
