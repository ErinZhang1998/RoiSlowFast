from config import load_cfg
from slowfast.models import SlowFast

cfg = load_cfg(CONFIG_FILENAME)
model = SlowFast(cfg)