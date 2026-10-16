import itertools


class ProcessManager:

    def __init__(self):
        self.pid_counter = itertools.count(1000)
        self.processes = {}

    def create_process(self, name, app):

        pid = next(self.pid_counter)

        self.processes[pid] = {
            "name": name,
            "app": app
        }

        return pid

    def kill_process(self, pid):

        if pid not in self.processes:
            return False

        proc = self.processes[pid]

        try:
            proc["app"].close()
        except Exception:
            pass

        del self.processes[pid]
        return True