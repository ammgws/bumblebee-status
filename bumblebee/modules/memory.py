import psutil
import bumblebee.module
import bumblebee.util

def usage():
    return "memory"

def notes():
    return "Warning is at 20% available RAM, Critical at 10%."

def description():
    return "Shows available RAM, total amount of RAM and the percentage of available RAM."

class Module(bumblebee.module.Module):
    def __init__(self, output, config, alias):
        super(Module, self).__init__(output, config, alias)
        self._mem = psutil.virtual_memory()

# TODO
#        output.add_callback(module=self.__module__, button=1,
#            cmd="gnome-system-monitor")

    def widgets(self):
        self._mem = psutil.virtual_memory()

        used = self._mem.total - self._mem.available

        return bumblebee.output.Widget(self, "{}/{} ({:05.02f}%)".format(
            bumblebee.util.bytefmt(used),
            bumblebee.util.bytefmt(self._mem.total),
            self._mem.percent)
        )

    def warning(self, widget):
        return self._mem.percent < self._config.parameter("warning", 20)

    def critical(self, widget):
        return self._mem.percent < self._config.parameter("critical", 10)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4