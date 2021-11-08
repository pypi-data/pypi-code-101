from . import xpd, xnp, xplt


def x_monkey_patch():
    xpd.monkey_patch()
    xnp.monkey_patch()
    xplt.monkey_patch()

