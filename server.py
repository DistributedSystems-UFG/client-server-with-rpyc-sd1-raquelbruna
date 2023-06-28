import rpyc
from constRPYC import *
from rpyc.utils.server import ThreadedServer


class DBList(rpyc.Service):
    value = []

    def exposed_append(self, data):
        self.value = self.value + [data]
        return self.value

    def exposed_value(self):
        return self.value

    def exposed_search_item(self, item):
        if item in self.value:
            return True
        else:
            return False

    def exposed_remove_item(self, item):
        if item in self.value:
            self.value.remove(item)

    def exposed_insert_item_at_index(self, item, index):
        self.value.insert(index, item)

    def exposed_sort_list(self):
        self.value.sort()


if __name__ == "__main__":
    server = ThreadedServer(DBList(), port=PORT)
    server.start()

